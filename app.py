from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

last_claim = False


# ------------------ HOME ------------------
@app.route('/')
def home():
    return render_template('home.html')


# ------------------ REGISTER ------------------
@app.route('/register')
def register():
    return render_template('register.html')


# ------------------ DASHBOARD ------------------
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        income = int(request.form['income'])

        premium = 20

        if income > 800:
            premium += 10

        if city.lower() in ["chennai", "mumbai", "kolkata"]:
            premium += 20

        risk = "High" if premium > 40 else "Low"

        return render_template(
            'dashboard.html',
            name=name,
            risk=risk,
            premium=premium,
            city=city
        )

    # 👇 This handles GET request (when clicking link)
    return render_template(
        'dashboard.html',
        name="Guest",
        risk="N/A",
        premium=0,
        city="Unknown"
    )

# ------------------ CLAIM PAGE (NEW) ------------------
@app.route('/claim/<type>')
def claim(type):
    city = request.args.get('city')

    if type == "rain":
        message = "🌧 Heavy rain detected"
        payout = 300
    elif type == "heat":
        message = "🌡 Heatwave detected"
        payout = 200
    elif type == "pollution":
        message = "🌫 Pollution detected"
        payout = 150
    else:
        message = "Unknown event"
        payout = 0

    return render_template(
        'claim_result.html',
        type=type,
        message=message,
        payout=payout,
        city=city
    )


# ------------------ TRIGGER (API + FRAUD) ------------------
@app.route('/trigger')
def trigger():
    global last_claim

    if last_claim:
        return jsonify({
            "message": "⚠ Fraud detected! Duplicate claim blocked",
            "payout": 0
        })

    city = request.args.get('city')

    api_key = "47ae4a07808903e39fa41de9147c9328"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return jsonify({
            "message": "❌ City not found or API error",
            "payout": 0
        })

    weather = data['weather'][0]['main']

    if weather.lower() == "rain":
        payout = 300
        message = "🌧 Real Rain detected!"
    elif weather.lower() == "clear":
        payout = 0
        message = "☀ No disruption"
    else:
        payout = 150
        message = f"{weather} condition detected!"

    last_claim = True

    return jsonify({
        "message": message,
        "payout": payout
    })


# ------------------ RUN ------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)