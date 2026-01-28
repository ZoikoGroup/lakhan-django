# Django Backend Project

A Django backend application providing REST-style APIs with a modular app structure.  
The project is configured to run locally and is suitable for frontend integration (React / Next.js).

---

## Tech Stack
- Python 3.12
- Django
- SQLite
- django-cors-headers
- django-filter
- whitenoise
- pillow

---

## Local Setup

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install django django-cors-headers django-filter whitenoise pillow (if needed)
python manage.py migrate
python manage.py runserver
