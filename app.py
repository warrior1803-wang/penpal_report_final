from flask import Flask, render_template, jsonify, request
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    # infos = []
    gender = []
    gender_num = []
    con = sqlite3.connect("user_info.db")
    cur = con.cursor()
    # sql = "select * from data_one limit 0, 10"
    # data = cur.execute(sql) 
    # for item in data:
    #     infos.append(item)
    sql = "SELECT gender,count(gender) from data_one group by gender  "
    data1 = cur.execute(sql)
    print(data1)
    for i in data1:
        gender.append(i[0])
        gender_num.append(i[1])

    cur.close()
    con.close()
    return render_template("index.html", gender=gender, gender_num=gender_num)


if __name__ == '__main__':
    app.run(debug=True)
