# Smart Farming — Setup Guide

## Quick Start (3 steps)

```bash
pip install django pillow
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000

---

## What's Fixed in v7

### ✅ Live Weather (wttr.in — FREE, No API Key)
- Type any Indian city → press Enter or click "Get Weather"
- Uses **wttr.in** which is 100% free, no signup, no API key
- Shows: temperature, humidity, wind, rain, feels like, cloud cover
- 3-day forecast with rain amounts
- Automatic crop alerts (heat, rain, fungal disease, frost, wind)
- **Remembers your city** — next visit loads automatically

### ✅ Photo Upload (Community Posts)
- Click "📷 Upload Photo" button in community form
- Select photo from phone/computer — preview shows instantly
- Photos save to `media/community/` folder
- Displayed in posts (auto-resized, 280px max height)
- Max 5MB per photo

### ✅ Submit Query (Ask Expert)
- All form fields properly validated
- Error messages shown if fields are missing
- Try/except prevents server crashes
- Phone number field added (optional)
- Success message confirms submission

---

## Pillow (for photo uploads)

```bash
pip install Pillow
# OR if using system Python:
pip install Pillow --break-system-packages
```

If you cannot install Pillow, comment out the `photo = models.ImageField(...)` line
in `farming/models.py` and the photo upload will be disabled but everything else works.

---

## Files Structure
```
smartfarm/
├── manage.py
├── db.sqlite3          ← created on first migrate
├── media/              ← created on first photo upload
│   └── community/      ← uploaded photos go here
├── smartfarm/
│   ├── settings.py
│   └── urls.py
└── farming/
    ├── models.py       ← CommunityPost with photo field
    ├── views.py        ← All views with error handling
    ├── urls.py
    └── templates/
        └── farming/
            ├── base.html       ← Translate bar, accessibility
            ├── weather.html    ← Live weather (wttr.in)
            ├── community.html  ← Photo upload + posts
            ├── ask_expert.html ← Query form
            └── ...
```
