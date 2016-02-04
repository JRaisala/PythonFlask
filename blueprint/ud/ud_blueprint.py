from flask import Blueprint,session,redirect,request,render_template,url_for,flash
from app.forms import FriendForm
from app import db
from app.db_models import Users,Friends
#Create blueprint
#First argument is the name of the blueprint folder
#second is always __name__ attribute
#thrid parameter tells what folder contans your templates
ud = Blueprint('ud',__name__,template_folder='templates',url_prefix=('/app/'))

#/app/delete
@ud.route('delete/<int:id>')
def delete(id):
	return "Delete"

@ud.route('update')
def update():
	return "Update"

@ud.route('friends',methods=['GET','POST'])
def friends():
	form = FriendForm()
	if request.method == 'GET':
		return render_template('template_friends.html',form=form,isLogged=True)
	else:
		if form.validate_on_submit():
			print('friends form submit ok')
			temp = Friends(form.name.data,form.address.data,form.age.data,session['user_id'])
			db.session.add(temp)
			db.session.commit()
			#tapa 2
			user = Users.query.get(session['user_id'])
			
			return render_template('template_user.html',isLogged=True,friends=user.friends)
		else:
			flash('Give proper values to all fields')
			return redirect(url_for('ud.friends'))

def before_request():
	if not 'isLogged' in session:
		return redirect('/')
	
ud.before_request(before_request)
