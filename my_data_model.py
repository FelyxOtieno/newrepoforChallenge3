from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////app/shplist.db'
db = SQLAlchemy(app)



class MemberUser(db.Model):
    member_id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(255))
    member_email = db.Column(db.String(255))
    member_password = db.Column(db.String(255))
    member_shopping_list_id = db.Column(db.String(255))
    shopping_lists = db.relationship('ShoppingListsTable',
        backref=db.backref('s_lists', lazy='dynamic'))





    timestamp = db.Coloumn(db.DateTime)

    def __init__(self,
				 member_id, 
				 member_name, 
				 member_email, 
				 member_password, 
				 member_shopping_list_id,
				 timestamp
    			)
    
    	self.member_id = member_id
    	self.member_name = member_name
    	self.member_email = member_email
    	self.member_password = member_password
    	self.member_shopping_list_id = member_shopping_list_id
    	self.timestamp = datetime.utcnow()

	def __repr__(self):
		return self.member_name


class ShoppingListsTable(db.Model):
	shopping_list_name = db.Column(db.String(255))
	shopping_list_category = db.Column(db.String(255))
	shopping_list_items = db.Column(db.String(255))

	def __init__(self,
				 shopping_list_name, 
				 shopping_list_category,
				 shopping_list_items 
				 
    			)

    	self.shopping_list_name = shopping_list_name
    	self.shopping_list_category = shopping_list_category
    	self.shopping_list_items = shopping_list_items

    def __str__(self):
        return self.shopping_list_name


class SingleShoppingList(db.Model):
	shopping_list_id = db.Column(db.String(255))
	shopping_list_items = db.Column(db.String(255))

	def __init__(self,
				 shopping_list_id, 
				 shopping_list_items,
				 
    			)
		self.shopping_list_id = shopping_list_id
		self.shopping_list_items = shopping_list_items

		def __str__(self):
        return self.shopping_list_id


class ShoppingListItems(db.Model):
	item_name = db.Column(db.String(255))
	

	def __init__(self,
				 item_name, 
    			)
		self.item_name = item_name
		
		def __str__(self):
        return self.item_name

