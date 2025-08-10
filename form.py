from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)
import res
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(700, 600))
        MainWindow.setMaximumSize(QSize(3000, 3000))
        MainWindow.setIconSize(QSize(26, 26))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(700, 600))
        self.centralwidget.setMaximumSize(QSize(3000, 3000))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(260, 600))
        self.frame.setMaximumSize(QSize(451, 3000))
        self.frame.setStyleSheet(u"background-color:rgb(52,52,52);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 7, 7, 23)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 100))
        self.pushButton.setMaximumSize(QSize(200, 200))
        self.pushButton.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/main.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(100, 100))

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font-size:18px;\n"
"color:rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.button_circle = QPushButton(self.frame)
        self.button_circle.setObjectName(u"button_circle")
        self.button_circle.setMinimumSize(QSize(70, 40))
        self.button_circle.setMaximumSize(QSize(150, 50))
        self.button_circle.setStyleSheet(u"background-color:rgb(151, 255, 198);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_circle.setIcon(icon1)
        self.button_circle.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.button_circle)

        self.button_close = QPushButton(self.frame)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setMinimumSize(QSize(70, 40))
        self.button_close.setMaximumSize(QSize(150, 50))
        self.button_close.setStyleSheet(u"background-color:rgb(151, 255, 198);\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/close.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_close.setIcon(icon2)
        self.button_close.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.button_close)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.result_frame = QFrame(self.frame)
        self.result_frame.setObjectName(u"result_frame")
        self.result_frame.setMinimumSize(QSize(250, 40))
        self.result_frame.setMaximumSize(QSize(300, 70))
        self.result_frame.setStyleSheet(u"border:none;\n"
"")
        self.result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.result_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.result_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.result_label = QLabel(self.result_frame)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(80, 25))
        self.result_label.setMaximumSize(QSize(120, 40))
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.result_label)

        self.result_button = QPushButton(self.result_frame)
        self.result_button.setObjectName(u"result_button")
        self.result_button.setMinimumSize(QSize(30, 30))
        self.result_button.setMaximumSize(QSize(60, 60))
        self.result_button.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.result_button)


        self.horizontalLayout_8.addWidget(self.result_frame)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.play_with_friend = QPushButton(self.frame)
        self.play_with_friend.setObjectName(u"play_with_friend")
        self.play_with_friend.setMinimumSize(QSize(90, 40))
        self.play_with_friend.setMaximumSize(QSize(150, 70))
        self.play_with_friend.setStyleSheet(u"background-color:rgb(66, 189, 38);\n"
"color:rgb(234, 234, 234);\n"
"font-size:14px;\n"
"border:none;\n"
"padding:7px;\n"
"border-radius:5px;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/human.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_with_friend.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.play_with_friend)

        self.play_with_bot = QPushButton(self.frame)
        self.play_with_bot.setObjectName(u"play_with_bot")
        self.play_with_bot.setMinimumSize(QSize(90, 40))
        self.play_with_bot.setMaximumSize(QSize(150, 70))
        self.play_with_bot.setStyleSheet(u"background-color:rgb(66, 189, 38);\n"
"color:rgb(234, 234, 234);\n"
"font-size:14px;\n"
"border:none;\n"
"padding:7px;\n"
"border-radius:5px;\n"
"\n"
"\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/bot.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.play_with_bot.setIcon(icon4)

        self.horizontalLayout_3.addWidget(self.play_with_bot)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border:none;\n"
"background-color:rgb(52,52,52);")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.button_about = QPushButton(self.frame_3)
        self.button_about.setObjectName(u"button_about")
        self.button_about.setMinimumSize(QSize(90, 40))
        self.button_about.setMaximumSize(QSize(150, 70))
        self.button_about.setStyleSheet(u"background-color:rgb(191, 61, 34);\n"
"color:rgb(255, 255, 255);\n"
"font-size:20px;\n"
"border:none;\n"
"border-radius:5px;\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.button_about)


        self.verticalLayout.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.button_restart = QPushButton(self.frame)
        self.button_restart.setObjectName(u"button_restart")
        self.button_restart.setMinimumSize(QSize(90, 40))
        self.button_restart.setMaximumSize(QSize(150, 70))
        self.button_restart.setStyleSheet(u"border:none;\n"
"background-color:rgb(151, 255, 198);\n"
"border-radius:6px;\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/restart.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.button_restart.setIcon(icon5)
        self.button_restart.setIconSize(QSize(20, 20))

        self.horizontalLayout_7.addWidget(self.button_restart)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color:rgb(30, 30, 30);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.tabWidget = QTabWidget(self.frame_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(300, 300))
        self.tabWidget.setMaximumSize(QSize(800, 800))
        self.tabWidget.setStyleSheet(u"border:none;")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button12 = QPushButton(self.tab)
        self.button12.setObjectName(u"button12")
        self.button12.setMinimumSize(QSize(100, 100))
        self.button12.setMaximumSize(QSize(266, 266))
        self.button12.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31);\n"
"")
        self.button12.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button12, 0, 1, 1, 1)

        self.button31 = QPushButton(self.tab)
        self.button31.setObjectName(u"button31")
        self.button31.setMinimumSize(QSize(100, 100))
        self.button31.setMaximumSize(QSize(266, 266))
        self.button31.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31);\n"
"")
        self.button31.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button31, 2, 0, 1, 1)

        self.button22 = QPushButton(self.tab)
        self.button22.setObjectName(u"button22")
        self.button22.setMinimumSize(QSize(100, 100))
        self.button22.setMaximumSize(QSize(266, 266))
        self.button22.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31);\n"
"")
        self.button22.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button22, 1, 1, 1, 1)

        self.button33 = QPushButton(self.tab)
        self.button33.setObjectName(u"button33")
        self.button33.setMinimumSize(QSize(100, 100))
        self.button33.setMaximumSize(QSize(266, 266))
        self.button33.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31);")
        self.button33.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button33, 2, 2, 1, 1)

        self.button11 = QPushButton(self.tab)
        self.button11.setObjectName(u"button11")
        self.button11.setMinimumSize(QSize(100, 100))
        self.button11.setMaximumSize(QSize(266, 266))
        self.button11.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31);\n"
"")
        self.button11.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button11, 0, 0, 1, 1)

        self.button23 = QPushButton(self.tab)
        self.button23.setObjectName(u"button23")
        self.button23.setMinimumSize(QSize(100, 100))
        self.button23.setMaximumSize(QSize(266, 266))
        self.button23.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31);\n"
"")
        self.button23.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button23, 1, 2, 1, 1)

        self.button21 = QPushButton(self.tab)
        self.button21.setObjectName(u"button21")
        self.button21.setMinimumSize(QSize(100, 100))
        self.button21.setMaximumSize(QSize(266, 266))
        self.button21.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31);\n"
"")
        self.button21.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button21, 1, 0, 1, 1)

        self.button13 = QPushButton(self.tab)
        self.button13.setObjectName(u"button13")
        self.button13.setMinimumSize(QSize(100, 100))
        self.button13.setMaximumSize(QSize(320, 320))
        self.button13.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31) ;\n"
"")
        self.button13.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button13, 0, 2, 1, 1)

        self.button32 = QPushButton(self.tab)
        self.button32.setObjectName(u"button32")
        self.button32.setMinimumSize(QSize(100, 100))
        self.button32.setMaximumSize(QSize(266, 266))
        self.button32.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"border: 1px solid rgb(31, 31, 31);\n"
"")
        self.button32.setIconSize(QSize(90, 90))

        self.gridLayout.addWidget(self.button32, 2, 1, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_2 = QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rule_of_game = QLabel(self.tab_2)
        self.rule_of_game.setObjectName(u"rule_of_game")
        self.rule_of_game.setMinimumSize(QSize(280, 20))
        self.rule_of_game.setMaximumSize(QSize(780, 30))
        font = QFont()
        font.setBold(True)
        self.rule_of_game.setFont(font)
        self.rule_of_game.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font-size:24px;\n"
"")
        self.rule_of_game.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.rule_of_game)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.text_of_rule = QTextBrowser(self.tab_2)
        self.text_of_rule.setObjectName(u"text_of_rule")
        self.text_of_rule.setMinimumSize(QSize(280, 265))
        self.text_of_rule.setMaximumSize(QSize(780, 570))
        self.text_of_rule.setStyleSheet(u"background-color:rgb(148, 146, 141);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:7px;\n"
"padding:10px;\n"
"")

        self.verticalLayout_2.addWidget(self.text_of_rule)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_4.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"tic-tac-toe", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"TIC-TAC-TOE", None))
        self.button_circle.setText("")
        self.button_close.setText("")
        self.result_label.setText("")
        self.result_button.setText("")
        self.play_with_friend.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c \u0441 \u0434\u0440\u0443\u0433\u043e\u043c", None))
        self.play_with_bot.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0433\u0440\u0430\u0442\u044c \u0441 \u0431\u043e\u0442\u043e\u043c", None))
        self.button_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.button_restart.setText(QCoreApplication.translate("MainWindow", u"Restart", None))
        self.button12.setText("")
        self.button31.setText("")
        self.button22.setText("")
        self.button33.setText("")
        self.button11.setText("")
        self.button23.setText("")
        self.button21.setText("")
        self.button13.setText("")
        self.button32.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"play", None))
        self.rule_of_game.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b", None))
        self.text_of_rule.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u041a\u0440\u0435\u0441\u0442\u0438\u043a\u0438-\u043d\u043e\u043b\u0438\u043a\u0438 - \u044d\u0442\u043e \u043a\u043b\u0430\u0441\u0441\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u0438\u0433\u0440\u0430 \u0434\u043b\u044f \u0434\u0432\u0443\u0445 \u0438\u0433\u0440\u043e\u043a\u043e\u0432. \u0412\u043e\u0442 \u043e\u0441\u043d\u043e\u0432\u043d\u044b\u0435 \u043f\u0440"
                        "\u0430\u0432\u0438\u043b\u0430:</span></p>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0418\u0433\u0440\u043e\u0432\u043e\u0435 \u043f\u043e\u043b\u0435 \u0441\u043e\u0441\u0442\u043e\u0438\u0442 \u0438\u0437 \u0441\u0435\u0442\u043a\u0438 3\u00d73 \u043a\u043b\u0435\u0442\u043a\u0438</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0414\u0432\u0430 \u0438\u0433\u0440\u043e\u043a\u0430 \u043f\u043e \u043e\u0447\u0435\u0440\u0435\u0434\u0438 \u0441\u0442\u0430\u0432\u044f\u0442 \u043d\u0430 \u0441\u0432\u043e\u0431\u043e\u0434\u043d\u044b\u0435 \u043a\u043b\u0435\u0442\u043a\u0438 \u0441\u0432\u043e\u0438"
                        " \u0437\u043d\u0430\u043a\u0438:</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u0435\u0440\u0432\u044b\u0439 \u0438\u0433\u0440\u043e\u043a \u0441\u0442\u0430\u0432\u0438\u0442 \u043a\u0440\u0435\u0441\u0442\u0438\u043a\u0438 (X)</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0412\u0442\u043e\u0440\u043e\u0439 \u0438\u0433\u0440\u043e\u043a \u0441\u0442\u0430\u0432\u0438\u0442 \u043d\u043e\u043b\u0438\u043a\u0438 (O)</li></ul>\n"
"<ol start=\"3\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right"
                        ":0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u041f\u0435\u0440\u0432\u044b\u0439 \u0445\u043e\u0434 \u0434\u0435\u043b\u0430\u0435\u0442 \u0438\u0433\u0440\u043e\u043a, \u0438\u0433\u0440\u0430\u044e\u0449\u0438\u0439 \u043a\u0440\u0435\u0441\u0442\u0438\u043a\u0430\u043c\u0438</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0426\u0435\u043b\u044c \u0438\u0433\u0440\u044b: \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043b\u0438\u043d\u0438\u044e \u0438\u0437 \u0442\u0440\u0435\u0445 \u0441\u0432\u043e\u0438\u0445 \u0437\u043d\u0430\u043a\u043e\u0432</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt; font-weight:700;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-b"
                        "lock-indent:0; text-indent:0px;\"><span style=\" font-weight:400;\">\u043f\u043e \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u0438</span></li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u043f\u043e \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u0438</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u043f\u043e \u0434\u0438\u0430\u0433\u043e\u043d\u0430\u043b\u0438</li></ul>\n"
"<ol start=\"5\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0423\u0441\u043b\u043e\u0432\u0438\u044f \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438"
                        "\u044f \u0438\u0433\u0440\u044b:</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041f\u043e\u0431\u0435\u0434\u0430: \u043e\u0434\u0438\u043d \u0438\u0437 \u0438\u0433\u0440\u043e\u043a\u043e\u0432 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u043b \u043b\u0438\u043d\u0438\u044e \u0438\u0437 \u0442\u0440\u0435\u0445 \u0441\u0432\u043e\u0438\u0445 \u0437\u043d\u0430\u043a\u043e\u0432</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u041d\u0438\u0447\u044c\u044f: \u0432\u0441\u0435 \u043a\u043b\u0435\u0442\u043a\u0438 \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u044b, \u043d\u043e \u043d\u0438\u043a\u0442\u043e \u043d\u0435 \u043f\u043e\u0441\u0442\u0440\u043e\u0438\u043b"
                        " \u043b\u0438\u043d\u0438\u044e</li></ul>\n"
"<ol start=\"6\" style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">\u0417\u0430\u043f\u0440\u0435\u0449\u0435\u043d\u043e:</span></li></ol>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0442\u0430\u0432\u0438\u0442\u044c \u0437\u043d\u0430\u043a \u043d\u0430 \u0437\u0430\u043d\u044f\u0442\u0443\u044e \u043a\u043b\u0435\u0442\u043a\u0443</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0425\u043e"
                        "\u0434\u0438\u0442\u044c \u0432\u043d\u0435 \u0441\u0432\u043e\u0435\u0439 \u043e\u0447\u0435\u0440\u0435\u0434\u0438</li>\n"
"<li style=\" font-size:12pt;\" style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u0421\u0442\u0430\u0432\u0438\u0442\u044c \u0437\u043d\u0430\u043a \u0441\u043e\u043f\u0435\u0440\u043d\u0438\u043a\u0430</li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"about", None))
    # retranslateUi