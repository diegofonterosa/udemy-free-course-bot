#!/usr/bin/env python3
import logging
import os
import sys
import time
from pathlib import Path
from typing import Set

import feedparser
import requests
import schedule
from dotenv import load_dotenv


# ----- configuration and helpers -----

def load_config():
    """Read configuration from environment variables.

    Requires TELEGRAM_TOKEN and TELEGRAM_CHAT_ID. Optional variables:
    RSS_URL (defaults to discudemy feed) and SENT_FILE (defaults to sent.txt).
    """
    load_dotenv()
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    rss_url = os.getenv("RSS_URL", "https://www.discudemy.com/feed")
    data_file = Path(os.getenv("SENT_FILE", "sent.txt"))

    if not token or not chat_id:
        logging.error("Missing required environment variables TELEGRAM_TOKEN or TELEGRAM_CHAT_ID")
        sys.exit(1)

    return token, chat_id, rss_url, data_file


def load_sent_courses(path: Path) -> Set[str]:
    """Return a set of already-sent course URLs from disk."""
    if path.exists():
        try:
            with path.open("r", encoding="utf-8") as f:
                return {line.strip() for line in f if line.strip()}
        except Exception:
            logging.exception("Failed to read sent courses file")
            return set()
    return set()


def save_course(path: Path, link: str) -> None:
    """Append a new course URL to the sent-file."""
    try:
        with path.open("a", encoding="utf-8") as f:
            f.write(link + "\n")
    except Exception:
        logging.exception("Failed to save course link")


def send_telegram(token: str, chat_id: str, message: str) -> bool:
    """Post a message to the configured Telegram chat."""
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        resp = requests.post(url, data={"chat_id": chat_id, "text": message}, timeout=10)
        if resp.status_code != 200:
            logging.error("Telegram API returned %s: %s", resp.status_code, resp.text)
            return False
        return True
    except requests.RequestException:
        logging.exception("Error sending telegram message")
        return False


def check_courses(
    token: str,
    chat_id: str,
    rss_url: str,
    sent_courses: Set[str],
    data_file: Path,
    limit: int = 10,
) -> int:
    """Fetch RSS feed and notify new courses. Returns number of new items sent."""
    logging.info("Checking for free courses")
    try:
        feed = feedparser.parse(rss_url)
    except Exception:
        logging.exception("Failed to parse RSS feed")
        return 0

    if not feed.entries:
        logging.warning("RSS feed empty or could not be read")
        return 0

    new = 0
    for entry in feed.entries[:limit]:
        title = getattr(entry, "title", "")
        link = getattr(entry, "link", "")
        if not link or link in sent_courses:
            continue

        msg = f"🎓 CURSO GRATIS DETECTADO\n\n{title}\n{link}"
        if send_telegram(token, chat_id, msg):
            sent_courses.add(link)
            save_course(data_file, link)
            new += 1
    logging.info("New courses sent: %d", new)
    return new


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    token, chat_id, rss_url, data_file = load_config()
    sent = load_sent_courses(data_file)

    # Schedule the check task every 5 minutes
    def job():
        nonlocal sent
        sent = load_sent_courses(data_file)
        check_courses(token, chat_id, rss_url, sent, data_file)

    schedule.every(5).minutes.do(job)
    logging.info("Bot started, checking for courses every 5 minutes")

    # Run the scheduler loop
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Bot stopped by user")
        sys.exit(0)


if __name__ == "__main__":
    main()
