from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector

from PyQt5.uic import loadUiType
import database as database_db

ui, _ = loadUiType('student.ui')


class MainApp(QMainWindow, ui):
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

    # =============================================open tab=============================================
    def create_database(self):
        database_db

        # ============================================= Student =============================================

    def show_all_students(self):
        pass

    def add_new_student(self):
        db = mysql.connector.connect(host='127.0.0.1', user='root', password='@615$011m9841k@',
                                     database='student_management')
        cursor = db.cursor()

        national_id = int(self.national_id_lineEdit.text())

    def edit_student(self):
        pass

    def delete_student(self):
        pass

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
