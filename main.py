import sqlite3
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QCalendarWidget, QListWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)
        self.updateTaskList()

    def calendarDateChanged(self):
        self.updateTaskList()

    def updateTaskList(self):
        self.tasksListWidget.clear()
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")

        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            query = "SELECT task, completed FROM tasks WHERE date = ?"
            cursor.execute(query, (date,))
            tasks = cursor.fetchall()
            for task, completed in tasks:
                item = QListWidgetItem(task)
                item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                item.setCheckState(Qt.Checked if completed == 'YES' else Qt.Unchecked)
                self.tasksListWidget.addItem(item)
            db.close()
        except sqlite3.Error as e:
            self.showDBErrorMessageBox(e)

    def saveChanges(self):
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")

        try:
            db = sqlite3.connect("data.db")
            cursor = db.cursor()
            for i in range(self.tasksListWidget.count()):
                item = self.tasksListWidget.item(i)
                task = item.text()
                completed = 'YES' if item.checkState() == Qt.Checked else 'NO'
                query = "UPDATE tasks SET completed = ? WHERE task = ? AND date = ?"
                cursor.execute(query, (completed, task, date))
            db.commit()
            db.close()
            QMessageBox.information(self, "Success", "Changes saved.")
        except sqlite3.Error as e:
            self.showDBErrorMessageBox(e)

    def addNewTask(self):
        newTask = self.taskLineEdit.text().strip()
        if newTask:
            date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
            try:
                db = sqlite3.connect("data.db")
                cursor = db.cursor()
                query = "INSERT INTO tasks(task, completed, date) VALUES (?, 'NO', ?)"
                cursor.execute(query, (newTask, date))
                db.commit()
                db.close()
                self.taskLineEdit.clear()
                self.updateTaskList()
            except sqlite3.Error as e:
                self.showDBErrorMessageBox(e)

    def showDBErrorMessageBox(self, error):
        QMessageBox.critical(self, "Database Error", f"An error occurred with the database: {error}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
