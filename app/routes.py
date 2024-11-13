from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/description')
def description():
    return render_template('description.html', title='Description')

@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects')

@app.route('/others')
def others():
    return render_template('others.html', title='Others')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

