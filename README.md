# Superheroes API

A Flask API for tracking heroes and their superpowers.

## Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Initialize the database:
   - `flask db init`
   - `flask db migrate`
   - `flask db upgrade`
5. Seed the database: `python seed.py`
6. Run the server: `python app.py`

## API Endpoints

### Heroes
- `GET /heroes` - Get all heroes
- `GET /heroes/<int:id>` - Get a specific hero by ID

### Powers
- `GET /powers` - Get all powers
- `GET /powers/<int:id>` - Get a specific power by ID
- `PATCH /powers/<int:id>` - Update a power's description

### HeroPowers
- `POST /hero_powers` - Create a new hero-power association

## Models

### Hero
- id: Integer
- name: String
- super_name: String

### Power
- id: Integer
- name: String
- description: String (must be at least 20 characters)

### HeroPower
- id: Integer
- strength: String (must be 'Strong', 'Weak', or 'Average')
- hero_id: Integer (foreign key)
- power_id: Integer (foreign key)