# Flask PayPal Payment Integration

## Overview
This is a simple Flask application that integrates PayPal payments using the `paypalrestsdk` library. The app allows users to create, execute, and cancel PayPal payments.

## Features
- Create a PayPal payment
- Redirect users to PayPal for approval
- Execute the payment upon user confirmation
- Handle payment cancellations

## Requirements
- Python 3.x
- Flask
- PayPal REST SDK (`paypalrestsdk`)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/flask-paypal-integration.git
   cd flask-paypal-integration
   ```

2. Install dependencies:
   ```bash
   pip install flask paypalrestsdk
   ```

3. Configure your PayPal credentials in the script:
   ```python
   paypalrestsdk.configure({
     "mode": "sandbox", # Change to "live" for production
     "client_id": "YOUR_CLIENT_ID",
     "client_secret": "YOUR_CLIENT_SECRET"
   })
   ```

## Running the Application

Run the Flask app:
```bash
python paypal.py
```

The application will start at `http://127.0.0.1:5000/`.

## Usage

1. **Create a Payment:**
   - Navigate to `http://127.0.0.1:5000/create_payment`
   - The app will redirect you to PayPal for approval.

2. **Execute a Payment:**
   - After approving the payment on PayPal, you will be redirected to `http://127.0.0.1:5000/execute_payment`.
   - The payment will be executed and confirmed.

3. **Cancel a Payment:**
   - If the user cancels the payment, they will be redirected to `http://127.0.0.1:5000/cancel_payment`.

## Notes
- Ensure that your PayPal client credentials are correct.
- Use the sandbox mode for testing before switching to live mode.

## License
This project is licensed under the MIT License.

