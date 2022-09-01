from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector
import functools

from PyQt5.uic import loadUiType
import database as database_db

ui, _ = loadUiType('student.ui')


class MainApp(QMainWindow, ui):
    file_path = ''
    file_path_edit = ''

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.create_database()
        self.handle_ui_changes()
        self.handle_button()
        self.show_all_students()

    def handle_ui_changes(self):
        self.main_tabWidget.tabBar().setVisible(False)

    def handle_button(self):
        self.studen_pushButton.clicked.connect(self.open_student_tab)
        self.marks_pushButton.clicked.connect(self.open_marks_tab)
        self.attendance_pushButton.clicked.connect(self.open_attendance_tab)
        self.report_pushButton.clicked.connect(self.open_report_tab)
        self.user_pushButton.clicked.connect(self.open_user_tab)

        self.add_user_pushButton.clicked.connect(self.add_user)
        self.login_user_pushButton.clicked.connect(self.login_check_user)
        self.edit_user_pushButton.clicked.connect(self.edit_user)
        self.delete_user_pushButton.clicked.connect(self.delete_user)

        self.image_browse_pushButton.clicked.connect(self.select_image)
        self.save_stu_pushButton.clicked.connect(self.add_new_student)
        self.search_pushButton.clicked.connect(self.search_stusent)
        self.image_browse_pushButton_edit.clicked.connect(self.select_image_edit)
        self.edit_stu_pushButton.clicked.connect(self.edit_student)
        self.delete_stu_pushButton.clicked.connect(self.delete_student)

    # =============================================open tab=============================================

    def open_student_tab(self):
        self.main_tabWidget.setCurrentIndex(0)

    def open_marks_tab(self):
        self.main_tabWidget.setCurrentIndex(1)

    def open_attendance_tab(self):
        self.main_tabWidget.setCurrentIndex(2)

    def open_report_tab(self):
        self.main_tabWidget.setCurrentIndex(3)

    def open_user_tab(self):
        self.main_tabWidget.setCurrentIndex(4)

    # ============================================= Database =============================================
    def create_database(self):
        database_db

    # ============================================= Student =============================================

    def show_all_students(self):
        pass

    def select_image(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open File', '~', 'PNG Files (*.png);;Jpg Files (*.jpg)')
        self.file_path = file_name
        pixmap = QPixmap(file_name[0])
        self.image_label.setPixmap(pixmap)

    def select_image_edit(self):
        file_name_edit = QFileDialog.getOpenFileName(self, 'Open File', '~', 'PNG Files (*.png);;Jpg Files (*.jpg)')
        self.file_path_edit = file_name_edit
        pixmap = QPixmap(file_name_edit[0])
        self.image_label_edit.setPixmap(pixmap)

    def __str__(self):
        return str(self.select_image())

    def add_new_student(self):
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                     database='student_management')
        cursor = db.cursor()

        image_path = self.file_path
        with open(image_path[0], 'rb') as File:
            photo_binary_data = File.read()

        national_id = self.national_id_lineEdit.text()
        firstname = self.firstname_lineEdit.text()
        lastname = self.lastname_lineEdit.text()
        gender = self.gender_comboBox.currentText()
        birthday = self.birthday_lineEdit.text()
        address = self.address_textEdit.toPlainText()
        mobile = self.mobile_lineEdit.text()
        grade = self.grade_comboBox.currentText()
        email = self.email_lineEdit.text()

        cursor.execute('''
            INSERT INTO student (national_id , firstname , lastname , gender , birth_day , mobile , grade , email , address , photo)
            VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s)
        ''', (national_id, firstname, lastname, gender, birthday, mobile, grade, email, address, photo_binary_data))
        db.commit()
        db.close()
        self.message_box('Student Added!')

    def search_stusent(self):
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                     database='student_management')
        cursor = db.cursor()

        student_national_id = self.national_id_lineEdit_search.text()

        sql = ''' SELECT * FROM student WHERE national_id = %s'''
        cursor.execute(sql, [(student_national_id)])
        data = cursor.fetchone()

        self.national_id_lineEdit_edit.setText(data[1])
        self.firstname_lineEdit_edit.setText(data[2])
        self.lastname_lineEdit_edit.setText(data[3])
        self.gender_comboBox_edit.setCurrentText(data[4])
        self.birthday_lineEdit_edit.setText(data[5])
        self.mobile_lineEdit_edit.setText(data[6])
        self.Grade_comboBox_edit.setCurrentText(data[7])
        self.email_lineEdit_edit.setText(data[8])
        self.address_textEdit_edit.setPlainText(data[9])
        photo = QPixmap()
        if photo.loadFromData(data[10]):
            self.image_label_edit.setPixmap(photo)

    def edit_student(self):
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                     database='student_management')
        cursor = db.cursor()

        original_national_id = self.national_id_lineEdit_search.text()
        national_id = self.national_id_lineEdit_edit.text()
        firstname = self.firstname_lineEdit_edit.text()
        lastname = self.lastname_lineEdit_edit.text()
        gender = self.gender_comboBox_edit.currentText()
        birthday = self.birthday_lineEdit_edit.text()
        mobile = self.mobile_lineEdit_edit.text()
        grade = self.Grade_comboBox_edit.currentText()
        email = self.email_lineEdit_edit.text()
        address = self.address_textEdit_edit.toPlainText()
        image_edit = self.file_path_edit
        with open(image_edit[0], 'rb') as File:
            photo_binary_data = File.read()

        cursor.execute('''
            UPDATE student SET national_id = %s , firstname = %s , lastname = %s , gender = %s , birth_day = %s ,
             mobile = %s , grade = %s , email = %s , address = %s , photo = %s WHERE national_id = %s
        ''', (national_id, firstname, lastname, gender, birthday, mobile, grade, email, address, photo_binary_data,
              original_national_id))
        db.commit()
        db.close()
        self.message_box('Student Information Updated!')

    def delete_student(self):
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                     database='student_management')
        cursor = db.cursor()

        original_national_id = self.national_id_lineEdit_search.text()

        warning = QMessageBox.warning(self, 'Delete Student', 'Are You Sure You Want to Delete This Student?',
                                      QMessageBox.Yes | QMessageBox.No)

        if warning == QMessageBox.Yes:
            sql = ''' DELETE FROM student WHERE national_id = %s'''
            cursor.execute(sql, [(original_national_id)])
            db.commit()
            db.close()
            self.message_box('Student Deleted!')

            self.national_id_lineEdit_search.setText('')
            self.national_id_lineEdit_edit.setText('')
            self.firstname_lineEdit_edit.setText('')
            self.lastname_lineEdit_edit.setText('')
            self.gender_comboBox_edit.setCurrentIndex(0)
            self.birthday_lineEdit_edit.setText('')
            self.mobile_lineEdit_edit.setText('')
            self.Grade_comboBox_edit.setCurrentIndex(0)
            self.email_lineEdit_edit.setText('')
            self.address_textEdit_edit.setPlainText('')
            pixmap = QPixmap('images/student.jpg')
            self.image_label_edit.setPixmap(pixmap)

    # ============================================= Marks =============================================
    def add_marks(self):
        pass

    def edit_marks(self):
        pass

    def delete_marks(self):
        pass

    # ============================================= Attendance =============================================
    def add_attendance(self):
        pass

    def edit_attendance(self):
        pass

    def delete_attendance(self):
        pass

    # ============================================= Reports =============================================
    def student_report(self):
        pass

    def marks_report(self):
        pass

    def attendance_report(self):
        pass

    # ============================================= Reports =============================================
    def add_user(self):
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                     database='student_management')
        cursor = db.cursor()
        full_name = self.user_fullname_lineEdit.text()
        username = self.username_lineEdit.text()
        password = self.password_lineEdit.text()
        password_confirm = self.password_confirm_lineEdit.text()

        if password == password_confirm:
            cursor.execute('''
                INSERT INTO user(fullname , username , password)
                VALUES (%s , %s ,%s)
            ''', (full_name, username, password))
            db.commit()
            self.message_box('User Added!')

            self.user_fullname_lineEdit.setText('')
            self.username_lineEdit.setText('')
            self.password_lineEdit.setText('')
            self.password_confirm_lineEdit.setText('')
        else:
            self.wrong_password_label.setText('The Passwords Are Not Match!l')

    def login_check_user(self):
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                     database='student_management')
        cursor = db.cursor()

        username = self.username_login_user_lineEdit.text()
        password = self.password_login_user_lineEdit.text()

        sql = "SELECT * FROM user"
        cursor.execute(sql)
        data = cursor.fetchall()

        for row in data:
            if username == row[2] and password == row[3]:
                self.message_box('You Are In!')
                self.edit_user_groupBox.setEnabled(True)

                self.user_fullname_lineEdit_edit.setText(row[1])
                self.username_lineEdit_edit.setText(row[2])
                self.password_lineEdit_edit.setText(row[3])

    def edit_user(self):
        fullname = self.user_fullname_lineEdit_edit.text()
        username = self.username_lineEdit_edit.text()
        password = self.password_lineEdit_edit.text()
        password_confirm = self.password_confirm_lineEdit_edit.text()

        if password == password_confirm:
            db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                         database='student_management')
            cursor = db.cursor()

            original_username = self.username_login_user_lineEdit.text()
            cursor.execute('''
                UPDATE user SET fullname =%s , username =%s , password =%s WHERE username =%s
            ''', (fullname, username, password, original_username))
            db.commit()

            self.message_box('Data Updated Successfully!')

            self.user_fullname_lineEdit_edit.setText('')
            self.username_lineEdit_edit.setText('')
            self.password_lineEdit_edit.setText('')
            self.password_confirm_lineEdit_edit.setText('')
            self.edit_user_groupBox.setEnabled(False)
        else:
            self.message_box('Invalid Information!')

    def delete_user(self):
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                     database='student_management')
        cursor = db.cursor()

        user_original_username = self.username_lineEdit_edit.text()
        warning = QMessageBox.warning(self, 'Delete User', 'Are You Sure You Want to Delete This User?',
                                      QMessageBox.Yes | QMessageBox.No)

        if warning == QMessageBox.Yes:
            sql = ''' DELETE FROM user WHERE username=%s'''
            cursor.execute(sql, [(user_original_username)])
            db.commit()
            db.close()
            self.message_box('User Deleted!')

            self.user_fullname_lineEdit_edit.setText('')
            self.username_lineEdit_edit.setText('')
            self.password_lineEdit_edit.setText('')
            self.password_confirm_lineEdit_edit.setText('')

            self.username_login_user_lineEdit.setText('')
            self.password_login_user_lineEdit.setText('')

    # ============================================= Message Box =============================================
    def message_box(self, message):
        msg = QMessageBox()
        msg.setText(message)
        msg.setIcon(QMessageBox.Information)

        msg.exec()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
