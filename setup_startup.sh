#!/usr/bin/env bash
# helper to install bot execution at boot using cron
# Usage: ./setup_startup.sh /path/to/project

PROJECT_DIR="${1:-$(pwd)}"
PYTHON=$(command -v python3)

if [[ -z "$PYTHON" ]]; then
    echo "python3 not found in PATH" >&2
    exit 1
fi

CRON_ENTRY="@reboot cd $PROJECT_DIR && $PYTHON $PROJECT_DIR/bot.py"

# add entry if not already present
(crontab -l 2>/dev/null | grep -F -v "$PROJECT_DIR/bot.py"; echo "$CRON_ENTRY") | crontab -

echo "Installed @reboot cron job. Verify with: crontab -l"