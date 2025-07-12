# 📝 BLOG_APP

A simple Django-based Blog Application that allows users to register, login, and create blog posts. Built for learning, personal use, or small blogging platforms.

---

## 🚀 Features

- User registration and login system
- Create, update, and delete blog posts
- Dashboard for managing your own posts
- Home page displaying all blogs
- Admin panel for full control
- Fully responsive UI with HTML/CSS

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap optional)
- **Database**: SQLite (default Django DB)

---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Archie519/BLOG_APP.git
cd BLOG_APP

### 2. Create a Virtual Environment
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Run the Server
python manage.py runserver

## 📁 Project Structure
BLOG_APP/
├── blog/               # Main app
│   ├── templates/      # HTML templates
│   ├── views.py        # Views
│   └── urls.py         # App-specific URLs
├── BLOG_APP/           # Project settings
├── db.sqlite3          # Default database
├── manage.py           # Django manager

🙌 Author
Made by Archie Arora
GitHub: @Archie519
