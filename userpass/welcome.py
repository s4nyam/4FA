

from PyQt4 import QtCore, QtGui
# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client
import os;

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(466, 283)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 30, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 120, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
	
	self.uname_lineEdit = QtGui.QLineEdit(MainWindow)
        self.uname_lineEdit.setGeometry(QtCore.QRect(180, 110, 113, 20))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.signup_btn = QtGui.QPushButton(MainWindow)
        self.signup_btn.setGeometry(QtCore.QRect(210, 200, 51, 23))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        ######################### Button Event ##############################3
        self.signup_btn.clicked.connect(self.handleButton)
	
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
	

    def handleButton(self):
        OTP = self.uname_lineEdit.text();
	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = "ACe6a26c83d6b8342daef53baab045bb1c"
	auth_token = "6fb86df5a1adad8fd094e83cc69322f1"
	client = Client(account_sid, auth_token)
	message = client.messages("SM02d78cca32e542269499a29e619a055c").fetch()
	z=message.body
	
	if(str(z[38:])==str(OTP)):
       		print ('User Verified!!!')
                with open('/home/superuser/Desktop/project_KEYRING/myTextFile.txt', 'a') as myFile:
                     myFile.write('\n')
        	     myFile.write(OTP)
		os.system('python /home/superuser/Desktop/project_KEYRING/facemodule/face.py');
		  
	else:
		print('User Not verified!!')
	

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Enter OTP : ", None))
	self.signup_btn.setText(_translate("MainWindow", "verify", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

