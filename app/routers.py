from app import app
#RENDER_TEMPLAte gives you access to Jinja2 template engine
from flask import render_template, request, make_response
from app.forms import loginForm

@app.route('/', method=['GET','POST'])
def index():
    login = loginForm()
    return render_template('template_index.html',form=login)


@app.route('/user/<name>')
def user(name):
    print(request.headers.get('User-Agent'))
    return render_template('template_user.html',name=name)

@app.route('/user',methods=['GET','POST'])
def userParams():
    name = request.args.get('name')
    return render_template('template_user.html', name=name)
   
