from crypt import methods
from click import password_option
from market import app
from flask import render_template, redirect, url_for, flash   
from market.models import item,User
from market.forms import RegisterForm
from market import db

@app.route('/')              #decorator
@app.route('/home')
def Home_Page():
    return render_template('home.html')

@app.route('/market') 
def Market_Page():
    items = item.query.all() 
      # items that i saved in the database from the python3 shell (terminal) 

# render templates to return the html doc
    return render_template('market.html',items=items)   #items in database should be rendered in the market page



@app.route('/register', methods = ['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(
                            Username = form.username.data,
                            Email_address = form.email_address.data,
                            Password_hash = form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('Market_Page'))

    if form.errors != {}:  #if there are not errors from the validation
        for err_msg in form.errors.values():
            flash(f'there was an error creating a user: {err_msg}', category= 'danger')

    return render_template('register.html',form = form)




# if __name__ =="__main__":
#     app.run(debug=True)