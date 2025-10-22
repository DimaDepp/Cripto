import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "core"))
# main.py
import asyncio
from telegram_bot import main as start_bot  # вместо from core.telegram_bot
