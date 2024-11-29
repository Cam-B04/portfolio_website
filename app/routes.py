from flask import render_template
from app import app

projs = [
    {
        "id": "project1",
        "title": "Producing realistic climate data using generative AI.",
        "description": "Paper produced during my PhD, the goal was "
        "to produce realistic climate data using generative AI. The paper "
        "was published in the Nonlinear Processes in Geophysics journal and underlined "
        "interesting properties for to help reduce instabilities in Meteorological "
        "simulators.",
        "image": "static/images/img_project_GAN_climat.jpeg",
        "link": "https://github.com/Cam-B04/Producing-realistic-climate-data-with-GANs",
        },
    {
        "id": "project2",
        "title": "Data visualisation of Bixi bike stations in Montreal.",
        "description": "This project aims at visualising the Bixi bike stations in Montreal.",
        "image": "static/images/img_project_bixi.png",
        "link": "https://github.com/Cam-B04/bixi_open_data",
        },
]


@app.route('/')
@app.route('/home')
def home():
    last_projects = projs[-3:]
    return render_template('home.html', title='Home', projects=last_projects)


@app.route('/projects')
def projects():
    return render_template('projects.html', title='Projects', projects=projs)


@app.route('/others')
def others():
    return render_template('others.html', title='Others')
