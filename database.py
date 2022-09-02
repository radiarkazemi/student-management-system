import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'student_management'

TABLES = {}
TABLES['student'] = (
    "CREATE TABLE `student` ("
    "  `id` int(15) NOT NULL AUTO_INCREMENT,"
    "  `national_id` varchar(15) NOT NULL,"
    "  `firstname` varchar(45) NOT NULL,"
    "  `lastname` varchar(45) NOT NULL,"
    "  `gender` varchar(10) NOT NULL,"
    "  `birth_day` varchar(15) NOT NULL,"
    "  `mobile` varchar(20) NOT NULL,"
    "  `grade` varchar(5) NOT NULL,"
    "  `email` varchar(45),"
    "  `address` varchar(90),"
    "   `photo` LONGBLOB NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['marks'] = (
    "CREATE TABLE `marks` ("
    "   `id` int(15) NOT NULL AUTO_INCREMENT,"
    "   `national_id` varchar(15) NOT NULL,"
    "   `exam_name` varchar(30) NOT NULL,"
    "   `language` varchar(5) NOT NULL,"
    "   `biology` varchar(5) NOT NULL,"
    "   `math` varchar(5) NOT NULL,"
    "   `chemistry` varchar(5) NOT NULL,"
    "   `physics` varchar(5) NOT NULL,"
    "   `sport` varchar(5) NOT NULL,"
    "   PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['attendance'] = (
    "CREATE TABLE `attendance` ("
    "   `id` int(15) NOT NULL AUTO_INCREMENT,"
    "   `national_id` int(15) NOT NULL,"
    "   `date` date NOT NULL,"
    "   `morning` varchar(20) NOT NULL,"
    "   `evening` varchar(20) NOT NULL,"
    "   PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['user'] = (
    "CREATE TABLE `user` ("
    "   `id` int(15) NOT NULL AUTO_INCREMENT,"
    "   `fullname` varchar(80) NOT NULL,"
    "   `username` varchar(45) NOT NULL,"
    "   `password` varchar(45) NOT NULL,"
    "   PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

db = mysql.connector.connect(host='localhost', user='root', password='@615$011m9841k@')
cursor = db.cursor()


def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


try:
    cursor.execute(" USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        db.database = DB_NAME
    else:
        print(err)
        exit(1)

for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}:".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists!")
        else:
            print(err.msg)
    else:
        print("Ok")

cursor.close()
db.close()
