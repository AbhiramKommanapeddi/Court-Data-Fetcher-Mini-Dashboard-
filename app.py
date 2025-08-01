from flask import Flask, render_template, request, redirect, url_for
from scraper import fetch_case_details
from models import init_db, log_query

app = Flask(__name__)

# Initialize database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']

    try:
        case_details, raw_html = fetch_case_details(case_type, case_number, filing_year)
        
        # Log query & raw response
        log_query(case_type, case_number, filing_year, raw_html)
        
        if case_details:
            return render_template('result.html', data=case_details)
        else:
            return render_template('result.html', data=None, error="No case details found.")
    except Exception as e:
        return render_template('result.html', data=None, error=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
