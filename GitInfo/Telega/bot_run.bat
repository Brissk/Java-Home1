@echo off

call %~dp0Telega\.venv\Scripts\activate

cd %~dp0Telega

set TOKEN=5551912606:AAGxqI31CII1UeKAh_0QNyCi5encrUDQoqY

python telegram_bot.py

pause