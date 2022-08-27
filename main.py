import random, sys
from PyQt5 import QtWidgets, QtGui

##################################################################################################
##################################################################################################
##################################################################################################

class QLabel(QtWidgets.QDialog):
# Standard array that we use to create password from
    CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
# Lowercase letters array
    LOWERCASE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k',
                         'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
# Capital letters array
    CAPITAL_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
                       'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'V', 'X', 'Y', 'Z']
# Special characters array
    SPECIAL_CHARACTERS = ['~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',':',';','/','<','>','.','?','`']
# Numbers array
    NUMBERS = ['1','2','3','4','5','6','7','8','9','0']
# Version number
    VERSION = '0.1.0'

    length = 5
    use_special_chars = False
    use_capital_letters = False
    use_numbers = False

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Simple Password Generator PyQt5')
        self.setFixedWidth(400)

        self.length_label = QtWidgets.QLabel('&Password length:', self)
        self.length_line_edit = QtWidgets.QLineEdit(self)
        self.length_label.setBuddy(self.length_line_edit)

        self.capital_letters_label = QtWidgets.QLabel('&Use capital letters:', self)
        self.capital_letters_toggle = QtWidgets.QPushButton(f'&%s' % (self.use_capital_letters),self)
        self.capital_letters_toggle.setCheckable(True)
        self.capital_letters_toggle.setChecked(False)
        self.capital_letters_toggle.clicked.connect(self.toggled)
        self.capital_letters_label.setBuddy(self.capital_letters_toggle)

        self.special_chars_label = QtWidgets.QLabel('&Use special characters:', self)
        self.special_chars_toggle = QtWidgets.QPushButton(f'&%s' % (self.use_special_chars),self)
        self.special_chars_toggle.setCheckable(True)
        self.special_chars_toggle.setChecked(False)
        self.special_chars_toggle.clicked.connect(self.toggled)
        self.special_chars_label.setBuddy(self.special_chars_toggle)

        self.numbers_label = QtWidgets.QLabel('&Use numbers:', self)
        self.numbers_toggle = QtWidgets.QPushButton(f'&%s' % (self.use_numbers),self)
        self.numbers_toggle.setCheckable(True)
        self.numbers_toggle.setChecked(False)
        self.numbers_toggle.clicked.connect(self.toggled)
        self.numbers_label.setBuddy(self.numbers_toggle)

        self.password = '' #get_password(CHARS, length, get_seed(16)) 
        self.password_label = QtWidgets.QLabel('Generated password: %s' %
                                               (self.password), self)

        btn_generate_password = QtWidgets.QPushButton('&Generate Password')
        btn_generate_password.clicked.connect(self.show_password)
        btn_copy_to_clipboard = QtWidgets.QPushButton('&Copy to Clipboard')

        main_layout = QtWidgets.QGridLayout(self)
        main_layout.addWidget(self.length_label, 0,0)
        main_layout.addWidget(self.length_line_edit,0,1,1,2)

        main_layout.addWidget(self.capital_letters_label)
        main_layout.addWidget(self.capital_letters_toggle,1,1,1,2)

        main_layout.addWidget(self.special_chars_label)
        main_layout.addWidget(self.special_chars_toggle,2,1,1,2)

        main_layout.addWidget(self.numbers_label)
        main_layout.addWidget(self.numbers_toggle,3,1,1,2)

        main_layout.addWidget(self.password_label)

        main_layout.addWidget(btn_generate_password,5,1)
        main_layout.addWidget(btn_copy_to_clipboard,5,2)

        self.update()
        self.show()

    def toggled(self):
        if self.capital_letters_toggle.isChecked():
            self.use_capital_letters = True
            self.CHARS += self.CAPITAL_LETTERS
        else:
            self.use_capital_letters = False
            if self.CAPITAL_LETTERS in self.CHARS:
                self.CHARS = list(set(self.CHARS) - set(self.CAPITAL_LETTERS))
        if self.special_chars_toggle.isChecked():
            self.use_special_chars = True
            self.CHARS += self.SPECIAL_CHARACTERS
        else:
            self.use_special_chars = False
            if self.SPECIAL_CHARACTERS in self.CHARS:
                self.CHARS = list(set(self.CHARS) - set(self.SPECIAL_CHARACTERS))
        if self.numbers_toggle.isChecked():
            self.use_numbers = True
            self.CHARS += self.NUMBERS
        else:
            self.use_numbers = False
            if self.NUMBERS in self.CHARS:
                self.CHARS = list(set(self.CHARS) - set(self.NUMBERS))
        self.capital_letters_toggle.setText(f'&%s' % (self.use_capital_letters))
        self.special_chars_toggle.setText(f'&%s' % (self.use_special_chars))
        self.numbers_toggle.setText(f'&%s' % (self.use_numbers))

    def show_password(self):
        passw = get_password(self.CHARS, self.length)
        print(passw)
        self.password_label.setText('Generated password: %s' %
                                    (passw))
        

# Function to generate password, needs list of characters to use, length of the password
# and seed for randomizing
def get_password(chars: list, length: int):
    password = ''
    #random.seed(seed)
    for x in range(length):
        index = random.randint(0, (len(chars)-1))
        password += chars[index]
    return password

# Function to generate seed for pseudo random number generator
def get_seed(length: int):
    seed = 0
    for x in range(length):
        seed = random.randint(0, 9)
    return seed

##################################################################################################
##################################################################################################
##################################################################################################

# Main function where magic happens
def main():
    random.seed()
    #Makes simple pyqt window
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    main = QLabel()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
