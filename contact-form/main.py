from flask import Flask, render_template, redirect, url_for
from ContactForm import ContactForm
import csv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gV4OyBbczY8dzMEIe1aRocr4vUvlF3gD28ku1oTDs7vriFPEsZfgbPPAKB2r02q8'

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        with open('contact_form_data.csv', 'a', newline='') as f: 
            writer = csv.writer(f)
            writer.writerow([form.name.data, form.email.data, form.message.data])
    # Redirect after submit to index.html that is located in the outside folder out of the contact-form folder on templates folder
    return redirect(url_for('../templates/index.html'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)