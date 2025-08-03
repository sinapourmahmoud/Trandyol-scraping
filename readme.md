# 🛍️ Trendyol Scraper Web App

A Flask-based web application that scrapes product data from [Trendyol.com](https://www.trendyol.com/) using Selenium and saves it to a local SQLite database. Users can search for stored products or submit a product URL to fetch live data. The app uses solid OOP principles and includes design patterns like **Singleton** and **Factory**.

---

## 📌 Features

- 🔍 **Search interface** with filters (category, price range, keyword)
- 🔗 **Submit a product URL** and retrieve product info (title, price, rating, etc.)
- 📂 Saves product data to a local **SQLite** database
- 🧱 Clean code structure with **design patterns**
- 💡 Uses **Selenium** for dynamic data scraping
- ✨ Styled with **Tailwind CSS**

---

## 🧠 Design Patterns Used

- **Singleton Pattern**: Ensures only one database connection throughout the app.
- **Factory Pattern**: Abstracts scraper creation based on product type/category.

---

## 🗂️ Project Structure

```
trandyol-bot/
├── templates/             # HTML templates
│   ├── index.html         # Search form with filters
│   └── search.html        # Display product details
│
├── venv/                  # Python virtual environment
│
├── .env                   # Environment variables (e.g., Flask secret key, token)
├── .gitignore             # Ignored files/folders (venv, .db, etc.)
├── app.db                 # SQLite database file
│
├── __init__.py            # Package initializer (optional)
├── bot.py                 # (Unused) Reserved for future Telegram bot
├── database.py            # Singleton DB connection manager
├── main.py                # Legacy entrypoint or logic holder
├── routes.py              # Flask routes and business logic
├── run.py                 # Application entry point
├── test.py                # Tests
├── trandyol.py            # Scraper logic for Trendyol
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/trandyol-bot.git
cd trandyol-bot
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> 📝 If `requirements.txt` doesn't exist, install manually:

```bash
pip install flask selenium
```

### 4. Run the App

```bash
python run.py
```

Open your browser at: [http://localhost:5000](http://localhost:5000)

---

## 🧪 Usage

### 🔎 Search Page

- Go to `/`
- Enter a keyword, select categories, or define a price range
- View filtered results from the database

### 🔗 Submit a Product URL

- Go to `/search`
- Enter a full product URL from Trendyol
- The app scrapes and displays product details (title, price, rating, etc.)

---

## 🧠 Technologies Used

| Tech        | Description                     |
| ----------- | ------------------------------- |
| Python      | Programming language            |
| Flask       | Web framework                   |
| Selenium    | Web scraping automation         |
| SQLite      | Lightweight database            |
| TailwindCSS | Styling the frontend            |
| Jinja2      | Template engine (Flask default) |

---

## ⚙️ Environment Variables

Create a `.env` file in the project root and define the following:

```txt
FLASK_APP=run.py
FLASK_ENV=development
SECRET_TOKEN=your_secret_token_here  # Used for secure Flask session or API access
```

---

## 🚫 Disclaimer

This tool is intended for **educational purposes**. Scraping commercial websites should comply with their [terms of service](https://www.trendyol.com/sayfa/kullanim-sartlari). Use responsibly.

---

## 📄 License

MIT License — feel free to use and modify.

---

## 👨‍💼 Author

Developed by Sina Pourmahmoud.

Feel free to open issues or contribute!

