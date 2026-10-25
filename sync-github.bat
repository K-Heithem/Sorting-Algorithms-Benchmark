@echo off
setlocal enabledelayedexpansion

echo ============================================================
echo   Syncing WorkJob / Sorting Algorithms to GitHub...
echo ============================================================

cd /d "%~dp0"

echo [1/3] Adding changes...
git add .

echo [2/3] Committing changes...
set "MSG=%~1"
if "!MSG!"=="" (
    for /f "tokens=1-4 delims=/ " %%a in ("%date%") do set mydate=%%c-%%a-%%b
    for /f "tokens=1-2 delims=: " %%a in ("%time%") do set mytime=%%a:%%b
    set "MSG=Update progress - !mydate! !mytime!"
)
git commit -m "!MSG!"

echo [3/3] Pushing to GitHub (main)...
git push origin main

echo.
if %ERRORLEVEL% EQU 0 (
    echo [SUCCESS] Everything has been pushed to GitHub!
) else (
    echo [NOTICE] If branch is not yet set up, pushing -u origin main...
    git push -u origin main
)

echo.
pause
