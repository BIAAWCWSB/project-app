from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('hello_form.html')

if __name__ == '__main__':
    app.run(debug=True)

