import paramiko
import logging
import sys
import demo_ui
import sys
import time
import json
import threading

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# generate = subprocess.Popen('pyuic5 -o demo_ui.py demo.ui')
# generate.wait()

"""
todo: 
    选中一列就选中一行
    双击某一行弹窗显示其服务器日志内容
    增加一个tab获取日志
"""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('hello world')

app = QApplication([])




class MainWindow(QMainWindow):
    alert_signal = pyqtSignal(str)
    def __init__(self, parent=None):        
        super(MainWindow, self).__init__(parent)        

        self.data_list = self.read_json()
        self.signal_connected = False

        self.ui = demo_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.table = self.ui.tableWidget
        self.set_header()
        self.add_item()
        
        
        self.ui.update_selected_button.clicked.connect(self.on_click_update_selected)
        self.ui.update_all_button.clicked.connect(self.on_click_update_all)
        self.alert_signal.connect(self.show_message)


    def read_json(self):
        with open('./server_list.json','r',encoding="utf-8") as f:
            json_list = json.load(f)
            return json_list

    def show_logging(self,item):
        """
        双击某一行显示服务器输出的内容
        """
        logging = 'empty'
        for data in self.data_list:
            if data["hostname"] == self.table.item(item.row(),1).text() and data["service_name"] == self.table.item(item.row(),0).text():
                logging = data["log"]
                logger.info('log:%s',logging)
                break

        box = QMessageBox()
        box.setWindowTitle("输出日志")
        box.setText(logging)
        box.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec()
    
    def show_message(self,message):
        """
        显示错误弹窗
        """
        box = QMessageBox()
        box.setWindowTitle("输出日志")
        box.setText(message)
        
        box.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        box.setStandardButtons(QMessageBox.Ok)
        box.exec()

        

    def adjust_table(self):
        self.table.setAlternatingRowColors(True)
        self.table.resizeColumnsToContents()
        # self.table.resizeRowsToContents()
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        if(not self.signal_connected):
            self.table.itemDoubleClicked.connect(self.show_logging)
            self.signal_connected = True

    def set_header(self):
        header_labels = ['service name','host name','keyword','last check','status']
        self.table.setColumnCount(len(header_labels))
        self.table.setHorizontalHeaderLabels(header_labels)        
        
        
    def add_item(self):
        for data in self.data_list:
            # logger.info('data:%s',data.get('service_name'))
            rowPosition=self.table.rowCount()
            self.table.insertRow(rowPosition)            
            self.table.setItem(rowPosition,0,QTableWidgetItem(data.get('service_name')))
            self.table.setItem(rowPosition,1,QTableWidgetItem(data.get('hostname')))
            self.table.setItem(rowPosition,2,QTableWidgetItem(data.get('keyword')))
            self.table.setItem(rowPosition,3,QTableWidgetItem(data.get('last_check')))
            self.table.setItem(rowPosition,4,QTableWidgetItem(data.get('status')))            

        self.adjust_table()
        

    def get_current_time(self):
        return time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime())                

    def clear_table(self):
        while(self.table.rowCount()>0):
            self.table.removeRow(self.table.rowCount()-1)
        # self.table.setRowCount(0)
        # self.table.clearContents()

    def filter_text(self,item):
        if item.column()==1:
            return item.text()

    def on_click_update_selected(self):        
        threading.Thread(target=self.update_selected,args=()).start()    

    def on_click_update_all(self):        
        threading.Thread(target=self.update_all,args=()).start()
        # self.clear_table()
        # self.add_item()
    
    def update_all(self):
        """
        更新所有数据
        """
        for data in self.data_list:
            keyword = data['keyword']
            hostname = data['hostname']
            logging = self.ssh_client(hostname=hostname,keyword=keyword)
            
            if(keyword in logging):
                status = 'good'
            else:
                status = 'not good'
            data['status']=status
            data['last_check'] = self.get_current_time()
            data['log']=logging

            logger.info('log:%s',logging)
        
            self.clear_table()        
            self.add_item()

    def update_selected(self):
        """
        更新选中的数据
        """

        items = self.table.selectedItems()
        if len(items) == 0:
            return

        
        for item in items:
            hostname = self.table.item(item.row(),1).text()
            keyword = self.table.item(item.row(),2).text()
            for data in self.data_list:
                 if data["hostname"] == hostname and data["keyword"]==keyword:
                     logging = self.ssh_client(hostname=hostname,keyword=keyword)
                     if(keyword in logging):
                        status = 'good'
                     else:
                        status = 'not good'

                     data['status']=status
                     data['last_check'] = self.get_current_time()
                     data['log']=logging

                     logger.info('log:%s',logging)

        self.clear_table()        
        self.add_item()
        

    def isSignalConnected(self, obj, name):
        """判断信号是否连接
        :param obj:        对象
        :param name:       信号名，如 clicked()
        """
        index = obj.metaObject().indexOfMethod(name)
        if index > -1:
            method = obj.metaObject().method(index)
            if method:
                return obj.isSignalConnected(method)
        return False

    def ssh_client(self,hostname,keyword):

        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.load_system_host_keys()

        username = self.ui.username.text()
        password = self.ui.password.text()
        dmz_password = self.ui.dmz_password.text()
        # logger.info('username:%s',username)
        try:
            ssh_client.connect(hostname=hostname, port=8022,username=username,password=password)
        except Exception as e:
            logger.info('error:%s',e)
            self.alert_signal.emit(hostname+str(e))
            

        stdin, stdout, stderr = ssh_client.exec_command('ps -ef |grep '+keyword+'|grep -v grep')
        output  = stdout.readlines()
        if stderr:
            logger.info('stderr:%s',stderr)
        
        return ''.join(output)

m = MainWindow()
m.show()

sys.exit(app.exec_())




    