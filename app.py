from flask import *
import sqlite3

app = Flask(__name__)
app.secret_key = "secret key"
ecom=sqlite3.connect("ecom.db")
@app.route("/")
def index():
    ecom=sqlite3.connect("ecom.db")
    cat1=ecom.execute("select * from category1;").fetchall()
    pro=ecom.execute("select * from products ").fetchall()
    return render_template("index.html",cat1=cat1,pro=pro)


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginde",methods=["POST"])
def loginde():
    email=request.form['email']
    password=request.form['pass']
    ecom=sqlite3.connect("ecom.db")
    cat1=ecom.execute("select count(*) from customers where customer_email=? and customer_pass=?",(email,password)).fetchone()
    print(cat1)
    if(cat1!=0):
        session["customer_email"]=email
        return redirect("/")
    else:
        return redirect("/login")


@app.route("/registerde",methods=["POST"])
def registerde():
    name=request.form['name']
    email=request.form['email']
    password=request.form['password']
    country=request.form['country']
    city=request.form['city']
    mobile=request.form['mobile']
    address=request.form['address']
    ecom=sqlite3.connect("ecom.db")
    cat1=ecom.execute("select count(*) from customers").fetchone()
    id=cat1[0]+1
    ecom.execute("insert into customers ( customer_id,customer_name,customer_email,customer_pass,customer_country,customer_city,customer_contact,customer_address) values (?,?,?,?,?,?,?,?)",(id,name,email,password,country,city,mobile,address));
    ecom.commit()
    cat1=ecom.execute("select * from customers").fetchall()
    print(cat1)
    ecom.close()

    return redirect("/")


@app.route('/logout')
def home():
    session.pop('customer_email', None)
    return render_template("index.html")
   
if __name__ == '__main__':
    app.run(debug=True)