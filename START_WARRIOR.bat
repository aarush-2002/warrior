@echo off
title WARRIOR APP
color 0A
echo.
echo  ============================================
echo    STARTING 100-DAY WARRIOR...
echo  ============================================
echo.

cd /d C:\Users\ASUS\100-day-warrior

echo  Starting Telegram Bot...
start "WARRIOR BOT" cmd /k "cd /d C:\Users\ASUS\100-day-warrior && python telegram_bot.py"

echo  Starting App Server...
echo.
echo  ============================================
echo    APP RUNNING!
echo    Open: http://127.0.0.1:5000
echo    Phone: Check IP below
echo    DON'T CLOSE THIS WINDOW!
echo  ============================================
echo.

python app.py