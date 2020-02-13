import json
from flask import Flask, request, jsonify
from flasgger import Swagger
from flasgger.utils import swag_from
from flasgger import LazyString, LazyJSONEncoder
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
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
    return "Views Detail"

@app.route("/Views", methods=["POST"])
@swag_from("swagger_config.yml")
def view():
    input_json = request.get_json()
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='blogging',
                                             user='root',
                                             password='')
        blog_info = "select * from blog_comment"
        cursor = connection.cursor()
        cursor.execute(blog_info)
        records = cursor.fetchall()
        # record = cursor.fetchone()
        # print(record[0])
        a = []
        b = []
        for row in records:
            a.append(row[0])
            b.append(row[1])

        connection.commit()
        # print('Sucess')
        cursor.close()
    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    res = {}
    res = {a[i]: b[i] for i in range(len(a))}
    print("Resultant dictionary is : " + str(res))
    return json.dumps(str(res))


if __name__ == "__main__":
    app.run(debug=True, port=8794)
