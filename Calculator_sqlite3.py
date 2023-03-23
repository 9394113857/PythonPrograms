from flask import Flask, render_template, request
import sqlite3
import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('calculator_sqlite3.log')
file_handler.setFormatter(log_formatter)
app.logger.addHandler(file_handler)


@app.route('/')
def index():
    return render_template('calc.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = request.form['num1']
    num2 = request.form['num2']
    operation = request.form['operation']
    email = request.form['email']
    result = None

    if operation == '+':
        result = float(num1) + float(num2)
    elif operation == '-':
        result = float(num1) - float(num2)
    elif operation == '*':
        result = float(num1) * float(num2)
    elif operation == '/':
        result = float(num1) / float(num2)

    conn = sqlite3.connect('calculator.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS calculations
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              num1 REAL, 
              num2 REAL, 
              operation TEXT, 
              result REAL,
              date DATE,
              time TIME,
              email TEXT)''')

    c.execute(
        "INSERT INTO calculations (num1, num2, operation, result, date, time, email) VALUES (?, ?, ?, ?, date('now'), time('now'), ?)",
        (num1, num2, operation, result, email))
    conn.commit()
    conn.close()

    app.logger.info(f"{num1} {operation} {num2} = {result} by {email}")

    return render_template('res.html', num1=num1, num2=num2, operation_symbol=operation, result=result, email=email)


if __name__ == '__main__':
    app.run(debug=True)
