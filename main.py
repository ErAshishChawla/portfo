from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def render_page(page_name='index.html'):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            data['datetime'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            write_to_csv(data)
            write_to_file(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong! please try again'


def write_to_file(data):
    with open(file='./database.txt', mode='ab') as database:
        database.write(str(data).encode('utf-8') + '\n'.encode('utf-8'))


@app.route('/submit_form', methods=['POST', 'GET'])
def write_to_csv(data):
    with open('database2.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='\'', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
