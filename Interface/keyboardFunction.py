from PyQt6.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QHBoxLayout, \
    QSizePolicy, QMainWindow, QDialog, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QFont


# noinspection PyMethodMayBeStatic
class KeyboardWindow(QMainWindow):

    def __init__(self):
        super(KeyboardWindow, self).__init__()

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.setWindowTitle("Keyboard")
        self.setWindowIcon(QIcon("./icons/KEY.png"))
        screen_size = QApplication.primaryScreen().size()
        self.wndWidth = int(screen_size.width())
        self.wndHeight = int(9 * screen_size.height() / 20)
        self.setGeometry(0, int(screen_size.height() / 2), self.wndWidth,
                         self.wndHeight)

        self.is_tab_pressed = False
        self.is_capslock_pressed = False
        self.is_lshift_pressed = False
        self.is_rshift_pressed = False
        self.is_lctrl_pressed = False
        self.is_rctrl_pressed = False
        self.is_lalt_pressed = False
        self.is_ralt_pressed = False
        self.is_numlock_pressed = False

        self.line1_1 = QHBoxLayout()
        self.esc = KeyboardButton("Esc", self.esc_pressed)
        self.line1_1.addWidget(self.esc)
        self.F1 = KeyboardButton("F1", self.f1_pressed)
        self.line1_1.addWidget(self.F1)
        self.F2 = KeyboardButton("F2", self.f2_pressed)
        self.line1_1.addWidget(self.F2)
        self.F3 = KeyboardButton("F3", self.f3_pressed)
        self.line1_1.addWidget(self.F3)
        self.F4 = KeyboardButton("F4", self.f4_pressed)
        self.line1_1.addWidget(self.F4)
        self.F5 = KeyboardButton("F5", self.f5_pressed)
        self.line1_1.addWidget(self.F5)
        self.F6 = KeyboardButton("F6", self.f6_pressed)
        self.line1_1.addWidget(self.F6)
        self.F7 = KeyboardButton("F7", self.f7_pressed)
        self.line1_1.addWidget(self.F7)
        self.F8 = KeyboardButton("F8", self.f8_pressed)
        self.line1_1.addWidget(self.F8)
        self.F9 = KeyboardButton("F9", self.f9_pressed)
        self.line1_1.addWidget(self.F9)
        self.F10 = KeyboardButton("F10", self.f10_pressed)
        self.line1_1.addWidget(self.F10)
        self.F11 = KeyboardButton("F11", self.f11_pressed)
        self.line1_1.addWidget(self.F11)
        self.F12 = KeyboardButton("F12", self.f12_pressed)
        self.line1_1.addWidget(self.F12)

        self.line1_2 = QHBoxLayout()
        self.tilda = KeyboardButton("~\n' ё", self.tilda_pressed)
        self.line1_2.addWidget(self.tilda, 1)
        self.key1 = KeyboardButton("1\n!", self.key1_pressed)
        self.line1_2.addWidget(self.key1, 1)
        self.key2 = KeyboardButton("2\n\" @", self.key2_pressed)
        self.line1_2.addWidget(self.key2, 1)
        self.key3 = KeyboardButton("3\n№ #", self.key3_pressed)
        self.line1_2.addWidget(self.key3, 1)
        self.key4 = KeyboardButton("4\n$ ;", self.key4_pressed)
        self.line1_2.addWidget(self.key4, 1)
        self.key5 = KeyboardButton("5\n%", self.key5_pressed)
        self.line1_2.addWidget(self.key5, 1)
        self.key6 = KeyboardButton("6\n^ :", self.key6_pressed)
        self.line1_2.addWidget(self.key6, 1)
        self.key7 = KeyboardButton("7\n& ?", self.key7_pressed)
        self.line1_2.addWidget(self.key7, 1)
        self.key8 = KeyboardButton("8\n*", self.key8_pressed)
        self.line1_2.addWidget(self.key8, 1)
        self.key9 = KeyboardButton("9\n(", self.key9_pressed)
        self.line1_2.addWidget(self.key9, 1)
        self.key0 = KeyboardButton("0\n)", self.key0_pressed)
        self.line1_2.addWidget(self.key0, 1)
        self.minus = KeyboardButton("-\n_", self.minus_pressed)
        self.line1_2.addWidget(self.minus, 1)
        self.equal = KeyboardButton("=\n+", self.equal_pressed)
        self.line1_2.addWidget(self.equal, 1)
        self.backspace = KeyboardButton("Backspace", self.backspace_pressed)
        self.line1_2.addWidget(self.backspace, 2)

        self.line1_3 = QHBoxLayout()
        self.tab = KeyboardButton("Tab", self.tab_pressed)
        self.tab.setCheckable(True)
        self.line1_3.addWidget(self.tab, 2)
        self.q = KeyboardButton("Q\nЙ", self.q_pressed)
        self.line1_3.addWidget(self.q, 1)
        self.w = KeyboardButton("W\nЦ", self.w_pressed)
        self.line1_3.addWidget(self.w, 1)
        self.e = KeyboardButton("E\nУ", self.e_pressed)
        self.line1_3.addWidget(self.e, 1)
        self.r = KeyboardButton("R\nК", self.r_pressed)
        self.line1_3.addWidget(self.r, 1)
        self.t = KeyboardButton("T\nЕ", self.t_pressed)
        self.line1_3.addWidget(self.t, 1)
        self.y = KeyboardButton("Y\nН", self.y_pressed)
        self.line1_3.addWidget(self.y, 1)
        self.u = KeyboardButton("U\nГ", self.u_pressed)
        self.line1_3.addWidget(self.u, 1)
        self.i = KeyboardButton("I\nШ", self.i_pressed)
        self.line1_3.addWidget(self.i, 1)
        self.o = KeyboardButton("O\nЩ", self.o_pressed)
        self.line1_3.addWidget(self.o, 1)
        self.p = KeyboardButton("P\nЗ", self.p_pressed)
        self.line1_3.addWidget(self.p, 1)
        self.opensqbr = KeyboardButton("{ [\nХ", self.opensqbr_pressed)
        self.line1_3.addWidget(self.opensqbr, 1)
        self.closesqbr = KeyboardButton("} ]\nЪ", self.closesqbr_pressed)
        self.line1_3.addWidget(self.closesqbr, 1)
        self.backslash = KeyboardButton("\\\n| /", self.backslash_pressed)
        self.line1_3.addWidget(self.backslash, 1)

        self.line1_4 = QHBoxLayout()
        self.capslock = KeyboardButton("Caps Lock", self.capslock_pressed)
        self.capslock.setCheckable(True)
        self.line1_4.addWidget(self.capslock, 2)
        self.a = KeyboardButton("A\nФ", self.a_pressed)
        self.line1_4.addWidget(self.a, 1)
        self.s = KeyboardButton("S\nЫ", self.s_pressed)
        self.line1_4.addWidget(self.s, 1)
        self.d = KeyboardButton("D\nВ", self.d_pressed)
        self.line1_4.addWidget(self.d, 1)
        self.d = KeyboardButton("D\nВ", self.d_pressed)
        self.line1_4.addWidget(self.d, 1)
        self.f = KeyboardButton("F\nА", self.f_pressed)
        self.line1_4.addWidget(self.f, 1)
        self.g = KeyboardButton("G\nП", self.g_pressed)
        self.line1_4.addWidget(self.g, 1)
        self.h = KeyboardButton("H\nР", self.h_pressed)
        self.line1_4.addWidget(self.h, 1)
        self.j = KeyboardButton("J\nО", self.j_pressed)
        self.line1_4.addWidget(self.j, 1)
        self.k = KeyboardButton("K\nЛ", self.k_pressed)
        self.line1_4.addWidget(self.k, 1)
        self.l = KeyboardButton("L\nД", self.l_pressed)
        self.line1_4.addWidget(self.l, 1)
        self.semicolon = KeyboardButton(": ;\nЖ", self.semicolon_pressed)
        self.line1_4.addWidget(self.semicolon, 1)
        self.quotes = KeyboardButton("\" \'\nЭ", self.quotes_pressed)
        self.line1_4.addWidget(self.quotes, 1)
        self.enter = KeyboardButton("Enter", self.enter_pressed)
        self.line1_4.addWidget(self.enter, 2)

        self.line1_5 = QHBoxLayout()
        self.lshift = KeyboardButton("Shift", self.lshift_pressed)
        self.lshift.setCheckable(True)
        self.line1_5.addWidget(self.lshift, 2)
        self.z = KeyboardButton("Z\nЯ", self.z_pressed)
        self.line1_5.addWidget(self.z, 1)
        self.x = KeyboardButton("X\nЧ", self.x_pressed)
        self.line1_5.addWidget(self.x, 1)
        self.c = KeyboardButton("C\nС", self.c_pressed)
        self.line1_5.addWidget(self.c, 1)
        self.v = KeyboardButton("V\nМ", self.v_pressed)
        self.line1_5.addWidget(self.v, 1)
        self.b = KeyboardButton("B\nИ", self.b_pressed)
        self.line1_5.addWidget(self.b, 1)
        self.n = KeyboardButton("N\nТ", self.n_pressed)
        self.line1_5.addWidget(self.n, 1)
        self.m = KeyboardButton("M\nЬ", self.m_pressed)
        self.line1_5.addWidget(self.m, 1)
        self.comma = KeyboardButton("< ,\nБ", self.comma_pressed)
        self.line1_5.addWidget(self.comma, 1)
        self.dot = KeyboardButton("> .\nЮ", self.dot_pressed)
        self.line1_5.addWidget(self.dot, 1)
        self.slash = KeyboardButton("? /\n, .", self.slash_pressed)
        self.line1_5.addWidget(self.slash, 1)
        self.uparrow = KeyboardButton("↑", self.uparrow_pressed)
        self.line1_5.addWidget(self.uparrow, 1)
        self.rshift = KeyboardButton("Shift", self.rshift_pressed)
        self.rshift.setCheckable(True)
        self.line1_5.addWidget(self.rshift, 2)

        self.line1_6 = QHBoxLayout()
        self.lctrl = KeyboardButton("Ctrl", self.lctrl_pressed)
        self.lctrl.setCheckable(True)
        self.line1_6.addWidget(self.lctrl, 1)
        self.win = KeyboardButton("Win", self.win_pressed)
        self.line1_6.addWidget(self.win, 1)
        self.lalt = KeyboardButton("Alt", self.lalt_pressed)
        self.lalt.setCheckable(True)
        self.line1_6.addWidget(self.lalt, 1)
        self.space = KeyboardButton("Space", self.space_pressed)
        self.line1_6.addWidget(self.space, 5)
        self.ralt = KeyboardButton("Alt", self.ralt_pressed)
        self.ralt.setCheckable(True)
        self.line1_6.addWidget(self.ralt, 1)
        self.rctrl = KeyboardButton("Ctrl", self.rctrl_pressed)
        self.rctrl.setCheckable(True)
        self.line1_6.addWidget(self.rctrl, 1)
        self.leftarrow = KeyboardButton("←", self.leftarrow_pressed)
        self.line1_6.addWidget(self.leftarrow, 1)
        self.downarrow = KeyboardButton("↓", self.downarrow_pressed)
        self.line1_6.addWidget(self.downarrow, 1)
        self.rightarrow = KeyboardButton("→", self.rightarrow_pressed)
        self.line1_6.addWidget(self.rightarrow, 1)

        self.line2_1 = QHBoxLayout()
        self.numasterisk = KeyboardButton("*", self.numasterisk_pressed)
        self.line2_1.addWidget(self.numasterisk, 1)
        self.numslash = KeyboardButton("/", self.numslash_pressed)
        self.line2_1.addWidget(self.numslash, 1)
        self.numprtsc = KeyboardButton("PrtSc", self.prtsc_pressed)
        self.line2_1.addWidget(self.numprtsc, 1)

        self.line2_2 = QHBoxLayout()
        self.numplus = KeyboardButton("+", self.numplus_pressed)
        self.line2_2.addWidget(self.numplus, 1)
        self.numminus = KeyboardButton("-", self.numminus_pressed)
        self.line2_2.addWidget(self.numminus, 1)
        self.numlock = KeyboardButton("NumLk", self.numlock_pressed)
        self.numlock.setCheckable(True)
        self.line2_2.addWidget(self.numlock, 1)

        self.line2_3 = QHBoxLayout()
        self.num7 = KeyboardButton("7\nHome", self.num7_pressed)
        self.line2_3.addWidget(self.num7, 1)
        self.num8 = KeyboardButton("8\n↑", self.num8_pressed)
        self.line2_3.addWidget(self.num8, 1)
        self.num9 = KeyboardButton("9\nPgUp", self.num9_pressed)
        self.line2_3.addWidget(self.num9, 1)

        self.line2_4 = QHBoxLayout()
        self.num4 = KeyboardButton("4\n←", self.num4_pressed)
        self.line2_4.addWidget(self.num4, 1)
        self.num5 = KeyboardButton("5", self.num5_pressed)
        self.line2_4.addWidget(self.num5, 1)
        self.num6 = KeyboardButton("6\n→", self.num6_pressed)
        self.line2_4.addWidget(self.num6, 1)

        self.line2_5 = QHBoxLayout()
        self.num1 = KeyboardButton("1\nEnd", self.num1_pressed)
        self.line2_5.addWidget(self.num1, 1)
        self.num2 = KeyboardButton("2\n↓", self.num2_pressed)
        self.line2_5.addWidget(self.num2, 1)
        self.num3 = KeyboardButton("3\nPgDn", self.num3_pressed)
        self.line2_5.addWidget(self.num3, 1)

        self.line2_6 = QHBoxLayout()
        self.num0 = KeyboardButton("0\nInsert", self.num0_pressed)
        self.line2_6.addWidget(self.num0, 1)
        self.numdot = KeyboardButton(".\nDelete", self.numdot_pressed)
        self.line2_6.addWidget(self.numdot, 1)
        self.numenter = KeyboardButton("Enter", self.numenter_pressed)
        self.line2_6.addWidget(self.numenter, 1)

        self.areas_layout = QHBoxLayout()
        self.main_area = QVBoxLayout()
        self.main_area.addLayout(self.line1_1)
        self.main_area.addLayout(self.line1_2)
        self.main_area.addLayout(self.line1_3)
        self.main_area.addLayout(self.line1_4)
        self.main_area.addLayout(self.line1_5)
        self.main_area.addLayout(self.line1_6)
        self.areas_layout.addLayout(self.main_area)

        self.num_area = QVBoxLayout()
        self.num_area.addLayout(self.line2_1)
        self.num_area.addLayout(self.line2_2)
        self.num_area.addLayout(self.line2_3)
        self.num_area.addLayout(self.line2_4)
        self.num_area.addLayout(self.line2_5)
        self.num_area.addLayout(self.line2_6)
        self.areas_layout.addLayout(self.num_area)

        self.user_area = QVBoxLayout()
        self.user_buttons = []
        self.user_buttons_names = ["Кушать", "Спать", "Ванная комната"]
        self.user_buttons_functions = (self.user_function1, self.user_function2, self.user_function3,
                                       self.user_function4, self.user_function5, self.user_function6,
                                       self.user_function7, self.user_function8)
        self.user_buttons_connections = {}
        for button_name in self.user_buttons_names:
            self.user_buttons.append(QPushButton(button_name))
            self.user_buttons[len(self.user_buttons) - 1].setSizePolicy(QSizePolicy.Policy.Expanding,
                                                                        QSizePolicy.Policy.Expanding)
            self.user_buttons[len(self.user_buttons) - 1].setFont(QFont('Tahoma', 13))
            self.user_buttons[len(self.user_buttons) - 1].pressed.connect(
                self.user_buttons_functions[len(self.user_buttons) - 1])
            self.user_buttons_connections[button_name] = self.user_buttons_functions[len(self.user_buttons) - 1]
            self.user_area.addWidget(self.user_buttons[len(self.user_buttons) - 1])

        self.user_buttons.append(QPushButton("..."))
        self.user_buttons[len(self.user_buttons) - 1].setSizePolicy(QSizePolicy.Policy.Expanding,
                                                                    QSizePolicy.Policy.Expanding)
        self.user_buttons[len(self.user_buttons) - 1].setFont(QFont('Tahoma', 20))
        self.user_buttons[len(self.user_buttons) - 1].pressed.connect(self.add_user_button)
        self.user_area.addWidget(self.user_buttons[len(self.user_buttons) - 1])
        self.user_buttons_amount = 4
        self.areas_layout.addLayout(self.user_area)

        widget = QWidget()
        widget.setLayout(self.areas_layout)
        self.setCentralWidget(widget)

    def esc_pressed(self):
        print('esc')

    def f1_pressed(self):
        print('F1')

    def f2_pressed(self):
        print('F2')

    def f3_pressed(self):
        print('F3')

    def f4_pressed(self):
        print('F4')

    def f5_pressed(self):
        print('F5')

    def f6_pressed(self):
        print('F6')

    def f7_pressed(self):
        print('F7')

    def f8_pressed(self):
        print('F8')

    def f9_pressed(self):
        print('F9')

    def f10_pressed(self):
        print('F10')

    def f11_pressed(self):
        print('F11')

    def f12_pressed(self):
        print('F12')

    def tilda_pressed(self):
        print('~')

    def key1_pressed(self):
        print('1')

    def key2_pressed(self):
        print('2')

    def key3_pressed(self):
        print('3')

    def key4_pressed(self):
        print('4')

    def key5_pressed(self):
        print('5')

    def key6_pressed(self):
        print('6')

    def key7_pressed(self):
        print('7')

    def key8_pressed(self):
        print('8')

    def key9_pressed(self):
        print('9')

    def key0_pressed(self):
        print('0')

    def minus_pressed(self):
        print('-')

    def equal_pressed(self):
        print('=')

    def backspace_pressed(self):
        print('backspace')

    def tab_pressed(self):
        if self.tab.isChecked():
            self.is_tab_pressed = False
            print('tab released')
        else:
            self.is_tab_pressed = True
            print('tab pressed')

    def q_pressed(self):
        print('q')

    def w_pressed(self):
        print('w')

    def e_pressed(self):
        print('e')

    def r_pressed(self):
        print('r')

    def t_pressed(self):
        print('t')

    def y_pressed(self):
        print('y')

    def u_pressed(self):
        print('u')

    def i_pressed(self):
        print('i')

    def o_pressed(self):
        print('o')

    def p_pressed(self):
        print('p')

    def opensqbr_pressed(self):
        print('[')

    def closesqbr_pressed(self):
        print(']')

    def backslash_pressed(self):
        print('\\')

    def capslock_pressed(self):
        if self.capslock.isChecked():
            self.is_capslock_pressed = False
            print('capslock released')
        else:
            self.is_capslock_pressed = True
            print('capslock pressed')

    def a_pressed(self):
        print('a')

    def s_pressed(self):
        print('s')

    def d_pressed(self):
        print('d')

    def f_pressed(self):
        print('f')

    def g_pressed(self):
        print('g')

    def h_pressed(self):
        print('h')

    def j_pressed(self):
        print('j')

    def k_pressed(self):
        print('k')

    def l_pressed(self):
        print('l')

    def semicolon_pressed(self):
        print(';')

    def quotes_pressed(self):
        print('"')

    def enter_pressed(self):
        print('enter pressed')

    def lshift_pressed(self):
        if self.lshift.isChecked():
            self.is_lshift_pressed = False
            print('lshift released')
        else:
            self.is_lshift_pressed = True
            print('lshift pressed')

    def z_pressed(self):
        print('z')

    def x_pressed(self):
        print('x')

    def c_pressed(self):
        print('c')

    def v_pressed(self):
        print('v')

    def b_pressed(self):
        print('b')

    def n_pressed(self):
        print('n')

    def m_pressed(self):
        print('m')

    def comma_pressed(self):
        print(',')

    def dot_pressed(self):
        print('.')

    def slash_pressed(self):
        print('/')

    def uparrow_pressed(self):
        print("↑")

    def rshift_pressed(self):
        if self.rshift.isChecked():
            self.is_rshift_pressed = False
            print('rshift released')
        else:
            self.is_rshift_pressed = True
            print('rshift pressed')

    def lctrl_pressed(self):
        if self.lctrl.isChecked():
            self.is_lctrl_pressed = False
            print('lctrl released')
        else:
            self.is_lctrl_pressed = True
            print('lctrl pressed')

    def win_pressed(self):
        print('windows pressed')

    def lalt_pressed(self):
        if self.lalt.isChecked():
            self.is_lalt_pressed = False
            print('lalt released')
        else:
            self.is_lalt_pressed = True
            print('lalt pressed')

    def space_pressed(self):
        print('space pressed')

    def rctrl_pressed(self):
        if self.rctrl.isChecked():
            self.is_rctrl_pressed = False
            print('rctrl released')
        else:
            self.is_rctrl_pressed = True
            print('rctrl pressed')

    def ralt_pressed(self):
        if self.ralt.isChecked():
            self.is_ralt_pressed = False
            print('ralt released')
        else:
            self.is_ralt_pressed = True
            print('ralt pressed')

    def leftarrow_pressed(self):
        print("←")

    def downarrow_pressed(self):
        print("↓")

    def rightarrow_pressed(self):
        print("→")

    def numasterisk_pressed(self):
        print('num *')

    def numslash_pressed(self):
        print('num /')

    def prtsc_pressed(self):
        print('Print Screen clicked')

    def numplus_pressed(self):
        print('num +')

    def numminus_pressed(self):
        print('num -')

    def numlock_pressed(self):
        if self.numlock.isChecked():
            self.is_numlock_pressed = False
            print('numlock released')
        else:
            self.is_numlock_pressed = True
            print('numlock pressed')

    def num7_pressed(self):
        print('num 7')

    def num8_pressed(self):
        print('num 8')

    def num9_pressed(self):
        print('num 9')

    def num4_pressed(self):
        print('num 4')

    def num5_pressed(self):
        print('num 5')

    def num6_pressed(self):
        print('num 6')

    def num1_pressed(self):
        print('num 1')

    def num2_pressed(self):
        print('num 2')

    def num3_pressed(self):
        print('num 3')

    def num0_pressed(self):
        print('num 0')

    def numdot_pressed(self):
        print('num .')

    def numenter_pressed(self):
        print('num enter')

    def user_function1(self):
        print('pressed 1')

    def user_function2(self):
        print('pressed 2')

    def user_function3(self):
        print('pressed 3')

    def user_function4(self):
        print('pressed 4')

    def user_function5(self):
        print('pressed 5')

    def user_function6(self):
        print('pressed 6')

    def user_function7(self):
        print('pressed 7')

    def user_function8(self):
        print('pressed 8')

    def add_user_button(self):
        choosedlg = ChooseDialog()
        result = choosedlg.exec()
        if result is 1:
            if self.user_buttons_amount > 8:
                return 0
            namedlg = NameDialog()
            name = namedlg.exec()
            self.user_buttons_names.append(str(name))
            new_button = QPushButton(str(name))
            new_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            new_button.setFont(QFont('Tahoma', 13))
            free = [f for f in self.user_buttons_functions if f not in self.user_buttons_connections.values()]
            new_button.clicked.connect(free[0])
            self.user_buttons_connections[str(name)] = free[0]
            self.user_buttons.insert(len(self.user_buttons) - 1, new_button)
            self.user_area.removeWidget(self.user_buttons[-1])
            self.user_area.addWidget(new_button)
            self.user_area.addWidget(self.user_buttons[-1])
            self.user_buttons_amount += 1
        elif result is -1:
            namedlg = NameDialog()
            name = namedlg.exec()
            if str(name) in self.user_buttons_names:
                self.user_area.removeWidget(self.user_buttons[self.user_buttons_names.index(str(name))])
                self.user_buttons.pop(self.user_buttons_names.index(str(name)))
                self.user_buttons_connections.pop(str(name))
                self.user_buttons_names.remove(str(name))
                self.user_buttons_amount -= 1


class KeyboardButton(QPushButton):
    def __init__(self, name, connect_function):
        super().__init__(name)
        self.setFont(QFont('Tahoma', 13))
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.clicked.connect(connect_function)


class ChooseDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Выберите действие")
        screen_size = QApplication.primaryScreen().size()
        self.dialogWidth = int(2 * screen_size.width() / 5)
        self.dialogHeight = int(screen_size.height() / 5)
        self.setGeometry(int(3*screen_size.width() / 10), int(screen_size.height() / 5), self.dialogWidth,
                         self.dialogHeight)

        self.addButton = QPushButton("Добавить\nкнопку")
        self.addButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.addButton.setFont(QFont('Tahoma', 20))
        self.deleteButton = QPushButton("Удалить\nкнопку")
        self.deleteButton.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.deleteButton.setFont(QFont('Tahoma', 20))
        self.addButton.clicked.connect(lambda: self.done(1))
        self.deleteButton.clicked.connect(lambda: self.done(-1))

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.deleteButton)
        self.setLayout(self.layout)


class NameDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Введите имя кнопки")
        screen_size = QApplication.primaryScreen().size()
        self.dialogWidth = int(2 * screen_size.width() / 5)
        self.dialogHeight = int(screen_size.height() / 5)
        self.setGeometry(int(3*screen_size.width() / 10), int(screen_size.height() / 5), self.dialogWidth,
                         self.dialogHeight)

        self.edit = QLineEdit()
        self.edit.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.edit.setFont(QFont('Tahoma', 20))
        self.OKButton = QPushButton("ОК")
        self.OKButton.setFont(QFont('Tahoma', 20))
        self.OKButton.clicked.connect(lambda: self.done(1))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.edit, 1)
        self.layout.addWidget(self.OKButton, 2)
        self.setLayout(self.layout)

    def exec(self):
        ok = super().exec()
        if ok:
            return self.edit.text()
