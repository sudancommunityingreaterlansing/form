#from flask import Flask, render_template, request, redirect
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
#from datetime import datetime

import os
import json
from oauth2client.service_account import ServiceAccountCredentials

creds_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])


#app = Flask(__name__)

# Google Sheets setup
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

#creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
#client = gspread.authorize(creds)

sheet = client.open("SudaneseMembership").sheet1  # must match your sheet name

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form.get('email', '')
    location = request.form.get('location', '')
    interests = request.form.get('interests', '')
    consent = "Yes"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append row to Google Sheet
    sheet.append_row([name, phone, timestamp])

    return redirect('/success')

@app.route('/success')
def success():
    return "✅ Submitted successfully!"

if __name__ == '__main__':
    if __name__ == "__main__":
       app.run(host="0.0.0.0", port=10000)
