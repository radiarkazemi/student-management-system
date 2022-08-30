from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector

from PyQt5.uic import loadUiType

ui, _ = loadUiType('student.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
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

    # ============================================= Student =============================================
    def show_all_students(self):
        pass

    def add_new_student(self):
        pass

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
