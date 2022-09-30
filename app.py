import sqlite3
from flask import Flask , request , url_for , redirect , render_template , flash 


con = sqlite3.connect("students.db")
cur = con.cursor()
cur.execute("create table if not exists std(id integer primary key autoincrement , name text , age text , city text)")
con.commit()
con.close()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add():
        return render_template("add.html")


@app.route("/view" , methods=['POST','GET'])
def view():
    try:
        if request.method == "POST":
            n = request.form.get("name")
            a = request.form.get("age")
            c = request.form.get("city")
            con = sqlite3.connect("students.db")
            cur = con.cursor()
            cur.execute("insert into std (name,age,city) values(?,?,?)",(n , a , c))
            con.commit()
            con.close()
            flash("added successfully")
            
          
    except:
        msg="something went wrong"          
    finally:
        con = sqlite3.connect("students.db")
        cur = con.cursor()
        cur.execute("select * from std")
        data = cur.fetchall()
        return render_template("view.html" , data = data)  

@app.route("/update/<string:id>" , methods=['POST','GET'])
def update(id):
    if  request.method == 'POST':
        n = request.form.get("name")
        a = request.form.get("age")
        c = request.form.get("city")
        con = sqlite3.connect("students.db")
        con.execute("update std set name=? , age=? , city=? where id= ?" , (n , a , c , id))
        con.commit()
        con.close()
        return redirect(url_for('view'))
    return render_template("update.html")

@app.route("/delete/<string:id>" , methods=['POST','GET'])
def delete(id):
    con = sqlite3.connect("students.db")
    con.execute("delete from std where id = ?",(id,))
    con.commit()
    con.close()
    return redirect(url_for('view'))

if __name__ == "__main__":
    app.run(debug=True)