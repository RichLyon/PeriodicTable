Write-Host "Starting Periodic Table Application..."
Write-Host ""

# Start the backend server
Write-Host "Starting backend server..."
Start-Process powershell -ArgumentList "-Command cd '$PSScriptRoot\backend'; pip install -r requirements.txt; python app.py"

# Wait a moment for the backend to start
Write-Host "Waiting for backend to initialize..."
Start-Sleep -Seconds 5

# Start the frontend server
Write-Host "Starting frontend server..."
Start-Process powershell -ArgumentList "-Command cd '$PSScriptRoot\frontend'; npm install; npm start"

Write-Host ""
Write-Host "Servers are starting in separate windows."
Write-Host "Backend will run on http://localhost:5000"
Write-Host "Frontend will run on http://localhost:3000"
Write-Host ""
Write-Host "Press any key to exit this window (servers will continue running)..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
