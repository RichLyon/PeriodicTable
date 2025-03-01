@echo off
echo Starting Periodic Table Application...
echo.

REM Start the backend server
start cmd /k "cd backend && pip install -r requirements.txt && python app.py"

REM Wait a moment for the backend to start
timeout /t 5

REM Start the frontend server
start cmd /k "cd frontend && npm install && npm start"

echo.
echo Servers are starting in separate windows.
echo Backend will run on http://localhost:5000
echo Frontend will run on http://localhost:3000
echo.
echo Press any key to exit this window (servers will continue running)...
pause > nul
