# Personal Development AI Web Application

A comprehensive web application for personal development powered by AI, offering intelligent journaling, goal tracking, and self-reflection tools.

## 🌟 Features

- **Smart Journaling**: AI-enhanced journal entries with mood analysis
- **Goal Tracking**: Structured goal setting with progress monitoring
- **Reflection Tools**: Guided self-reflection with AI-generated insights
- **User Profiles**: Customizable user experience with AI preference settings
- **REST API**: Full-featured API with JWT authentication

## 🔧 Tech Stack

### Backend
- Django 5.1.7
- Django REST Framework 3.15.2
- JWT Authentication
- SQLite (Development) / PostgreSQL (Production-ready)

### Frontend (Planned)
- React with TypeScript
- Material-UI components
- Redux for state management

## 📋 Prerequisites

- Python 3.11 or higher
- Node.js 18+ (for frontend)
- Git
- WSL or Linux environment

## 🚀 Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/personal-dev-ai.git
cd personal-dev-ai
```

2. **Set up Python environment**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Environment Variables**
```bash
cp .env.example .env
# Edit .env with your settings
```

4. **Database Setup**
```bash
python manage.py migrate
python manage.py createsuperuser
```

5. **Run Development Server**
```bash
python manage.py runserver
```

## 🏗️ Project Structure

```
personal-dev-ai/
├── backend/
│   ├── core/            # Project configuration
│   ├── users/           # User management
│   ├── journaling/      # Journal functionality
│   ├── goals/           # Goal tracking
│   ├── reflections/     # Reflection tools
│   └── ai_integration/  # AI services
├── docs/                # Documentation
├── frontend/            # React frontend (planned)
└── scripts/            # Utility scripts
```

## 📝 API Endpoints

### Authentication
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token

### Users
- `GET /api/users/me/` - Current user profile
- `PATCH /api/users/me/` - Update profile

### Journaling
- `GET /api/journals/` - List entries
- `POST /api/journals/` - Create entry
- `GET /api/journals/{id}/` - Retrieve entry
- `PUT /api/journals/{id}/` - Update entry
- `DELETE /api/journals/{id}/` - Delete entry

## 🧪 Testing

```bash
# Run backend tests
python manage.py test

# Run with coverage
coverage run manage.py test
coverage report
```

## 🛠️ Development Status

### Completed
- ✅ Core backend structure
- ✅ User authentication
- ✅ Journal entry system
- ✅ Goal tracking models

### In Progress
- 🔄 AI integration services
- 🔄 Reflection system
- 🔄 Frontend development

### Planned
- 📋 Advanced AI analysis
- 📋 Mobile responsive design
- 📋 Data visualization
- 📋 Export functionality

## 📚 Documentation

Detailed documentation is available in the `/docs` directory:
- Architecture Overview
- API Documentation
- Development Guide
- Deployment Instructions

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

For support, email [your-email@example.com] or open an issue in the repository.