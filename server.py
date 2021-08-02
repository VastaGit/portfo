from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template('index.html')

@app.route("/<string:page_name>")
def every_page(page_name):
    return render_template(page_name)

def data_saving(data):
    with open ('database.txt','a') as database:
        email = data['email']
        subject = data['subject']
        message  = data['message']
        file = database.write(f"\n{email}  {subject}  {message}")

def csv_data_saving(data):
    with open ('database.csv','a', newline="") as database2:
        email = data['email']
        subject = data['subject']
        message  = data['message']
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            csv_data_saving(data)
            return redirect('thankyou.html')
        except:
            return "could not save any data"
    else:
        return 'you got error'

