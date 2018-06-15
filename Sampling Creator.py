
# coding: utf-8

# In[1]:


import numpy as np
import os
import cv2
import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QDesktopWidget, QFileDialog,
                             QSlider, QPushButton, QLabel, QLCDNumber)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap



class Sampling_Creator_Main_Class(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

        
    def initUI(self):
        self.height_of_screen = QDesktopWidget().availableGeometry().height()
        self.width_of_screen = QDesktopWidget().availableGeometry().width()
        
        self.path_to_pull = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))
        self.list_dir = os.listdir(self.path_to_pull)
        self.list_dir_iterator = 0
        self.path_to_push = None
        
        self.tmp_im = cv2.imread(self.path_to_pull + '/' + self.list_dir[self.list_dir_iterator])
        self.tmp_im_non_rotated = self.tmp_im.copy()

        self.create_lables()
        self.create_LCD_numbers()
        self.create_sliders()
        self.create_picture()
        self.create_buttons()
        self.statusBar()
        
        self.setWindowTitle('Sampling Creator')
        self.setGeometry(self.norm(1, 'w'), self.norm(5, 'h'),
                         self.norm(98, 'w'), self.norm(93, 'h'))
        self.show()

    
    def create_lables(self):
        self.label_H = QLabel('Hue', self)
        self.label_H.setGeometry(self.norm(2, 'w'), self.norm(1, 'h'),
                                 self.norm(3, 'w'), self.norm(3, 'h'))
        
        self.label_L = QLabel('Lightness', self)
        self.label_L.setGeometry(self.norm(6, 'w'), self.norm(1, 'h'),
                                 self.norm(3, 'w'), self.norm(3, 'h'))
        
        self.label_S = QLabel('Saturation', self)
        self.label_S.setGeometry(self.norm(10, 'w'), self.norm(1, 'h'),
                                 self.norm(3, 'w'), self.norm(3, 'h'))
        
        self.label_A = QLabel('Angle', self)
        self.label_A.setGeometry(self.norm(14, 'w'), self.norm(1, 'h'),
                                 self.norm(3, 'w'), self.norm(3, 'h'))
    
    
    def create_LCD_numbers(self):
        self.num_H = QLCDNumber(self)
        self.num_H.setGeometry(self.norm(2, 'w'), self.norm(87, 'h'),
                               self.norm(3, 'w'), self.norm(3, 'h'))
        
        self.num_L = QLCDNumber(self)
        self.num_L.setGeometry(self.norm(6, 'w'), self.norm(87, 'h'),
                               self.norm(3, 'w'), self.norm(3, 'h'))
        
        self.num_S = QLCDNumber(self)
        self.num_S.setGeometry(self.norm(10, 'w'), self.norm(87, 'h'),
                               self.norm(3, 'w'), self.norm(3, 'h'))
        
        self.num_A = QLCDNumber(self)
        self.num_A.setGeometry(self.norm(14, 'w'), self.norm(87, 'h'),
                               self.norm(3, 'w'), self.norm(3, 'h'))
    
    
    def create_sliders(self):
        self.sld_H = QSlider(Qt.Vertical, self)
        self.sld_L = QSlider(Qt.Vertical, self)
        self.sld_S = QSlider(Qt.Vertical, self)
        self.sld_A = QSlider(Qt.Vertical, self)
        
        self.sld_H.setMinimum(-179)
        self.sld_H.setMaximum(179)
        self.sld_H.setValue(0)
        self.sld_H.setFocusPolicy(Qt.StrongFocus)
        self.sld_H.setTickPosition(QSlider.TicksBothSides)
        self.sld_H.setTickInterval(30)
        self.sld_H.setSingleStep(1)
        self.sld_H.valueChanged[int].connect(self.changeValue_H)
        self.sld_H.valueChanged[int].connect(self.num_H.display)
        self.sld_H.setGeometry(self.norm(2, 'w'), self.norm(5, 'h'),
                               self.norm(3, 'w'), self.norm(81, 'h'))
        
        self.sld_L.setMinimum(-257)
        self.sld_L.setMaximum(257)
        self.sld_L.setValue(0)
        self.sld_L.setFocusPolicy(Qt.StrongFocus)
        self.sld_L.setTickPosition(QSlider.TicksBothSides)
        self.sld_L.setTickInterval(43)
        self.sld_L.setSingleStep(1)
        self.sld_L.valueChanged[int].connect(self.changeValue_L)
        self.sld_L.valueChanged[int].connect(self.num_L.display)
        self.sld_L.setGeometry(self.norm(6, 'w'), self.norm(5, 'h'),
                               self.norm(3, 'w'), self.norm(81, 'h'))
        
        self.sld_S.setMinimum(-257)
        self.sld_S.setMaximum(257)
        self.sld_S.setValue(0)
        self.sld_S.setFocusPolicy(Qt.StrongFocus)
        self.sld_S.setTickPosition(QSlider.TicksBothSides)
        self.sld_S.setTickInterval(43)
        self.sld_S.setSingleStep(1)
        self.sld_S.valueChanged[int].connect(self.changeValue_S)
        self.sld_S.valueChanged[int].connect(self.num_S.display)
        self.sld_S.setGeometry(self.norm(10, 'w'), self.norm(5, 'h'),
                               self.norm(3, 'w'), self.norm(81, 'h'))
        
        self.sld_A.setMinimum(-180)
        self.sld_A.setMaximum(180)
        self.sld_A.setValue(0)
        self.sld_A.setFocusPolicy(Qt.StrongFocus)
        self.sld_A.setTickPosition(QSlider.TicksBothSides)
        self.sld_A.setTickInterval(30)
        self.sld_A.setSingleStep(1)
        self.sld_A.valueChanged[int].connect(self.changeValue_A)
        self.sld_A.valueChanged[int].connect(self.num_A.display)
        self.sld_A.setGeometry(self.norm(14, 'w'), self.norm(5, 'h'),
                               self.norm(3, 'w'), self.norm(81, 'h'))
        
        self.old_value_H = 0
        self.old_value_L = 0
        self.old_value_S = 0
        
        
    def create_picture(self):
        self.picture = QLabel(self)

        self.pixmap = QPixmap(self.path_to_pull + '/' + self.list_dir[self.list_dir_iterator])        
        self.picture.setPixmap(self.pixmap.scaled(self.norm(78, 'w'), 
                                                  self.norm(87, 'h'), 
                                                  Qt.KeepAspectRatio))
        
        self.picture.setGeometry(self.norm(18, 'w'), self.norm(1, 'h'),
                                 self.norm(78, 'w'), self.norm(87, 'h'))
        
        
    def create_buttons(self):
        self.btn_previous = QPushButton('Previous', self)
        self.btn_next = QPushButton('Next', self)
        self.btn_save = QPushButton('Save', self)
        
        self.btn_previous.clicked.connect(self.buttonClicked)
        self.btn_next.clicked.connect(self.buttonClicked)
        self.btn_save.clicked.connect(self.buttonClicked)
        
        self.btn_previous.setGeometry(self.norm(20, 'w'), self.norm(89, 'h'),
                                      self.norm(3, 'w'), self.norm(3, 'h'))
        self.btn_next.setGeometry(self.norm(55, 'w'), self.norm(89, 'h'),
                                  self.norm(3, 'w'), self.norm(3, 'h'))
        self.btn_save.setGeometry(self.norm(90, 'w'), self.norm(89, 'h'),
                                  self.norm(3, 'w'), self.norm(3, 'h'))
        
        self.btn_save_was_clicked = False
        self.btn_next_or_prev_was_clicked = False
        
        
    def changeValue_H(self, value):
        if (self.btn_next_or_prev_was_clicked == False):
            hls_im = cv2.cvtColor(self.tmp_im, cv2.COLOR_RGB2HLS)
            hls_im[:, :, 0] = hls_im[:, :, 0] + value - self.old_value_H
            self.tmp_im = cv2.cvtColor(hls_im, cv2.COLOR_HLS2RGB)
        
            hls_im = cv2.cvtColor(self.tmp_im_non_rotated, cv2.COLOR_RGB2HLS)
            hls_im[:, :, 0] = hls_im[:, :, 0] + value - self.old_value_H
            self.tmp_im_non_rotated = cv2.cvtColor(hls_im, cv2.COLOR_HLS2RGB)
        
            self.old_value_H = value
        
            cv2.imwrite('tmp_im.jpg', self.tmp_im)
            self.picture.setPixmap(QPixmap('tmp_im.jpg').scaled(self.norm(78, 'w'), 
                                                  self.norm(87, 'h'), 
                                                  Qt.KeepAspectRatio))
        
        
    def changeValue_L(self, value):
        if (self.btn_next_or_prev_was_clicked == False):
            hls_im = cv2.cvtColor(self.tmp_im, cv2.COLOR_RGB2HLS)
            hls_im[:, :, 1] = hls_im[:, :, 1] + value - self.old_value_L
            self.tmp_im = cv2.cvtColor(hls_im, cv2.COLOR_HLS2RGB)
        
            hls_im = cv2.cvtColor(self.tmp_im_non_rotated, cv2.COLOR_RGB2HLS)
            hls_im[:, :, 1] = hls_im[:, :, 1] + value - self.old_value_L
            self.tmp_im_non_rotated = cv2.cvtColor(hls_im, cv2.COLOR_HLS2RGB)
        
            self.old_value_L = value
        
            cv2.imwrite('tmp_im.jpg', self.tmp_im)
            self.picture.setPixmap(QPixmap('tmp_im.jpg').scaled(self.norm(78, 'w'), 
                                                  self.norm(87, 'h'), 
                                                  Qt.KeepAspectRatio))
        
        
    def changeValue_S(self, value):
        if (self.btn_next_or_prev_was_clicked == False):
            hls_im = cv2.cvtColor(self.tmp_im, cv2.COLOR_RGB2HLS)
            hls_im[:, :, 2] = hls_im[:, :, 2] + value - self.old_value_S
            self.tmp_im = cv2.cvtColor(hls_im, cv2.COLOR_HLS2RGB)
        
            hls_im = cv2.cvtColor(self.tmp_im_non_rotated, cv2.COLOR_RGB2HLS)
            hls_im[:, :, 2] = hls_im[:, :, 2] + value - self.old_value_S
            self.tmp_im_non_rotated = cv2.cvtColor(hls_im, cv2.COLOR_HLS2RGB)
        
            self.old_value_S = value
        
            cv2.imwrite('tmp_im.jpg', self.tmp_im)
            self.picture.setPixmap(QPixmap('tmp_im.jpg').scaled(self.norm(78, 'w'), 
                                                  self.norm(87, 'h'), 
                                                  Qt.KeepAspectRatio))
        
        
    def changeValue_A(self, value):
        if (self.btn_next_or_prev_was_clicked == False):
            self.tmp_im = self.rotate_bound(self.tmp_im_non_rotated, value)
        
            cv2.imwrite('tmp_im.jpg', self.tmp_im)
            self.picture.setPixmap(QPixmap('tmp_im.jpg').scaled(self.norm(78, 'w'), 
                                                  self.norm(87, 'h'), 
                                                  Qt.KeepAspectRatio))
            
        
    def buttonClicked(self):
        sender = self.sender()
        if (sender.text() == 'Next' and self.list_dir_iterator < len(self.list_dir) - 1):
            self.list_dir_iterator += 1
            self.btn_next_or_prev_was_clicked = True
            
            self.tmp_im = cv2.imread(self.path_to_pull + '/' + self.list_dir[self.list_dir_iterator])
            self.tmp_im_non_rotated = self.tmp_im.copy()
            self.picture.setPixmap(QPixmap(self.path_to_pull + '/' + 
                                           self.list_dir[self.list_dir_iterator]).scaled(self.norm(78, 'w'), 
                                                  self.norm(87, 'h'), 
                                                  Qt.KeepAspectRatio))
            
            self.sld_H.setValue(0)
            self.sld_L.setValue(0)
            self.sld_S.setValue(0)
            self.sld_A.setValue(0)
            
            self.btn_next_or_prev_was_clicked = False
            
        elif (sender.text() == 'Previous' and self.list_dir_iterator > 0):
            self.list_dir_iterator -= 1
            self.btn_next_or_prev_was_clicked = True
            
            self.tmp_im = cv2.imread(self.path_to_pull + '/' + self.list_dir[self.list_dir_iterator])
            self.tmp_im_non_rotated = self.tmp_im.copy()
            self.picture.setPixmap(QPixmap(self.path_to_pull + '/' + 
                                           self.list_dir[self.list_dir_iterator]).scaled(self.norm(78, 'w'), 
                                                  self.norm(87, 'h'), 
                                                  Qt.KeepAspectRatio))
            
            self.sld_H.setValue(0)
            self.sld_L.setValue(0)
            self.sld_S.setValue(0)
            self.sld_A.setValue(0)
            
            self.btn_next_or_prev_was_clicked = False
            
        elif (sender.text() == 'Save'):
            if (self.btn_save_was_clicked == False):
                self.btn_save_was_clicked = True
                self.path_to_push = str(QFileDialog.getExistingDirectory(self, 'Select Directory'))

            cv2.imwrite(self.path_to_push + '/' + self.list_dir[self.list_dir_iterator], self.tmp_im)
        
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
        
    def rotate_bound(self, image, angle):
        # grab the dimensions of the image and then determine the
        # center
        (h, w) = image.shape[:2]
        (cX, cY) = (w // 2, h // 2) 
        # grab the rotation matrix (applying the negative of the
        # angle to rotate clockwise), then grab the sine and cosine
        # (i.e., the rotation components of the matrix)
        M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1]) 
        # compute the new bounding dimensions of the image
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin)) 
        # adjust the rotation matrix to take into account translation
        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY
        # perform the actual rotation and return the image
        return cv2.warpAffine(image, M, (nW, nH))
    
    
    def norm(self, per, height_or_width):
        # per is from 0 to 100
        if (height_or_width == 'h'):
            return int(per * self.height_of_screen / 100)
        elif (height_or_width == 'w'):
            return int(per * self.width_of_screen / 100)


    
if __name__ == '__main__':
    Sampling_Creator = QApplication(sys.argv)
    Sampling_Creator_Instance = Sampling_Creator_Main_Class()
    sys.exit(Sampling_Creator.exec_())

