# Court-Data-Fetcher-Mini-Dashboard-# 🏛 Court-Data Fetcher & Mini-Dashboard

A simple web app to fetch and display **Indian Court case metadata** (parties’ names, filing/next-hearing dates, and latest orders/judgments) based on **Case Type, Case Number, and Filing Year**.

---

## 🎯 Objective
The project queries the **Faridabad District Court** (https://districts.ecourts.gov.in/faridabad) portal, scrapes case details, and presents them neatly on a mini dashboard.

---

## ⚙️ Tech Stack
- **Backend:** Python (Flask)
- **Frontend:** HTML + CSS (Bootstrap-style styling)
- **Scraper:** Playwright (headless browser automation)
- **Database:** SQLite (to log all queries & raw responses)
- **Parser:** BeautifulSoup4

---

## 📂 Project Structure
court-data-fetcher/
│
├── app.py # Flask app entry point
├── scraper.py # Web scraping logic
├── models.py # SQLite DB models (query logging)
├── requirements.txt # Python dependencies
├── templates/
│ ├── index.html # Form UI
│ ├── result.html # Display scraped results
├── static/
│ ├── style.css # Styling for UI
└── README.md # You are here

yaml
Copy code

---

## 🚀 Setup Instructions

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/court-data-fetcher.git
cd court-data-fetcher
✅ 2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
✅ 3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
playwright install
✅ 4. Run the App
bash
Copy code
python app.py
Open your browser → http://127.0.0.1:5000

🖥 How It Works
1️⃣ User enters:

Case Type (Civil/Criminal)

Case Number

Filing Year

2️⃣ Flask sends the query to scraper.py, which:

Navigates to the eCourts portal

Handles CAPTCHA (see below)

Scrapes:

Petitioner/Respondent names

Filing date

Next hearing date

Latest order/judgment PDF link

3️⃣ Results are displayed in a neat UI.

4️⃣ Every query + raw response HTML is logged in SQLite (queries.db).
