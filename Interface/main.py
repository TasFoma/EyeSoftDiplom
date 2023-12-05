import sys
from PyQt6.QtCore import QSize, QUrl
from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QSizePolicy, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QSoundEffect
from keyboardFunction import KeyboardWindow
from LMBFunction import LMBFunction
from RMBFunction import RMBFunction
from DLMBFunction import DLMBFunction
from DRMBFunction import DRMBFunction
'''from HelpFunction import helpFunction'''
from SettingsFunction import settingsFunction


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Eye Cue Rew See")
        self.setWindowIcon(QIcon("./icons/WNDICO.jpg"))
        screen_size = QApplication.primaryScreen().size()
        self.wndWidth = int(screen_size.width()/10)
        self.wndHeight = int(4*(screen_size.height()/5))
        self.setGeometry(int(33*(screen_size.width()/40)), int(screen_size.height()/10), self.wndWidth, self.wndHeight)

        self.keyboard = None

        self.helpSygnal = QSoundEffect()
        self.helpSygnal.setSource(QUrl.fromLocalFile("./media/help.wav"))
        self.helpSygnal.setVolume(20)
        self.helpSygnal.setLoopCount(-2)

        '''Labels defenition
        self.Label = QLabel("Eye Cue Rew See")
        self.Label.setStyleSheet("border: 1px solid black;")
        '''
        '''
        self.calc_label.setStyleSheet("border: 1px solid black;")
        self.dialogue_label.setStyleSheet("border: 1px solid black;")
        self.portrait_label.setStyleSheet("border: 1px solid black;")
        '''

        '''Buttons definition'''

        self.KeyboardButton = QPushButton(QIcon("./icons/KEY.png"), "Клавиатура", self)
        self.KeyboardButton.setIconSize(QSize(50, 50))
        self.KeyboardButton.setStyleSheet("text-align: left;")
        self.KeyboardButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.KeyboardButton.setCheckable(True)
        self.KeyboardButton.clicked.connect(self.keyboardFunction)

        self.LMBButton = QPushButton(QIcon("./icons/LMB.png"), "Левая кнопка мыши (ЛКМ)", self)
        self.LMBButton.setIconSize(QSize(50, 50))
        self.LMBButton.setStyleSheet("text-align: left;")
        self.LMBButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.LMBButton.clicked.connect(LMBFunction)

        self.RMBButton = QPushButton(QIcon("./icons/RMB.png"), "Правая кнопка мыши (ПКМ)", self)
        self.RMBButton.setIconSize(QSize(50, 50))
        self.RMBButton.setStyleSheet("text-align: left;")
        self.RMBButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.RMBButton.clicked.connect(RMBFunction)

        self.DoubleLMBButton = QPushButton(QIcon("./icons/DLMB.png"), "Двойное нажатие ЛКМ", self)
        self.DoubleLMBButton.setIconSize(QSize(50, 50))
        self.DoubleLMBButton.setStyleSheet("text-align: left;")
        self.DoubleLMBButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.DoubleLMBButton.clicked.connect(DLMBFunction)

        self.DoubleRMBButton = QPushButton(QIcon("./icons/DRMB.png"), "Двойное нажатие ПКМ", self)
        self.DoubleRMBButton.setIconSize(QSize(50, 50))
        self.DoubleRMBButton.setStyleSheet("text-align: left;")
        self.DoubleRMBButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.DoubleRMBButton.clicked.connect(DRMBFunction)

        self.HelpButton = QPushButton(QIcon("./icons/HELP.png"), "Помощь", self)
        self.HelpButton.setIconSize(QSize(50, 50))
        self.HelpButton.setStyleSheet("text-align: left;")
        self.HelpButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.HelpButton.setCheckable(True)
        self.HelpButton.clicked.connect(self.helpFunction)

        self.SettingsButton = QPushButton(QIcon("./icons/SETT.png"), "Настройки", self)
        self.SettingsButton.setIconSize(QSize(50, 50))
        self.SettingsButton.setStyleSheet("text-align: left;")
        self.SettingsButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.SettingsButton.clicked.connect(settingsFunction)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.KeyboardButton)
        self.main_layout.addWidget(self.LMBButton)
        self.main_layout.addWidget(self.RMBButton)
        self.main_layout.addWidget(self.DoubleLMBButton)
        self.main_layout.addWidget(self.DoubleRMBButton)
        self.main_layout.addWidget(self.HelpButton)
        self.main_layout.addWidget(self.SettingsButton)

        widget = QWidget()
        widget.setLayout(self.main_layout)
        self.setCentralWidget(widget)

    def keyboardFunction(self):
        if self.KeyboardButton.isChecked():
            if self.keyboard is None:
                 self.keyboard = KeyboardWindow()
            self.keyboard.show()
            print('keyboard show')
        else:
            if self.keyboard is None:
                self.keyboard = KeyboardWindow()
            self.keyboard.hide()
            print('keyboard hide')

    def helpFunction(self):
        if self.HelpButton.isChecked():
            self.helpSygnal.play()
            print('Help sygnal is playing')
        else:
            self.helpSygnal.stop()
            print('Help sygnal stopped')

    def closeEvent(self, event):
        if self.keyboard is not None:
            self.keyboard.close()

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
