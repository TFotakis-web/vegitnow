# Wais

Deploy
```bash
mkdir logs
pip install -r requirements.txt
cd frontend
npm install
```

Setup database
```
python manage.py makemigrations
python manage.py migrate
```

Create superuser
```bash
python manage.py createsuperuser
```

Run DJango backend server
```bash
python manage.py runserver localhost:8000
```

Run VueJS webpack (frontend) server
```bash
cd frontend
npm run dev
```

- http://localhost:8080 for live reload
- http://localhost:8000 for full server experience
