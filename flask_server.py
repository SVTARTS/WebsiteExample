import flask
from flask import Flask, request, redirect, url_for, render_template, session, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session management

# Dummy user database
users = {'jching1': 'password1'}

# In-memory order storage
order_list  = []

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/fetch_orders')
def fetch_orders():
    return jsonify(order_list)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Process the order
        product = request.form['product']
        quantity = request.form['quantity']
        structure_type = request.form['Structure Type']
        structure_description = request.form['Structure Description']
        call_freq = request.form['Call Freq']
        spread = request.form['Spread (Bps)']
        settlement_date = request.form['Settlement Date: ']
        maturity_date = request.form['Maturity Date: ']
        order_amount = request.form['Order Amount (MM): ']
        investor = request.form['Investor: ']
        
        order_list .append({'product': product, 
        'quantity': quantity,
        'structure_type': structure_type,
        'structure_description' : structure_description,
        'call_freq': call_freq,
        'spread': spread,
        'settlement_date' : settlement_date,
        'maturity_date': maturity_date,
        'order_amount': order_amount,
        'investor':investor
        })        

        return redirect(url_for('home'))
    return render_template('order.html')

@app.route('/orders')
def orders():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    print('The order list is: ', order_list)
    return render_template('orders.html', order_list=order_list)

@app.route('/submit', methods=['POST'])
def submit_order():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Logic to submit all orders could go here
    return "Orders submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
