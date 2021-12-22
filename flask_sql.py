from flask import Flask
from flask import render_template
from flask import redirect, render_template, request
import psycopg2
app = Flask(__name__)

connection = psycopg2.connect(user='postgres', password='1488', host='localhost', database='web')
cursor = connection.cursor()
sql_select = "SELECT * FROM list_people" # покажет весь список
cursor.execute(sql_select)



users = []
for line in cursor.fetchall():
    user_dict = {'username': line[0],
                 'name': line[1],
                 'surname': line[2],
                 'age': line[3]}
    users.append(user_dict)


@app.route('/')
def index():
    return redirect("http://127.0.0.1:5000/users")


@app.route('/users')
def name_users():
    return render_template('Users_list.html', users = users)


@app.route('/users/insert/', methods=['get', 'post'])
def users_insert():
    connection = psycopg2.connect(user='postgres', password='1488', host='localhost', database='web')
    cursor = connection.cursor()
    if request.method == 'POST':
        username = request.form.get('username')
        name = request.form.get('name')
        surname = request.form.get('surname')
        age = request.form.get('age')

        user_info = {
            'username': username,
            'name': name,
            'surname': surname,
            'age': age
        }

        sql_insert = [f"INSERT INTO list_people VALUES ('{user_info[0]['username']}', '{user_info[1]['name']}', '{user_info[2]['surname']}', '{user_info[3]['age']}');"]
        sql_select = "SELECT * FROM list_people"  # покажет весь список

        with connection.cursor() as cursor:
            cursor.execute(sql_insert)
            connection.commit()


    return render_template("sql_insert.html")







if __name__ == '__main__':
    app.run(debug=True)



