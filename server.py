from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file=database.write(f'\n{name},{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file=csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([name,email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    error = None
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            print(data)
            write_to_csv(data)
            return render_template('thankyou.html')
        except:
            return "Error, Please try again after some time."