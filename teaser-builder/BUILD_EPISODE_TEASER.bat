@echo off
title The God Queen - Episode Teaser
cd /d "%~dp0"
where ffmpeg >nul 2>nul || (winget install --id Gyan.FFmpeg -e --accept-source-agreements --accept-package-agreements & echo Close this window and run it again. & pause & exit /b)
python -c "import PIL" 2>nul || pip install pillow
set /p EP=Episode number: 
python make_teaser.py %EP%
if exist "..\teasers" start "" "..\teasers"
pause
