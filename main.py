from form import *

from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtGui import QTextCursor, QImage, QTextImageFormat, QTextOption
from PySide6.QtCore import QSize
from PySide6 import * # type: ignore
import sys
from res import *
from utils import *
from math import *

class Window(QMainWindow):
    # Стартовые настройки (инициализация)
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.area = [[button() for j in range(3)] for i in range(3)]
        self.type_of_tag = "close"
        self.icon_close = QIcon(resource_path("icons/close.svg"))
        self.icon_circle =QIcon(resource_path("icons/circle.svg"))
        self.setWindowIcon(QIcon(resource_path("icons/main.ico")))
        self.list_of_buttons = [
            self.ui.button11, self.ui.button12, self.ui.button13,
            self.ui.button21, self.ui.button22, self.ui.button23,
            self.ui.button31, self.ui.button32, self.ui.button33,
        ]
        self.make_buttons_enabled(True)
        # Настройки окна
        self.setWindowState(Qt.WindowNoState)
        self.setWindowFlags(
            self.windowFlags() | 
            Qt.WindowMaximizeButtonHint |
            Qt.CustomizeWindowHint |
            Qt.WindowTitleHint |
            Qt.WindowSystemMenuHint |
            Qt.WindowMinimizeButtonHint |
            Qt.WindowCloseButtonHint
        )
        self.depth = 0
        self.is_game_with_bot = False
        self.ui.tabWidget.tabBar().hide()
        self.ui.result_button.setEnabled(False)
        self.ui.button_circle.setEnabled(False)
        self.ui.button_close.setEnabled(False)
        self.ui.button_restart.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.add_functions()

    #Подключение конпок 
    def add_functions(self):
        for button in self.list_of_buttons:
            button.clicked.connect(lambda ch, b=button: self.check_clicks(b))
        self.ui.play_with_friend.clicked.connect(lambda:self.get_in_page_play())
        self.ui.button_restart.clicked.connect(lambda:self.restart_game())
        self.ui.button_about.clicked.connect(lambda:self.get_in_page_about())
        self.ui.play_with_bot.clicked.connect(lambda:self.play_game_with_bot_start_settings())

    # Игра друг с другом
    def check_clicks(self, button):
        position = get_position(button.objectName())
        types = self.type_of_tag
        for i in range(3):
            for j in range(3):
                if i == position[0] and j == position[1]:
                    if not self.area[i][j].clicked:
                        self.make_move(i, j, button)
                        # self.area[i][j].clicked = True
                        # self.area[i][j].type = self.type_of_tag
                        # self.change_type_of_tag(button)
                        # if types=="circle":
                        #     self.change_type_of_button(self.ui.button_close, self.ui.button_circle)
                            
                        # else:
                        #     self.change_type_of_button(self.ui.button_circle, self.ui.button_close)

                        # type_of_winner, win_list = self.type_of_winner()
                        # if type_of_winner:
                        #     self.make_winner(win_list)
                        # elif self.check_draw():
                        #     self.make_draw()
                            
    #Ход    
    def make_move(self, row, col, button):
        self.area[row][col].clicked = True
        self.area[row][col].type = self.type_of_tag
        self.change_type_of_tag(button)
        button.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        if self.type_of_tag=="close":
            self.change_type_of_button(self.ui.button_close, self.ui.button_circle)                  
        else:
            self.change_type_of_button(self.ui.button_circle, self.ui.button_close)
        type_of_winner, win_list = self.type_of_winner()
        if type_of_winner:
            self.make_winner(win_list)
        elif self.check_draw():
            self.make_draw()
        if self.is_game_with_bot:
            if self.type_of_tag=="circle":
                self.make_buttons_enabled(True)
            QTimer.singleShot(1000, lambda:self.play_game_with_bot())

    # Изменение стиля кнопок
    def change_type_of_button(self, button1, button2):
        button1.setStyleSheet("background-color:rgb(179, 255, 131);")  
        button2.setStyleSheet("background-color:rgb(151, 255, 198);")   

    # Одинаковый стиль кнопок
    def make_same_type_of_buttons(self, button1, button2):
        button1.setStyleSheet("background-color:rgb(151, 255, 198);")  
        button2.setStyleSheet("background-color:rgb(151, 255, 198);") 
          
    # Смена хода
    def change_type_of_tag(self, button):
        if self.type_of_tag=="close":
            button.setIcon(self.icon_close)
            self.type_of_tag = "circle"
        else:
            button.setIcon(self.icon_circle)
            self.type_of_tag = "close"

    # Проверка комбинаций
    def check_combination(self, lists):
        types = self.area[lists[0][0]][lists[0][1]].type
        for i in range(1, len(lists)):
            if self.area[lists[i][0]][lists[i][1]].type !=types or not types:
                return False
        return True
    
    # Получение возможных ходов
    def get_possible_moves(self):
        possible_moves = [] 
        for i in range(3):
            for j in range(3):
                if not self.area[i][j].type:
                    possible_moves.append([i,j])
        return possible_moves
    
    # Поиск выигрышной комбинации
    def check_win_combination(self):
        for i in range(len(win_combinations_dict)):
            if self.check_combination(win_combinations_dict[i]):
                return win_combinations_dict[i]
        return []
    
    # Поиск победителя
    def type_of_winner(self):
        win_list = self.check_win_combination()
        if not win_list:
            return None, None
        row = win_list[0][0]
        col = win_list[0][1]
        return self.area[row][col].type, win_list
    
    # Отображение победителя
    def make_winner(self, lists):
        lists_of_name = []
        for i in range(len(lists)):
            name_of_button = get_key(lists[i])
            for button in self.list_of_buttons:
                if button.objectName() == name_of_button:
                    button.setStyleSheet("background-color:#39ac33; border:none;")
                    lists_of_name.append(name_of_button)
        self.make_win_label("Winner", True)
        self.make_buttons_uncklicked(lists_of_name)
        self.make_same_type_of_buttons(self.ui.button_circle, self.ui.button_close)
        self.make_buttons_enabled(True)

    # Проверка ничьи
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if not self.area[i][j].type:
                    return False
        return True
    
    # Отображение ничьи
    def make_draw(self):
        self.make_win_label("Draw", False)
        self.make_same_type_of_buttons(self.ui.button_circle, self.ui.button_close)
        self.make_buttons_enabled(True)
    
    # Поиск конпки по ее имени
    def get_button_by_name(self, name):
        for button in self.list_of_buttons:
            if button.objectName() == name:
                return button
    
    # Алгорит минимакс
    def minimax(self, depth, is_maxplayer):
        winner = self.type_of_winner()[0]
        if winner =="circle":
            return 1, None
        elif winner == "close":
            return -1, None
        else:
            if self.check_draw():
                return 0, None
        if is_maxplayer:
            best_move = None
            best_score = float('-inf')
            possible_moves = self.get_possible_moves()
            # print(possible_moves)
            for move in possible_moves:
                self.area[move[0]][move[1]].type = "circle"
                eval, _  = self.minimax(depth+1, False)
                self.area[move[0]][move[1]].type = None
                if eval> best_score:
                    best_score = eval
                    best_move = move
            return best_score, best_move
        else:
            best_move = None
            best_score = float('inf')
            possible_moves = self.get_possible_moves()
            for move in possible_moves:
                self.area[move[0]][move[1]].type = "close"
                eval, _  = self.minimax(depth+1, True)
                self.area[move[0]][move[1]].type = None
                if eval< best_score:
                    best_score = eval
                    best_move = move
            return best_score, best_move
        
    # Игра с ботом
    def play_game_with_bot(self):
        # print(self.type_of_tag)
        if self.type_of_tag=="circle":
            # self.make_buttons_enabled(True)
            best_move = None
            _, best_move = self.minimax(self.depth, True)
            # print(best_move)
            if best_move:
                button = self.get_button_by_name(f"button{best_move[0]+1}{best_move[1]+1}")
                self.make_move(best_move[0], best_move[1], button)
        else:
            self.make_buttons_enabled(False)

    # Настройки

    def play_game_with_bot_start_settings(self):
        self.ui.button_restart.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.is_game_with_bot = True
        self.make_buttons_enabled(False)
        self.ui.play_with_friend.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.play_game_with_bot()

    def play_game_with_friends_start_settings(self):
        self.ui.button_restart.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.is_game_with_bot = False
        self.ui.play_with_bot.setAttribute(Qt.WA_TransparentForMouseEvents, True)
        self.make_buttons_enabled(False)


    def make_buttons_uncklicked(self, list_of_clicked_name):
        for button in self.list_of_buttons:
            if button.objectName() not in list_of_clicked_name:
                button.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    def make_win_label(self, string, flag):
        self.ui.result_frame.setStyleSheet("background-color:rgb(0,0,0); color:(255,255,255); border-radius:5px;border:none;")
        self.ui.result_label.setStyleSheet("background-color:rgb(0,0,0); color:rgb(255, 255, 255); border-radius:7px; font-size:24px;")
        self.ui.result_label.setText(string)
        if flag:
            if self.type_of_tag=="circle":
                self.ui.result_button.setIcon(self.icon_close)
            else:
                self.ui.result_button.setIcon(self.icon_circle)
        self.ui.result_button.setStyleSheet("background-color:rgb(0,0,0);border:none;")

    def clear_area_to_restart(self):
        for i in range(3):
            for j in range(3):
                self.area[i][j].type = None
                self.area[i][j].clicked = False

    def make_buttons_enabled(self, flag):
        for button in self.list_of_buttons:
            button.setAttribute(Qt.WA_TransparentForMouseEvents, flag)

    def restart_game(self):
        self.make_buttons_enabled(True)
        self.ui.play_with_friend.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.ui.play_with_bot.setAttribute(Qt.WA_TransparentForMouseEvents, False)
        self.type_of_tag = "close"
        self.ui.result_frame.setStyleSheet("background-color:rgb(52,52,52); color:(255,255,255); border-radius:5px;border:none;")
        self.clear_area_to_restart()
        for button in self.list_of_buttons:
            button.setIcon(QIcon())
            button.setStyleSheet(u"background-color:rgb(148, 146, 141);\n" "border: 1px solid rgb(31, 31, 31);\n" "")
        self.make_buttons_enabled(True)
        self.ui.result_button.setIcon(QIcon())
        self.ui.result_button.setStyleSheet(u"background-color:rgb(52,52,52);\n" "border:none;")
        self.ui.result_label.setText("")
        self.ui.result_label.setStyleSheet("background-color:none")
        self.make_same_type_of_buttons(self.ui.button_circle, self.ui.button_close)
        self.ui.button_restart.setAttribute(Qt.WA_TransparentForMouseEvents, False)

    def get_in_page_about(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab_2)
    def get_in_page_play(self):
        self.ui.tabWidget.setCurrentWidget(self.ui.tab)
        self.play_game_with_friends_start_settings()

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())