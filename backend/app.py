from flask import Flask, request, render_template, session
import json
import requests
import razorpay
import os

#KEY = os.environ['KEY']
#SECRET = os.environ['SECRET']
client = razorpay.Client(auth=("<APP_ID>", "<APP_SECRET>"))
app = Flask(__name__)
@app.route('/health', methods=['GET'])
def health_check():
    """
    To check if the server is up or not
    """
    return "O.K", 200

@app.route('/')
def donation_page():
    return render_template('index.html')

@app.route('/donate', methods=['POST'])
def donation_logic():
    amount = request.form['amount']
    payment_type = request.form['type']
    print(payment_type)
    if payment_type == "one_time":
        session['amount'] = amount + '00'
        return render_template('app.html', amount=session['amount']) 
    elif payment_type == "subscription":
        plans = client.plan.all()
        return "Work in progress"

def explore_plans(amount, plans):
    pass


@app.route('/charge', methods=['POST'])
def app_charge():
    amount = int(session['amount'])
    payment_id = request.form['razorpay_payment_id']
    client.payment.capture(payment_id, amount)
    session.pop('amount', 0)
    return json.dumps(client.payment.fetch(payment_id))

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run()