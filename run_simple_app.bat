@echo off
echo Starting Periodic Table Application...
echo.

REM Start the backend server
start cmd /k "cd backend && pip install -r requirements.txt && python app.py"

REM Wait a moment for the backend to start
timeout /t 5

REM Open the simple frontend in the default browser
start "" "simple-frontend\index.html"

echo.
echo Backend server is running in a separate window.
echo Backend API is available at http://localhost:5000
echo Frontend is opening in your default browser.
echo.
echo Press any key to exit this window (backend server will continue running)...
pause > nul
