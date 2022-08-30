import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(host='localhost', user='root', password='@615$011m9841k@')
cursor = db.cursor()


def create_database(cursor):
    try:
        cursor.execute('''
            CREATE DATABASE student_management DEFAULT CHARACTER SET 'utf8'
        ''')
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute(" USE student_management")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        db.database = 'student_management'
    else:
        print(err)
        exit(1)


