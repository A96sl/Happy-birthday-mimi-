from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def order():
    name = request.form['name']
    flavor = request.form['flavor']
    message = request.form['message']
    
    # In a real application, you would process the order here
    print(f"Order received: {mimi} ordered a {flavor} cake with message: {message}")
    
    return f"Thank you, {name}! Your {flavor} cake will be ready soon."

if __name__ == '__main__':
    app.run(debug=True)
