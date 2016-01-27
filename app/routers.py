from app import app
#RENDER_TEMPLAte gives you access to Jinja2 template engine
from flask import render_template, request

@app.route('/')
def index():
    name = 'Markus'
    address='Rautatienkatu'
    return render_template('template_index.html', title=address, name=name)


@app.route('/user/<name>')
def user(name):
    print(request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

@app.route('/user',method=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html', name=name)
  