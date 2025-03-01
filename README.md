# Interactive Periodic Table Application

This application displays an interactive periodic table of elements with detailed information and Bohr model visualizations when hovering over elements.

## Features

- Interactive periodic table with color-coded element categories
- Detailed element information on hover
- Animated Bohr model visualization showing electron shells
- Responsive design that works on various screen sizes

## Technologies Used

- **Backend**: Python with Flask
- **Frontend**: React with styled-components
- **Visualization**: HTML5 Canvas for Bohr model animation

## Project Structure

```
periodic-table-app/
├── backend/               # Python Flask backend
│   ├── app.py             # Flask API server
│   ├── elements_data.py   # Periodic table data
│   └── requirements.txt   # Python dependencies
├── frontend/              # React frontend
│   ├── public/            # Static files
│   └── src/               # React source code
│       ├── components/    # React components
│       │   ├── BohrModel.js         # Electron shell visualization
│       │   ├── ElementCell.js       # Individual element display
│       │   ├── ElementDetails.js    # Detailed element information
│       │   └── PeriodicTable.js     # Main periodic table grid
│       ├── App.js         # Main React application
│       └── index.js       # React entry point
└── run_app.bat            # Script to run both servers
```

## Setup and Running

### Prerequisites

- Python 3.6 or higher
- For the React frontend: Node.js and npm

### Running the Application

#### Option 1: Simple HTML Frontend (No Node.js required)

The easiest way to run the application without Node.js is to use the simple HTML frontend:

1. Double-click on `run_simple_app.bat` in the project root directory
2. This will start the backend server in a separate window
3. The simple HTML frontend will automatically open in your default browser

#### Option 2: React Frontend (Requires Node.js)

If you have Node.js installed, you can run the full React frontend:

1. Double-click on `run_app.bat` in the project root directory
2. This will start both the backend and frontend servers in separate windows
3. The frontend will automatically open in your default browser at http://localhost:3000

**Note:** If you encounter issues with the React frontend not loading data, check that:
- Node.js and npm are properly installed (run `node -v` and `npm -v` to verify)
- The backend server is running on port 5000
- The API endpoint in `frontend/src/App.js` is correctly set to `http://localhost:5000/api/elements` (not just `/api/elements`)

### Manual Setup

If you prefer to start the servers manually:

#### Backend

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Start the Flask server:
   ```
   python app.py
   ```

4. The backend API will be available at http://localhost:5000

#### Frontend (Option 1: Simple HTML)

1. Start the backend server as described above
2. Open the `simple-frontend/index.html` file in your browser

#### Frontend (Option 2: React)

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install the required npm packages:
   ```
   npm install
   ```

3. Start the React development server:
   ```
   npm start
   ```

4. The frontend will automatically open in your default browser at http://localhost:3000

## Usage

- Browse the periodic table by scrolling and looking at the color-coded elements
- Hover over any element to see detailed information and a Bohr model visualization
- The Bohr model shows the electron configuration with animated electrons orbiting the nucleus
