from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)        #app instancne
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'    #uniform resource identifier..a file that will be identified as db
app.config['SECRET_KEY'] = '2d25a401fb7c6446df91a69f'
db = SQLAlchemy(app)         #database instance  


from market import routes