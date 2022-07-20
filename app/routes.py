from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return  render_template('index.html', title='home')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', title="About me")

@app.route('/certificates')
def skills():
    return render_template('certificates.html', title="Skills")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")