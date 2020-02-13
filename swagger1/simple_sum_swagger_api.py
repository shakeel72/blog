import json
from flask import Flask, request, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from
from flasgger import LazyString, LazyJSONEncoder
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


""""---------------------------------------Add Blog--------------------------------------------------------------------------------------------------"""

def add_blog(blog_id1, blog_name1, blog_description1, blog_comment1):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='blogging',
                                             user='root',
                                             password='')
        blog_info = """INSERT INTO blog_table(blog_id, blog_name, blog_description, blog_comment) VALUES (%s,%s,%s,%s)"""
        cursor = connection.cursor()
        info = (blog_id1, blog_name1, blog_description1, blog_comment1)
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
    add_blog = "Sucess"
    output["Sucess"] = add_blog
    return output

""""---------------------------------------------End Blog---------------------------------------------------"""







"""----------------------------------------------Start Delete Blog-------------------------------------------"""
def del_blog(blog_id2):
    output = {"Null"}
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='blogging',
                                             user='root',
                                             password='')
        blog_info = """DELETE FROM blog_table where blog_id =%s"""
        cursor = connection.cursor()
        info = (blog_id2)
        cursor.execute(blog_info, (info,))
        connection.commit()
        print('Sucess')
        cursor.close()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
    output = {"Null"}
    del_blog = "Sucess1"
    output["Sucess1"] = del_blog
    return output
"""-------------------------------------------------End Delete----------------------------------------------------------"""

"""-------------------------------------------------Start Update Blog------------------------------------------------------"""
def update_blog(blog_description3, blog_comment3, blog_id3):
    output={"Null"}
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='blogging',
                                             user='root',
                                             password='')
        blog_info = """Update blog_table set blog_description = %s, blog_comment = %s where blog_id = %s"""
        cursor = connection.cursor()
        info = (blog_description3, blog_comment3, blog_id3)
        cursor.execute(blog_info, info)
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
    output = {"Null"}
    update_blog = "Sucess"
    output["Sucess"] = update_blog
    return output
"""------------------------------------------------End update--------------------------------------------------------"""

"""=-----------------------------------------------Start Login--------------------------------------------------------"""
def login_blog(blog_name4,blog_id4):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='blogging',
                                             user='root',
                                             password='')
        blog_info = "select blog_id from blog_table where blog_name =%s"
        cursor = connection.cursor()
        info = (blog_name4)
        cursor.execute(blog_info, (info,))
        record = cursor.fetchone()
        print(record[0])
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
    if(record[0]==blog_id4):

        output = ("Your Status Login")
        return output
    else:
        output=("NOT")
        return output


"""---------------------------------------------------------End Login-------------------------------------------------------"""

"""---------------------------------------------------------JSON------------------------------------------------------------"""

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
    return "Blogging page please entered in url /swagger"

@app.route("/Add Blog", methods=["POST"])
@swag_from("swagger_config.yml")
def add_blogi():
    input_json = request.get_json()
    try:
        blog_id1 = input_json["b1"]
        blog_name1 = input_json["b2"]
        blog_description1 = input_json["b3"]
        blog_comment1 =input_json["b4"]
        res = add_blog(blog_id1, blog_name1, blog_description1, blog_comment1)
    except:
        res = {"success": False, "message": "Unknown error"}

    return json.dumps(res)



@app.route("/Delete Blog", methods=["DELETE"])
@swag_from("swagger_config.yml")
def del_blogi():
    input_json = request.get_json()
    try:
        blog_id2 = input_json["d1"]
        res = del_blog(blog_id2)
    except:
        res = {"success": False, "message": "Unknown error"}
    return json.dumps(res)

@app.route("/Update Employee", methods=["PUT"])
@swag_from("swagger_config.yml")
def update_blogi():
    input_json = request.get_json()
    try:

        blog_description3 = input_json["u1"]
        blog_comment3 = input_json["u2"]
        blog_id3 = input_json["u3"]
        res = update_blog(blog_description3,blog_comment3,blog_id3)
    except:
        res = {"success": False, "message": "Unknown error"}
    return json.dumps(res)

@app.route("/Login Into Blog", methods=["GET"])
@swag_from("swagger_config.yml")
def login_blogi():
    input_json = request.get_json()
    try:
        blog_name4 = str(input_json["username1"])
        blog_id4 = str(input_json["password1"])
        res = login_blog(blog_name4,blog_id4)
    except:
        res = {"success": True, "message": "Unknown error"}
    return json.dumps(res)


if __name__ == "__main__":
    app.run(debug=True, port=8791)
