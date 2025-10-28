# Portfolio Backend API

A FastAPI-based backend service for managing a personal portfolio website with authentication, profile management, skills, and projects.

## Features

- 🔐 **Authentication**

  - Admin login with JWT tokens
  - Protected admin routes
  - Public client routes
  
- 👤 **Profile Management**

  - Create/Update personal profile
  - Manage social links
  - Public profile viewing

- 💪 **Skills Management**

  - CRUD operations for skills
  - Skill categorization
  - Proficiency levels (1-5)

- 🚀 **Projects Management**
  - CRUD operations for projects
  - Project status tracking
  - Tech stack management
  - GitHub, docs, and live URL support

## API Endpoints

### Authentication

- `POST /api/v1/admin/token` - Admin login
- `GET /api/v1/admin/me` - Get current admin info

### Admin Routes (Protected)

#### Profile

- `GET /api/v1/admin/profile/` - Retrieve profile
- `POST /api/v1/admin/profile/` - Create profile
- `PUT /api/v1/admin/profile/` - Update profile

#### Skills

- `GET /api/v1/admin/skills/` - List all skills
- `POST /api/v1/admin/skills/` - Create new skill
- `GET /api/v1/admin/skills/{skill_id}` - Get specific skill
- `PUT /api/v1/admin/skills/{skill_id}` - Update skill
- `DELETE /api/v1/admin/skills/{skill_id}` - Delete skill

#### Projects

- `GET /api/v1/admin/projects/` - List all projects
- `POST /api/v1/admin/projects/` - Create new project
- `GET /api/v1/admin/projects/{id}` - Get specific project
- `PUT /api/v1/admin/projects/{id}` - Update project
- `DELETE /api/v1/admin/projects/{id}` - Delete project

### Client Routes (Public)

- `GET /api/v1/clients/profiles` - View public profile
- `GET /api/v1/clients/skills` - View all skills
- `GET /api/v1/clients/skills/{id}` - View specific skill
- `GET /api/v1/clients/projects` - View all projects
- `GET /api/v1/clients/projects/{id}` - View specific project

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .penv
   source .penv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env`:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_URL=your_database_url
   ```

## Running the Application

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
backend/
├── auth/                      # Authentication related modules
│   ├── auth_dependencies.py
│   ├── auth_schema.py
│   ├── auth_utils.py
│   └── auth.py
├── core/                      # Core configurations
│   ├── config.py             # App configuration
│   └── db.py                 # Database setup
├── src/
│   ├── app/
│   │   ├── profile/          # Profile management
│   │   │   ├── profile_model.py
│   │   │   ├── profile_repo.py
│   │   │   ├── profile_route.py
│   │   │   ├── profile_schemas.py
│   │   │   └── profile_service.py
│   │   ├── project/          # Project management
│   │   │   ├── project_model.py
│   │   │   ├── project_repo.py
│   │   │   ├── project_route.py
│   │   │   ├── project_schemas.py
│   │   │   └── project_service.py
│   │   └── skillset/         # Skills management
│   │       ├── skill_model.py
│   │       ├── skill_repo.py
│   │       ├── skill_route.py
│   │       ├── skill_schemas.py
│   │       └── skill_service.py
│   ├── router/               # API route handlers
│   │   ├── admin_route.py
│   │   └── client_route.py
│   └── utils/                # Utility modules
│       └── error/           # Error handling
│           ├── error_handler.py
│           └── errors.py
├── .env                      # Environment variables
├── .gitignore               # Git ignore rules
├── main.py                  # Application entry point
├── requirements.txt         # Project dependencies
├── route.py                # Route definitions
└── swagger.json            # API documentation
```
