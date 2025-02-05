from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Product data
products = {
    'hand_painted_tote_bags': [
        {'name': 'Floral Tote Bag', 'description': 'Hand-painted with love. Cotton material.', 'price': '₹300', 'image': 'product1.jpg'},
        {'name': 'Abstract Art Tote', 'description': 'Unique design, durable fabric.', 'price': '₹400', 'image': 'product2.jpg'}
        # Add more products as needed
    ],
    # Define other categories similarly
    'hand_painted_clothes': [
        {'name': 'Floral tees', 'description': 'Hand-painted with love. Cotton material.', 'price': '₹600', 'image': 'product3.jpg'},
        {'name': 'Abstract Art Tees', 'description': 'Unique design, durable fabric.', 'price': '₹700', 'image': 'product4.jpg'}],
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/category/<category_name>')
def category(category_name):
    if category_name not in products:
        return "Category not found", 404
    return render_template('category.html', category_name=category_name, products=products[category_name])

@app.route('/order', methods=['POST'])
def order():
    if request.method == 'POST':
        product_name = request.form['product_name']
        customer_name = request.form['customer_name']
        customer_email = request.form['customer_email']
        message = f"New order received:\nProduct: {product_name}\nCustomer Name: {customer_name}\nCustomer Email: {customer_email}"

        # Send email notification
        send_email('New Order Received', message)

        return redirect(url_for('home'))

def send_email(subject, body):
    sender_email = 'kashishsharma211099@acropolis.in'
    receiver_email = 'kashisharma1912@gmail.com'
    password = 'Reset1912'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == '__main__':
    app.run(debug=True)
