# Made with love by Alvison Hunter Arnuero - September 12th, 2020
from flask import Flask, flash, redirect, render_template, request, url_for
import sqlite3 as sql
import secrets

app = Flask(__name__, static_url_path='/static', template_folder="templates")
DEVELOPMENT_ENV = True
app.config['SESSION_COOKIE_SECURE'] = False

app_data = {
    "name":         "Das Zeugnisblatt",
    "description":  "A basic CRUD Flask app using bootstrap for layout & SQL Lite as DB",
    "author":       "Alvison Hunter Arnuero",
    "html_title":   "Das Zeugnisblatt",
    "project_name": "Das Zeugnisblatt",
    "keywords":     "flask, webapp, bootstrap, basic, python, crud, crud app, sqlLite, sql"
}
secret = secrets.token_urlsafe(32)
app.secret_key = secret

students_fields = ["ID", "FIRST_NAME", "LAST_NAME", "FATHER_NAME", "MOTHER_NAME",
                   "PHONE", "AGE", "GPA", "CURRENT_ADDRESS", "CITY", "PIN", "TEACHER_ID"]

# Defining the regular routes on this section


@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html', students_fields=students_fields)


@app.route('/edit/<id>', methods=['POST'])
def edit_student(id):
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute('SELECT * FROM students WHERE ID= ?', [id])
    rows = cur.fetchall()
    qry_data = [item for t in rows for item in t]
    zip_iterator = zip(students_fields, qry_data)
    tmp_dict = dict(zip_iterator)
    del tmp_dict['ID']
    selected_student = tmp_dict
    return render_template('edit_student.html', ID=id, selected_student=selected_student)


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            msg = ''
            FIRST_NAME = request.form['FIRST_NAME']
            LAST_NAME = request.form['LAST_NAME']
            FATHER_NAME = request.form['FATHER_NAME']
            MOTHER_NAME = request.form['MOTHER_NAME']
            PHONE = request.form['PHONE']
            AGE = request.form['AGE']
            GPA = request.form['GPA']
            CURRENT_ADDRESS = request.form['CURRENT_ADDRESS']
            CITY = request.form['CITY']
            PIN = request.form['PIN']
            TEACHER_ID = request.form['TEACHER_ID']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (FIRST_NAME,LAST_NAME,FATHER_NAME,MOTHER_NAME,PHONE,AGE,GPA,CURRENT_ADDRESS,CITY,PIN,TEACHER_ID) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                            (FIRST_NAME, LAST_NAME, FATHER_NAME, MOTHER_NAME, PHONE, AGE, GPA, CURRENT_ADDRESS, CITY, PIN, TEACHER_ID))
                con.commit()
                msg = FIRST_NAME + ' was successfully added to our records.'
                alertType = "align-middle alert alert-primary"
                flash(msg, alertType)

        except:
            con.rollback()
            msg = "An Unexpected error occurred while saving this new profile."
            alertType = "align-middle alert alert-danger"
        finally:
            return redirect(url_for('list'))
            # return render_template("result.html",msg = msg, alertType = alertType)
        con.close()


@app.route('/updaterec', methods=['POST', 'GET'])
def updaterec():
    if request.method == 'POST':
        try:
            alertType = ""
            msg = ''

            FIRST_NAME = request.form['FIRST_NAME']
            LAST_NAME = request.form['LAST_NAME']
            FATHER_NAME = request.form['FATHER_NAME']
            MOTHER_NAME = request.form['MOTHER_NAME']
            PHONE = request.form['PHONE']
            AGE = request.form['AGE']
            GPA = request.form['GPA']
            CURRENT_ADDRESS = request.form['CURRENT_ADDRESS']
            CITY = request.form['CITY']
            PIN = request.form['PIN']
            TEACHER_ID = request.form['TEACHER_ID']
            STUDENT_ID = request.form['ID']

            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute(''' UPDATE students SET FIRST_NAME=?, LAST_NAME=?, FATHER_NAME=?, MOTHER_NAME=?, PHONE=?, AGE=?, GPA=?,CURRENT_ADDRESS=?,CITY=?,PIN=?,TEACHER_ID=? WHERE ID=? ''',
                            (FIRST_NAME, LAST_NAME, FATHER_NAME, MOTHER_NAME, PHONE, AGE, GPA, CURRENT_ADDRESS, CITY, PIN, TEACHER_ID, STUDENT_ID))
                con.commit()
                msg = str(FIRST_NAME) + \
                    ' was successfully updated to our records.'
                alertType = "align-middle alert alert-primary"
                flash(msg, alertType)

        except:
            con.rollback()
            msg = "An Unexpected error occurred while updating this profile."
            alertType = "align-middle alert alert-danger"

        finally:
            return redirect(url_for('list'))
            # return render_template("result.html",msg = msg, alertType = alertType)
        con.close()


@app.route('/delete/<id>', methods=['POST'])
def delRecord(id):
    if request.method == 'POST':
        try:
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute('DELETE FROM students WHERE ID = ?', [id])
                con.commit()
                msg = 'This Profile was successfully deleted from Our records.'
                alertType = "align-middle alert alert-primary"

        except:
            con.rollback()
            msg = "An Unexpected error occurred while deleting this profile."
            alertType = "align-middle alert alert-danger"

        finally:
            flash(msg, alertType)
            return redirect(url_for('list'))
            # return render_template("result.html",msg = msg, alertType = alertType)
        con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    return render_template("list.html", rows=rows)


@app.route('/staff')
def view_staff():
    return render_template('staff.html')

# Let's try to capture the 404 error and handle it


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', page="404"), 404


if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)
