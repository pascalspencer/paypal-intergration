# Import flask and paypalrestsdk modules
from flask import Flask, request, redirect, url_for
import paypalrestsdk

# Initialize the flask app
app = Flask(__name__)

# Configure your paypal credentials
paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET" })

# Define a route for creating a payment
@app.route("/create_payment")
def create_payment():
  # Create a payment object with the desired amount, currency and intent
  payment = paypalrestsdk.Payment({
    "intent": "sale",
    "payer": {
      "payment_method": "paypal" },
    "redirect_urls": {
      "return_url": url_for("execute_payment", _external=True),
      "cancel_url": url_for("cancel_payment", _external=True) },
    "transactions": [{
      "amount": {
        "total": "10.00",
        "currency": "USD" } }] })

  # Create the payment and get the approval url
  if payment.create():
    print("Payment created successfully")
    for link in payment.links:
      if link.rel == "approval_url":
        approval_url = link.href
        print("Redirecting to {}".format(approval_url))
        return redirect(approval_url)
  else:
    print(payment.error)
    return "Error creating payment"

# Define a route for executing a payment
@app.route("/execute_payment")
def execute_payment():
  # Get the payment id and payer id from the request parameters
  payment_id = request.args.get("paymentId")
  payer_id = request.args.get("PayerID")

  # Get the payment object by id
  payment = paypalrestsdk.Payment.find(payment_id)

  # Execute the payment using the payer id
  if payment.execute({"payer_id": payer_id}):
    print("Payment executed successfully")
    return "Payment executed"
  else:
    print(payment.error)
    return "Error executing payment"

# Define a route for canceling a payment
@app.route("/cancel_payment")
def cancel_payment():
  return "Payment canceled"

# Run the app
if __name__ == "__main__":
  app.run(debug=True)