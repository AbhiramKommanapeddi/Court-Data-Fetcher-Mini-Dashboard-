from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

def fetch_case_details(case_type, case_number, filing_year):
    url = "https://services.ecourts.gov.in/ecourtindia_v6/"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 👈 Run non-headless for debugging first
        context = browser.new_context(user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/119.0.0.0 Safari/537.36"
        ))
        page = context.new_page()
        try:
            page.goto(url, timeout=60000)  # 👈 Increase timeout to 60s
            print("✅ Page loaded successfully")

            # TODO: Navigate to case status page and scrape data here
            html = page.content()

            case_data = {
                "petitioner": "John Doe",
                "respondent": "State of Haryana",
                "filing_date": "2024-05-10",
                "next_hearing": "2025-08-20",
                "pdf_link": "https://services.ecourts.gov.in/sample_order.pdf"
            }
            return case_data, html
        except Exception as e:
            raise Exception(f"Scraping failed: {str(e)}")
        finally:
            browser.close()
