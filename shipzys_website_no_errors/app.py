
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.to_dict()
    return f"Form submitted successfully! Data: {data}"

if __name__ == "__main__":
    app.run(debug=True)
