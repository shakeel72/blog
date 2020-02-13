import json
from flask import Flask, request, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from
from flasgger import LazyString, LazyJSONEncoder
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

def add_comments(blog_id1, comments1):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='blogging',
                                             user='root',
                                             password='')
        blog_info = """INSERT INTO blog_comment(blog_id, comments,approved_reject) VALUES (%s,%s,'')"""
        cursor = connection.cursor()
        info = (blog_id1, comments1)
        cursor.execute(blog_info, info)
        connection.commit()
        print(cursor.rowcount, 'Sucess')
        cursor.close()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    output = {"Null"}
    add_items = "Sucess"
    output["Sucess"] = add_items
    return output


def approved_reject(blog_id2,approved_reject2):
    output={"Null"}
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='blogging',
                                             user='root',
                                             password='')
        blog_info = """Update blog_comment set approved_reject = %s where blog_id = %s"""
        cursor = connection.cursor()
        info =(approved_reject2,blog_id2)
        cursor.execute(blog_info,info)
        connection.commit()
        print('Sucess')
        cursor.close()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    update = "Sucess Entered"
    output["Sucess"] = update
    return output


#
#
# def views(emp_id):
#     a=emp_id
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='employee',
#                                              user='root',
#                                              password='')
#         employee_info = "select * from elect_items"
#         cursor = connection.cursor()
#         cursor.execute(employee_info)
#         records = cursor.fetchall()
#         # record = cursor.fetchone()
#         # print(record[0])
#         a = []
#         b = []
#         for row in records:
#             a.append(row[1])
#             b.append(row[2])
#
#         connection.commit()
#         # print('Sucess')
#         cursor.close()
#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if (connection.is_connected()):
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")
#     res = {}
#     res = {a[i]: b[i] for i in range(len(a))}
#     print("Resultant dictionary is : " + str(res))
#     return res



app = Flask(__name__)
app.config["SWAGGER"] = {"title": "Swagger-UI", "uiversion": 2}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": "apispec_1",
            "route": "/apispec_1.json",
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    # "static_folder": "static",  # must be set by user
    "swagger_ui": True,
    "specs_route": "/swagger/",
}

template = dict(
    swaggerUiPrefix=LazyString(lambda: request.environ.get("HTTP_X_SCRIPT_NAME", ""))
)

app.json_encoder = LazyJSONEncoder
swagger = Swagger(app, config=swagger_config, template=template)


@app.route("/")
def index():
    return "Add Comments to go /swagger"

@app.route("/Add Comments", methods=["POST"])
@swag_from("swagger_config.yml")
def add_commi():
    input_json = request.get_json()
    try:
        blog_id1 = str(input_json["c1"])
        comments1 = str(input_json["c2"])
        res = add_comments(blog_id1,comments1)
    except:
        res = {"success": False, "message": "Unknown error"}
        return json.dumps(res)

@app.route("/Approved/Reject_comments", methods=["PUT"])
@swag_from("swagger_config.yml")
def appi_rejji():
    input_json = request.get_json()
    try:
        blog_id2= input_json["ar1"]
        approved_reject2 = input_json["ar2"]
        res = approved_reject(blog_id2,approved_reject2)
    except:
        res = {"success": False, "message": "Unknown error"}
    return json.dumps(res)


# @app.route("/Views", methods=["GET"])
# @swag_from("swagger_config.yml")
# def view():
#     input_json = request.get_json()
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                                              database='blogging',
#                                              user='root',
#                                              password='')
#         blog_info = "select * from blog_comment"
#         cursor = connection.cursor()
#         cursor.execute(blog_info)
#         records = cursor.fetchall()
#         # record = cursor.fetchone()
#         # print(record[0])
#         a = []
#         b = []
#         for row in records:
#             a.append(row[0])
#             b.append(row[1])
#
#         connection.commit()
#         # print('Sucess')
#         cursor.close()
#     except Error as e:
#         print("Error while connecting to MySQL", e)
#     finally:
#         if (connection.is_connected()):
#             cursor.close()
#             connection.close()
#             print("MySQL connection is closed")
#     res = {}
#     res = {a[i]: b[i] for i in range(len(a))}
#     print("Resultant dictionary is : " + str(res))


if __name__ == "__main__":
    app.run(debug=True, port=8792)
