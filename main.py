import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "core"))
import asyncio
import sys, os

# добавляем путь, чтобы core находился всегда
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "core"))

from core.telegram_bot import main as start_bot

if __name__ == "__main__":
    try:
        asyncio.run(start_bot())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(start_bot())
        loop.run_forever()
