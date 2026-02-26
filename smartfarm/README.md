# 🌾 Smart Farming Solutions
### Maximizing Crop Yield & Complete Protection from Wildlife, Pests, Insects & Weeds

A full-stack Django web application for Indian farmers to protect their crops and maximize yield.

---

## 🚀 Quick Setup (5 Minutes)

### 1. Install Django
```bash
pip install django
```

### 2. Navigate to project folder
```bash
cd smartfarm
```

### 3. Run Database Migrations
```bash
python manage.py migrate
```
This will create the database AND automatically seed it with:
- 5 Wildlife threats (Wild Boar, Nilgai, Monkeys, Birds, Rodents)
- 5 Pest & Insect threats (Aphids, Army Worm, Whitefly, Termites, Locust)
- 4 Weed threats (Wild Oat, Bathu, Parthenium, Nut Grass)
- 6 Crop production tips

### 4. Create Admin User (optional)
```bash
python manage.py createsuperuser
```

### 5. Run the Development Server
```bash
python manage.py runserver
```

### 6. Open in Browser
Visit: **http://127.0.0.1:8000**

Admin panel: **http://127.0.0.1:8000/admin**

---

## 📱 Pages & Features

| Page | URL | Description |
|------|-----|-------------|
| Home | `/` | Hero, stats, category cards, tips |
| All Threats | `/threats/` | Search, filter by category & severity |
| Threat Detail | `/threats/<id>/` | Full prevention & treatment info |
| Wildlife | `/wildlife/` | All wildlife threats |
| Pests & Insects | `/pests/` | All pest threats |
| Weeds | `/weeds/` | All weed threats |
| Crop Tips | `/crop-tips/` | Filter tips by crop/season |
| Ask Expert | `/ask-expert/` | Submit query form |
| Admin | `/admin/` | Manage all data |

---

## 🛠 Tech Stack

- **Backend:** Django 4.x (Python)
- **Database:** SQLite (via Django ORM)
- **Frontend:** Pure HTML5, CSS3, JavaScript (no external frameworks)
- **Fonts:** Google Fonts (Playfair Display + DM Sans)
- **Admin:** Django built-in admin panel

---

## 🗂 Project Structure

```
smartfarm/
├── manage.py
├── requirements.txt
├── smartfarm/          # Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── farming/            # Main app
    ├── models.py       # Threat, CropTip, FarmerQuery
    ├── views.py        # All page views
    ├── urls.py         # App URL routes
    ├── admin.py        # Admin configuration
    ├── migrations/     # Database migrations + seed data
    └── templates/
        └── farming/
            ├── base.html        # Navigation + Footer
            ├── home.html        # Landing page
            ├── threat_list.html # Search/filter threats
            ├── threat_detail.html  # Individual threat info
            ├── category_page.html  # Wildlife/Pest/Weed pages
            ├── crop_tips.html   # Farming tips
            └── ask_expert.html  # Expert query form
```

---

## ➕ Adding More Data via Admin

1. Go to `/admin/`
2. Login with superuser credentials
3. Add threats, crop tips, or view farmer queries
4. Each threat has: name, category, icon, description, affected crops, prevention methods, treatment, season, severity

---

## 🌱 Built for Indian Farmers
- Covers Punjab's most common threats: Wild Boar, Nilgai, Phalaris minor (wild oat)
- IST timezone configured
- Government resources linked in footer (ICAR, farmer.gov.in, state agriculture departments)
