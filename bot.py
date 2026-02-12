import feedparser
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise ValueError("Faltan las variables de entorno TELEGRAM_TOKEN o TELEGRAM_CHAT_ID")

RSS_URL = "https://www.discudemy.com/feed"
FILE = "sent.txt"


# Cargar cursos ya enviados
if os.path.exists(FILE):
    with open(FILE, "r") as f:
        sent_courses = set(f.read().splitlines())
else:
    sent_courses = set()


def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)

    if response.status_code != 200:
        print("Error enviando mensaje:", response.text)


def check_courses():
    print("Buscando cursos gratis...")

    feed = feedparser.parse(RSS_URL)

    if not feed.entries:
        print("No se pudo leer el RSS.")
        return

    new_courses = 0

    for entry in feed.entries[:10]:
        title = entry.title
        link = entry.link

        if link not in sent_courses:

            message = f"🎓 CURSO GRATIS DETECTADO\n\n{title}\n{link}"

            send_telegram(message)

            sent_courses.add(link)

            with open(FILE, "a") as f:
                f.write(link + "\n")

            new_courses += 1

    print(f"Cursos nuevos enviados: {new_courses}")


check_courses()
