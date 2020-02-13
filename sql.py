import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# try:
#     name = "Amrtya"
#     id="am123"
#     mail="abc@gm.com"
#     number="9166121"
#     password="Amri@hu"
#     connection = mysql.connector.connect(host='localhost',
#                                          database='employee',
#                                          user='root',
#                                          password='')
#     employee_info = """INSERT INTO emp_table(emp_name, emp_id, emp_mail, emp_number, password) VALUES (%s,%s,%s,%s,%s)"""
#     cursor = connection.cursor()
#     vari =(name,id,mail,number,password)
#     cursor.execute(employee_info, vari)
#     connection.commit()
#     print(cursor.rowcount,'Sucess')
#     cursor.close()
#     # if connection.is_connected():
#     #     db_Info = connection.get_server_info()
#     #     print("Connected to MySQL Server version ", db_Info)
#     #     cursor = connection.cursor()
#     #     cursor.execute("select database();")
#     #     record = cursor.fetchone()
#     #     print("You're connected to database: ", record)
#
# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")





# try:
#     name = "Amrtya"
#     id="am123"
#     mail="abc@gm.com"
#     number="9166121"
#     password="Amri@hu"
#     connection = mysql.connector.connect(host='localhost',
#                                          database='employee',
#                                          user='root',
#                                          password='')
#     employee_info = """DELETE FROM emp_table where emp_id =%s"""
#     cursor = connection.cursor()
#     vari =(id)
#     cursor.execute(employee_info, (vari,))
#     connection.commit()
#     print('Sucess')
#     cursor.close()
#     # if connection.is_connected():
#     #     db_Info = connection.get_server_info()
#     #     print("Connected to MySQL Server version ", db_Info)
#     #     cursor = connection.cursor()
#     #     cursor.execute("select database();")
#     #     record = cursor.fetchone()
#     #     print("You're connected to database: ", record)
#
# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")





# try:
#     name = "Amrtya"
#     id="shaku72"
#     mail="abc@gm.com"
#     number="916611"
#     password="Amri@hui"
#     connection = mysql.connector.connect(host='localhost',
#                                          database='employee',
#                                          user='root',
#                                          password='')
#     employee_info = """Update emp_table set emp_number = %s, password = %s where emp_id = %s"""
#     cursor = connection.cursor()
#     vari =(number,password,id)
#     cursor.execute(employee_info, vari)
#     connection.commit()
#     print('Sucess')
#     cursor.close()
# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")




# try:
#     name = "Amrtya"
#     id="shaku72"
#     mail="abc@gm.com"
#     number="916611"
#     password="Amri@hui"
#     connection = mysql.connector.connect(host='localhost',
#                                          database='employee',
#                                          user='root',
#                                          password='')
#     employee_info = "select password from emp_table where emp_id =%s"
#     cursor = connection.cursor()
#     vari =(id)
#     cursor.execute(employee_info, (vari,))
#     record = cursor.fetchone()
#     print(record[0])
#     connection.commit()
#     print('Sucess')
#     cursor.close()
# except Error as e:
#     print("Error while connecting to MySQL", e)
# finally:
#     if (connection.is_connected()):
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")
# print(record[0])



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
    a=[]
    b=[]
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
print ("Resultant dictionary is : " +  str(res))

