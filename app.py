# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC31d7734a3411f343a503cc2fd3bcbf29'
        auth_token = '3491efa3b7b1e41d74cc1360140668d6'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('VA62cd6934ec6ef4f53aedab602cb730ac') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp')
def get_otp():
    print("Processing")
    recieved_otp = request.form['recieved_otp']
    mobile_number = request.form['number']



    auth_token = '3491efa3b7b1e41d74cc1360140668d6'
    client = client(account_sid, auth_token)

    verification_check = client.verify \
        .services('VA62cd6934ec6ef4f53aedab602cb730ac') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification.status)
    if verification_check.status == "pending":
        return "Entered OTP is wrong"
    else:
        return redirect('https://project-c272.onrender.com/')





if __name__ == "__main__":
    app.run()

