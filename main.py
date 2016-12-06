#!/usr/bin/python
# -*- coding: utf-8 -*-

# simple.py

import sys
from PySide import QtGui , QtCore

class Alarm(QtGui.QMainWindow):
	
	def __init__(self):
		super (Alarm,self).__init__()
		self.initwindow()
		    	
	def initwindow(self):
		
		self.statusBar().showMessage('Ready')
		currenttimelb =QtGui.QLabel("<b>Current Time</b>",self)
		currenttimelb.move (250,300)
		self.setGeometry(300, 300, 600, 600)
		self.setWindowTitle('Alarm')
		self.setWindowIcon(QtGui.QIcon("img.png"))
		print ("center")
		qr= self.frameGeometry()
		print (qr)
		btn = QtGui.QPushButton ("alarms ",self)
		btn.setToolTip('Go to alarms page')
		btn.move(100,500)
		print ("initwindow")
		#quit button 
		qbutton = QtGui.QPushButton ("Exit  ",self)
		#qbutton.clicked.connect(QtCore.QCoreApplication.instance().quit)
		qbutton.clicked.connect(QtCore.QCoreApplication.instance().quit)
		qbutton.setToolTip('Quit')
		qbutton.move(500,500)
		
		
		
		self.show() 
	# def closeEvent(self, event):
    #    
     #   reply = QtGui.QMessageBox.question(self, 'Message',
    #        "Are you sure to quit?", QtGui.QMessageBox.Yes | 
    #        QtGui.QMessageBox.No, QtGui.QMessageBox.No)
    #
    #    if reply == QtGui.QMessageBox.Yes:
    #        event.accept()
    #    else:
    #        event.ignore()        
        

		
def  main ():
	app = QtGui.QApplication(sys.argv)
	
	w = Alarm ()
	sys.exit(app.exec_())



if __name__ == '__main__':
    main()


	







#wid = QtGui.QWidget() #The default constructor has no parent. A widget with no parent is called a window. 
#wid.resize(600, 800)
#wid.setWindowTitle('Alarm')
#wid.show()

#sys.exit(app.exec_())
