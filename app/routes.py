from flask import render_template
from app import app

projs = [
    {
        "id": "project1", "title": "Project 1",
        "description": "Description for project 1.",
        "image": "static/images/1.jpeg"},
    {
        "id": "project2", "title": "Project 2",
        "description": "Description for project 2.",
        "image": "static/images/2.jpeg"},
    {
        "id": "project3", "title": "Project 3",
        "description": "Description for project 3.",
        "image": "static/images/3.jpeg"},
]

@app.route('/')
@app.route('/home')
def home():
    last_projects = projs[-3:]
    return render_template('home.html', title='Home', projects=last_projects)

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
