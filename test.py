# import sys
# from PyQt5 import QtSql, QtWidgets
# from PyQt5.QtSql import QSqlTableModel
# from PyQt5.QtWidgets import QFileDialog
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     my_app = QtWidgets.QWidget()
#
#     db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
#     db.setDatabaseName('/home/west920/PycharmProjects/InstaBot/classes/Database/people.db')
#     db.open()
#
#     model = QSqlTableModel()
#     model.setTable('accounts')
#     # model.setFilter('id = 1')
#     model.select()
#
#     vb = QtWidgets.QVBoxLayout()
#     nameEdit = QtWidgets.QLineEdit()
#     btn = QtWidgets.QPushButton()
#     btn.setText('Submit')
#     pushButton = QtWidgets.QPushButton()
#     pushButton.setText('Open file')
#
#     tv = QtWidgets.QTableView()
#
#
#     mapModel = QtWidgets.QDataWidgetMapper()
#     mapModel.setModel(model)
#     mapModel.addMapping(nameEdit, 5)
#     mapModel.setSubmitPolicy(QtWidgets.QDataWidgetMapper.ManualSubmit)
#     mapModel.toFirst()
#
#     tv.setModel(model)
#
#     # tv.setModel(model)
#     def selectFile():
#         nameEdit.setText(QFileDialog.getOpenFileName()[0])
#
#     pushButton.clicked.connect(selectFile)
#     btn.clicked.connect(lambda: mapModel.submit())
#
#     vb.addWidget(tv)
#     vb.addWidget(nameEdit)
#     vb.addWidget(pushButton)
#     vb.addWidget(btn)
#
#
#     my_app.setLayout(vb)
#
#     my_app.show()
#     sys.exit(app.exec_())
from classes.Database.Models.TaskSettings import Tasks

t = Tasks()