from flask import Flask, flash, redirect, url_for, render_template, session
from flask import request

from flask_sqlalchemy import SQLAlchemy

DB_HOST = "localhost"
DB_NAME = "sandwhich_makers"
DB_USERNAME = "root"
DB_Password = "Murloc2014!"

database_file = f"mysql+pymysql://{DB_USERNAME}:{DB_Password}@{DB_HOST}:3306/{DB_NAME}"

app = Flask(__name__)
app.secret_key = "mysecret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


class Resource(db.Model):
    __tablename__ = 'resources'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __init__(self, item, amount):
        self.item = item
        self.amount = amount

## just swap in sandwich model instead of resources
class Sandwiches(db.Model):
    __tablename__ = 'sandwiches'
    sandwich_size = db.Column(db.String(50), primary_key=True)
    price = db.Column(db.DECIMAL(5, 2), nullable=False)

    def __init__(self, sandwhich_size, price):
        self.sandwich_size = sandwhich_size
        self.price = price


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/resource")
def resource():
    return render_template("resources/list.html", resources=Resource.query.all())


@app.route('/addresource', methods=['GET', 'POST'])
def add_resource():
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            resource = Resource(request.form['item'], request.form['amount'])

            db.session.add(resource)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('resource'))
    return render_template('resources/add.html')


@app.route('/updateresource/<int:id>/', methods=['GET', 'POST'])
def update_resource(id):
    if request.method == 'POST':
        if not request.form['item'] or not request.form['amount']:
            flash('Please enter all the fields', 'error')
        else:
            resource = Resource.query.filter_by(id=id).first()
            resource.item = request.form['item']
            resource.amount = request.form['amount']
            db.session.commit()

            flash('Record was successfully updated')
            return redirect(url_for('resource'))
    data = Resource.query.filter_by(id=id).first()
    return render_template("resources/update.html", data=data)


@app.route('/deleteresource/<int:id>/', methods=['GET', 'POST'])
def delete_resource(id):
    if request.method == 'POST':
        resource = Resource.query.filter_by(id=id).first()
        db.session.delete(resource)
        db.session.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('resource'))
    data = Resource.query.filter_by(id=id).first()
    return render_template("resources/delete.html", data=data)


############# swap in values respective to the sandwich version of the implimentation
@app.route("/Sandwiches")
def sandwich():
    return render_template("sandwiches/list.html", sandwiches=Sandwiches.query.all())


@app.route('/add_sandwich', methods=['GET', 'POST'])
def add_sandwich():
    if request.method == 'POST':
        if not request.form['sandwich_size'] or not request.form['price']:
            flash('Please enter all the fields', 'error')
        else:
            sandwiches = Sandwiches(request.form['sandwich_size'], request.form['price'])
            db.session.add(Sandwiches)
            db.session.commit()

            flash('Record was successfully added')
            return redirect(url_for('sandwich'))
    return render_template('sandwiches/add.html')


@app.route('/update_sandwich/<int:id>/', methods=['GET', 'POST'])
def update_sandwich(sandwich_size):
    if request.method == 'POST':
        if not request.form['sandwich_size'] or not request.form['price']:
            flash('Please enter all the fields', 'error')
        else:
            sandwiches = Resource.query.filter_by(id=id).first()
            sandwiches.sandwich_size = request.form['sandwich_size']
            sandwiches.price = request.form['amount']
            db.session.commit()

            flash('Record was successfully updated')
            return redirect(url_for('sandwiches'))
    data = Sandwiches.query.filter_by(id=id).first()
    return render_template("sandwiches/update.html", data=data)


@app.route('/delete_sandwich/<int:id>/', methods=['GET', 'POST'])
def delete_sandwich(sandwich_size):
    if request.method == 'POST':
        sandwiches = Sandwiches.query.filter_by(id=id).first()
        db.session.delete(sandwiches)
        db.session.commit()

        flash('Record was successfully deleted')
        return redirect(url_for('sandwiches'))
    data = Resource.query.filter_by(id=id).first()
    return render_template("sandwiches/delete.html", data=data)


if __name__ == '__main__':
    app.run(port=3001, host="localhost", debug=True)
