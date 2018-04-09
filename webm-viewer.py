#!/usr/bin/env python3
import sys, locale, mpv, os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QMessageBox, QHBoxLayout

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.directory = ""
        self.files = []
    
    def initUI(self):
        self.container = QWidget()
        self.setGeometry(300,300,1200,640)
        self.setWindowTitle('webm viewer')
        self.statusBar()

        #Menu Bar
        main = self.menuBar()
        fileMenu = main.addMenu('File')
        helpMenu = main.addMenu('Help')
        
        about = QAction('About',self)
        about.triggered.connect(self.AboutScreen)
        openFolder = QAction('Open Folder',self)
        openFolder.setShortcut('Ctrl+O')
        openFolder.triggered.connect(self.GetDirectory)
        
        fileMenu.addAction(openFolder)
        helpMenu.addAction(about)
        
        #Video Player
        locale.setlocale(locale.LC_NUMERIC, 'C')
        self.player = mpv.MPV(wid=str(int(self.container.winId())),input_vo_keyboard=True)

        @self.player.on_key_press('z')
        def goBack():
            try:
                self.player.playlist_prev()
            except SystemError:
                self.player.playlist_pos = len(self.files) - 1
            finally:
                self.player.loop = "inf"
    
        @self.player.on_key_press('x')
        def goFoward():
            try:
                self.player.playlist_next()
            except SystemError:
                self.player.playlist_pos = 0
            finally:
                self.player.loop = "inf"

        @self.player.on_key_press('space')
        def pause():
            self.player.pause = not self.player.pause
        
        @self.player.on_key_press('m')
        def mute():
            self.player.mute = not self.player.mute

        #Layout
        self.setCentralWidget(self.container)
        self.container.setAttribute(Qt.WA_DontCreateNativeAncestors)
        self.container.setAttribute(Qt.WA_NativeWindow)
        
        self.show()

    def GetDirectory(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.Directory)

        if dlg.exec_():
            self.directory = dlg.selectedFiles()[0]
            self.statusBar().showMessage(self.directory)
            self.files.clear()
            self.files = self.GetFiles(self.directory)
            self.VideoSetup()

    def AboutScreen(self):
        msg = QMessageBox()
        msg.setWindowTitle('About')
        msg.setText('https://gitlab.com/bunu/webm-viewer')
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    def VideoError(self):
        msg = QMessageBox()
        msg.setWindowTitle('Video Error')
        msg.setText(self.mediaPlayer.errorString())
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def VideoSetup(self):
        self.player.playlist_clear()
        for file in self.files:
            self.player.playlist_append(file)
        self.player.playlist_pos = 0
        self.player.wait_for_playback()

    def GetFiles(self,directory:str) -> list:
        supported_files = []
        for file in os.listdir(directory):
            if file.endswith('.webm') or file.endswith('.gif'):
                supported_files.append(directory +'/' +file)
    
        return supported_files

def main():
    app = QApplication(sys.argv)
    UI = MainUI()
    sys.exit(app.exec_())

if __name__ ==  '__main__':
    main()