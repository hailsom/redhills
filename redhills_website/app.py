from flask import Flask, render_template, request  # Import Flask and necessary modules
from datetime import datetime  # For working with dates

app = Flask(__name__)  # This creates the Flask app

# Function to calculate how many days are in a given month
def month_days(month): 
    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31  # These months have 31 days
    elif month in (4, 6, 9, 11):
        return 30  # These months have 30 days
    else:
        return 28  # February has 28 days (ignoring leap years for simplicity)

cycle_length = 28  # The cycle length is 28 days

# This route shows the home page with the form where users will enter their information
@app.route('/')
def home():
    return render_template('index.html')  # This renders (shows) the 'index.html' page

# This route handles the calculation when the user submits the form
@app.route('/calculate', methods=['POST'])
def calculate():
    # Get user inputs from the form
    last_period_month = int(request.form['last_period_month'])
    last_period_day = int(request.form['last_period_day'])
    period_duration = int(request.form['period_duration'])
    
    # Calculate next period day and month
    next_period_day = last_period_day + cycle_length
    next_period_month = last_period_month

    # Adjust the month and day if we go beyond the number of days in the current month
    while next_period_day > month_days(next_period_month):
        next_period_day -= month_days(next_period_month)
        next_period_month += 1
        if next_period_month > 12:
            next_period_month = 1  # If we pass December, start back at January

    # Check if the user is currently on their period based on today's date
    today = datetime.now()
    period_end = next_period_day + period_duration - 1
    is_on_period = False

    if today.month == next_period_month and next_period_day <= today.day <= period_end:
        is_on_period = True
    elif today.month == next_period_month + 1 and next_period_day > period_end and today.day <= period_end:
        is_on_period = True
    elif next_period_month == 12 and today.month == 1 and today.day <= period_end:
        is_on_period = True

    # Return the results page with the calculated next period date and whether the user is on their period
    return render_template(
        'result.html',  # This renders (shows) the 'result.html' page
        next_period_month=next_period_month,  # Pass the next period month to the result page
        next_period_day=next_period_day,  # Pass the next period day to the result page
        is_on_period=is_on_period  # Pass the "currently on period" status to the result page
    )

if __name__ == '__main__':
    app.run(debug=True)  # This starts the web server so you can view your site