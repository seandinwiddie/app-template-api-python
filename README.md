# app-template-api

This project is an API for an application template.

## Description

This is an API for an application template. It serves as the backend for fetching and providing data to the frontend application.

## Main Components

### API Server (src/main.py)
- Uses FastAPI to create a server
- Implements CORS for cross-origin requests
- Reads initial state from a JSON file
- Provides endpoints for:
  - Homepage
  - Status check
  - Fetching all data
  - Dynamic endpoints for each key in the initial state

### Initial State Data (src/data/initialState.json)
- Contains structured data for the application template
- Same structure as original project

## Project Structure
- `src/main.py`: Contains the main API logic
- `src/data/`: Stores the initial state data

## Dependencies
- FastAPI for the server
- Uvicorn for ASGI server
- CORS middleware for handling cross-origin requests

## Key Features
- Dynamic endpoint generation based on the initial state structure
- Centralized data management through a JSON file
- Support for multiple themes
- BDD test scenarios included in the data

## Running the Project
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Start the server:  
```bash
python src/main.py
```
or
```bash
uvicorn src.main:app --reload --port 3000
```
## Data Flow
The project follows a structure where data is stored in a JSON file, loaded into the API, and then served through various endpoints. This allows for easy updates to the portfolio content without changing the API code.
  