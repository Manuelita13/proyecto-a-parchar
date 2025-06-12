import os
from flask import Flask, render_template, redirect, url_for
from ContactForm import ContactForm
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/guiaCallejera')
def guiaCallejera():
    return render_template('guiaCallejera.html')

@app.route('/lugaresTuristicos')
def lugaresTuristicos():
    return render_template('lugaresTuristicos.html')

@app.route('/Museos')
def museos():
    return render_template('Museos.html')

@app.route('/Restaurantes')
def restaurantes():
    return render_template('Restaurantes.html')


#Formulario de contacto
app.config['SECRET_KEY'] = 'gV4OyBbczY8dzMEIe1aRocr4vUvlF3gD28ku1oTDs7vriFPEsZfgbPPAKB2r02q8'

@app.route('/contact-form', methods = ['GET', 'POST'])
def contact_form():
    form = ContactForm()
    if form.validate_on_submit():
        with open('contact_form_data.csv', 'a', newline='') as f: 
            writer = csv.writer(f)
            writer.writerow([
                f' Nombre: {form.name.data}',
                f' Correo electrónico: {form.email.data}',
                f' Mensaje: {form.message.data}'
            ])
        return redirect(url_for('index')) 
    return render_template('contact-form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
