import math

import requests as requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index')
def index_page():
    return render_template('index.html')


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


#######

def is_prime_check(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


@app.route('/even_odd_prime', methods=['GET', 'POST'])
def even_odd_prime():
    return render_template('even_odd_prime.html')


@app.route('/even_odd_prime_results', methods=['GET', 'POST'])
def even_odd_prime_results():
    if request.method == 'POST':
        start = int(request.form['start'])
        end = int(request.form['end'])
        even = []
        odd = []
        prime = []
        for num in range(start, end + 1):
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
            if is_prime(num):
                prime.append(num)
        return render_template('even_odd_prime_results.html', even=even, odd=odd, prime=prime)
    else:
        return render_template('index.html')


@app.route('/prime', methods=['GET', 'POST'])
def prime():
    return render_template('prime.html')


@app.route('/find_prime_or_not', methods=['POST'])
def check_prime():
    num = int(request.form['num'])
    prime = is_prime(num)
    return render_template('prime.html', num=num, prime=prime)


@app.route('/prime_range', methods=['GET', 'POST'])
def prime_range():
    return render_template('prime_numers_range.html')


@app.route('/prime_numers_range', methods=['GET', 'POST'])
def prime_numers_range():
    if request.method == 'POST':
        start = int(request.form['start'])
        end = int(request.form['end'])
        primes = [n for n in range(start, end + 1) if is_prime(n)]
        return render_template('primes.html', primes=primes)
    else:
        return render_template('prime_numers_range.html')


@app.route('/even', methods=['GET', 'POST'])
def even():
    return render_template('even.html')


@app.route('/find_even_or_not', methods=['POST'])
def find_even_or_not():
    number = int(request.form['number'])
    if number % 2 == 0:
        result = f"{number} is divisible by 2"
    else:
        result = f"{number} is not divisible by 2"
    return render_template('even.html', result=result)


@app.route('/even_range', methods=['GET', 'POST'])
def even_range():
    return render_template('even_numers_range.html')


@app.route('/even_numers_range', methods=['GET', 'POST'])
def even_numers_range():
    if request.method == 'POST':
        # Get the user's input for the range of numbers
        start = int(request.form['start'])
        end = int(request.form['end'])

        # Create a list of numbers in the range
        numbers = list(range(start, end + 1))

        # Create a list of whether each number is divisible by 2 or not
        divisibility = ['even' if num % 2 == 0 else 'odd' for num in numbers]

        # Render the template with the results
        return render_template('evens.html', numbers=numbers, divisibility=divisibility)

    # If it's a GET request, just render the index page
    return render_template('index.html')


@app.route('/number_checker', methods=['GET', 'POST'])
def number_checker():
    return render_template('number_checker.html')


@app.route('/check_what_number_it_is', methods=['GET', 'POST'])
def check_what_number_it_is():
    result = ''
    if request.method == 'POST':
        number = int(request.form['number'])
        if number % 2 == 0:
            result = 'Even'
        else:
            result = 'Odd'
        if is_prime(number):
            result += ', Prime'
    return render_template('number_checker.html', result=result)


@app.route('/mobile', methods=['GET', 'POST'])
def mobile():
    return render_template('mobile_form.html')


@app.route('/check_mobile', methods=['POST'])
def check_mobile():
    mobile_number = request.form['mobile_number']
    api_key = 'IAnYotMPDj7XWbo9CUR9glnhiNQE471W'
    url = f'https://apilayer.net/api/validate?access_key={api_key}&number={mobile_number}&country_code=&format=1'
    response = requests.get(url)
    data = response.json()
    if data['valid'] and data['line_type'] == 'mobile':
        return f'{mobile_number} is an active mobile number.'
    else:
        return f'{mobile_number} is not a valid or active mobile number.'


@app.route('/check_mobile_number', methods=['GET', 'POST'])
def check_mobile_number():
    return render_template('check_mobile_number.html')


@app.route('/find_number', methods=['GET', 'POST'])
def nnn():
    if request.method == 'POST':
        mobile_number = request.form['mobile_number']
        api_key = 'IAnYotMPDj7XWbo9CUR9glnhiNQE471W'  # replace with your Numverify API key
        url = f'http://apilayer.net/api/validate?access_key={api_key}&number={mobile_number}&country_code=IN'
        response = requests.get(url)
        data = response.json()

        if data['valid'] and data['line_type'] == 'mobile':
            status = 'Active'
        else:
            status = 'Inactive'

        isp = data['carrier']
        location = data['location']

        return render_template('find_number_result.html', mobile_number=mobile_number, status=status, isp=isp,
                               location=location)

    return render_template('index.html')


@app.route('/discount_form', methods=['GET', 'POST'])
def discount_form():
    return render_template('discount_form.html')


@app.route('/calculate_discount', methods=['GET', 'POST'])
def calculate_discount():
    if request.method == 'POST':
        price = float(request.form['price'])
        discount = float(request.form['discount'])
        discounted_price = price * (1 - discount / 100)
        return render_template('discount_results.html', discounted_price=discounted_price)
    else:
        return render_template('discount_form.html')


@app.route('/commission_form', methods=['GET', 'POST'])
def commission_form():
    return render_template('commission_form.html')


@app.route('/calculate_commission', methods=['POST'])
def calculate_commission():
    if request.method == 'POST':
        price = float(request.form['price'])
        commission = float(request.form['commission'])
        total_commission = price * commission / 100
        # return f"Commission: {commission}"
        return render_template('commission_results.html', price=price, commission=commission,
                               total_commission=total_commission)
    else:
        return render_template('commission_form.html')


@app.route('/interest_form', methods=['GET', 'POST'])
def interest_form():
    return render_template('interest_form.html')


@app.route('/calculate_interest', methods=['POST'])
def calculate_interest():
    price = float(request.form['price'])
    interest_rate = float(request.form['interest_rate'])
    tenure = int(request.form['tenure'])

    interest = (price * interest_rate * tenure) / 100

    monthly_interest_rate = interest_rate / (12 * 100)
    months = tenure * 12
    monthly_payment = (price * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** (-months))

    Total_Payable = price + interest

    return render_template('interest_form.html', interest=interest, monthly_payment=monthly_payment, price=price, interest_rate=interest_rate, tenure=tenure, totalpay=Total_Payable )


if __name__ == '__main__':
    app.run(debug=True)
