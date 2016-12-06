import sys
from PySide import QtGui
from PySide import QtCore 
from pygame import mixer # Load the required library
class SetAlarmPage(QtGui.QWidget):
    
    def __init__(self):
        super(SetAlarmPage, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        saveButton = QtGui.QPushButton("Save")
        cancelButton = QtGui.QPushButton("Cancel")
        hbox= QtGui.QHBoxLayout ()
        hbox.addStretch(1)
        hbox.addWidget(saveButton)
        hbox.addWidget(cancelButton )
        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        #hr min time 
        hrlb = QtGui.QLabel("<b>hr</b>")
        minlb = QtGui.QLabel("<b>min</b>")
        self.hrinput = QtGui.QLineEdit()
        self.mininput=QtGui.QLineEdit()
        #ampmComb= QtGui.QComboBox()
        
        #ampmComb.setStyleSheet("width:30px; background-color:rgb(255,255,255); color: rgb(0, 0, 0); font-size: 10px; ")
        #ampmComb.addItem("AM")
        #ampmComb.addItem("PM")
        timebox= QtGui.QHBoxLayout ()
        timebox.addStretch(1)
        timebox .addWidget(hrlb)
        timebox.addWidget (self.hrinput)
        timebox .addWidget(minlb,5,1)
        timebox.addWidget (self.mininput)
        #timebox.addWidget(ampmComb)
        #self.setLayout (vbox)
        setalarmlb = QtGui.QLabel("<b>Set Alarm</b>")
        #backbutton = QtGui.QPushButton ("back")
        #backbutton.setStyleSheet("width:5px")
        mygrid = QtGui.QGridLayout()
        mygrid.horizontalSpacing()
        mygrid.rowStretch(0)
        #mygrid.addWidget(backbutton, 0, 1)
        mygrid.addWidget(setalarmlb,0,1)
        mygrid.addLayout (timebox,2,1)
        mygrid.addLayout(vbox,2,3)
        print (mygrid)
        #event source
        saveButton.clicked.connect(self.saveaction)
        cancelButton.clicked.connect(self.cancelaction)
        #backbutton.clicked.connect(self.backaction)
       
        
        
        self.setLayout (mygrid)
        self.setStyleSheet("QWidget {background-color:rgb(0,0,0) ; }  QLabel { color: rgb(173, 216, 230); font-size: 12px;   solid rgba(188, 188, 188, 250); } QSpinBox { color: rgb(50, 50, 50); font-size: 11px; background-color: rgba(255, 188, 20, 50); } QButton { background-color:#008CBA; color : rgb (0,0,0)}")
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('New Alarm')    
        self.show()
    def saveaction (self):
		print ("save button clicked")
		hour=self.hrinput.text()
		mint=self.mininput.text()
		hourint=int (hour)
		minint =int (mint)
		now=QtCore.QTime.currentTime ()
		#print (now.hour())
		#print (now.minute())
		#print (type(now))
		alarm = QtCore.QTime(hourint,minint)
		print (alarm)
		msgBox = QtGui.QMessageBox()
		if (alarm.isValid()):
			
			#compute number of hours and minutes  between current time and entered time 
			DiffHour=0
			DiffMin=0
			if (now.minute()==0):
				DiffHour = alarm.hour() - now.hour()
			else:
				DiffHour = alarm.hour()-(now.hour()+1)  	
			#print (DiffHour)	
			#compute the number of minutes between two times
			sumMin = alarm.minute() + (60-now.minute() )
			if (sumMin==60):
				DiffHour = DiffHour+1
			elif (sumMin >60 ):
				plushr= sumMin/60 
				DiffMin = sumMin %60 
				DiffHour += plushr
					 
			else:
				DiffMin = sumMin
			print (DiffHour)
			print (DiffMin)
			if (DiffHour < 0):
				DiffHour = DiffHour + 24
				
			
			
			msgBox.setText("Alarm set for  "+ str (DiffHour)+" hours  and "+ str( DiffMin)+" minutes from now.")
			interval=(60000*DiffMin)+((DiffHour*60)*60000)
			
			QtCore.QTimer.singleShot(interval, self.wakeupNow)			   			 
		else:
			msgBox.setText("Please check the validation  of alarm")
		
		
		
		#print (msgBox.informativeText())
		
		msgBox.exec_()
        

	

        
    def  cancelaction(self):
		print ("cancel button clicked")
		self.close()
    def  backaction (self):
		print ("back button clicked")
    def wakeupNow(self):
		print ("wakupmethod")
		mixer.init()
		mixer.music.load('/home/sohaila/projects/AlarmVersion0/wakeup.wav')
		mixer.music.play()
		
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = SetAlarmPage()
    sys.exit(app.exec_())
if __name__=='__main__':
	main ()
