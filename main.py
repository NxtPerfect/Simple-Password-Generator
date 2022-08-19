import random, os, sys
from PyQt5 import QtWidgets, QtGui

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

# Function to generate password, needs list of characters to use, length of the password
# and seed for randomizing
def get_password(chars: list, length: int, seed: int):
    password = ''
    random.seed(seed)
    for x in range(length):
        index = random.randint(0, (len(chars)-1))
        password += chars[index]
    return password

# Function to generate seed for pseudo random number generator
def get_seed(length: int):
    seed: int = 0
    for x in range(length):
        seed = random.randint(0, 9)
    return seed

##################################################################################################
##################################################################################################
##################################################################################################

class QLabel(QtWidgets.QDialog):
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
        self.capital_letters_toggle = QtWidgets.QPushButton(f'&%s' % (use_capital_letters),self)
        self.capital_letters_toggle.setCheckable(True)
        self.capital_letters_toggle.setChecked(False)
        self.capital_letters_toggle.clicked.connect(self.toggled)
        self.capital_letters_label.setBuddy(self.capital_letters_toggle)

        self.special_chars_label = QtWidgets.QLabel('&Use special characters:', self)
        self.special_chars_toggle = QtWidgets.QPushButton(f'&%s' % (use_special_chars),self)
        self.special_chars_toggle.setCheckable(True)
        self.special_chars_toggle.setChecked(False)
        self.special_chars_toggle.clicked.connect(self.toggled)
        self.special_chars_label.setBuddy(self.special_chars_toggle)
        
        self.numbers_label = QtWidgets.QLabel('&Use numbers:', self)
        self.numbers_toggle = QtWidgets.QPushButton(f'&%s' % (use_numbers),self)
        self.numbers_toggle.setCheckable(True)
        self.numbers_toggle.setChecked(False)
        self.numbers_toggle.clicked.connect(self.toggled)
        self.numbers_label.setBuddy(self.numbers_toggle)

        self.password_label = QtWidgets.QLabel('&Generated password:', self)

        btn_generate_password = QtWidgets.QPushButton('&Generate Password')
        btn_generate_password.clicked.connect(get_password(CHARS, length, get_seed(random.randint(0,16)) if 0 < length < 128 else self.password_label.setText('&Generated password: Password needs to be of length at least 1 and no more than 128',self)))
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

        main_layout.addWidget(btn_generate_password,4,1)
        main_layout.addWidget(btn_copy_to_clipboard,4,2)
        
        self.update()
        self.show()

    def toggled(self):
        if self.capital_letters_toggle.isChecked():
            use_capital_letters = True
        else:
            use_capital_letters = False
        if self.special_chars_toggle.isChecked():
            use_special_chars = True
        else:
            use_special_chars = False
        if self.numbers_toggle.isChecked():
            use_numbers = True
        else:
            use_numbers = False
        self.capital_letters_toggle.setText(f'&%s' % (use_capital_letters))
        self.special_chars_toggle.setText(f'&%s' % (use_special_chars))
        self.numbers_toggle.setText(f'&%s' % (use_numbers))

# Function to clear console after use put keyboard input after password was shown on the
# screen
#def clear_console():
#    command = 'clear'
#    if os.name in ('nt','dos'):
#        command = 'cls'
#    os.system(command)


# Main function where magic happens
def main():


    #Makes simple pyqt window
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    main = QLabel()
    sys.exit(app.exec())

    random.seed()
    while True:
        menu = "Welcome to Password Generator v%s\nPick your option:\n1. Generate password\n2. Change password length %s\n3. Include special characters %s\n4. Include capital letters %s\n5. Include numbers %s\n" % (VERSION, length, str(use_special_chars), str(use_capital_letters), str(use_numbers))
        choice = int(input(menu))
        match choice:
            case 1:
                password = get_password(CHARS, length, generate_seed(random.randint(0,16)))
                print(password)
                input()
                clear_console()
            case 2:
                while True:
                    length = int(input("How long should the password be?\t"))
                    if length != 0:
                        break
            case 3:
                if use_special_chars:
                    CHARS = list(set(CHARS) - set(SPECIAL_CHARACTERS))
                    use_special_chars = False
                    continue
                if SPECIAL_CHARACTERS not in CHARS:
                    CHARS += SPECIAL_CHARACTERS
                    use_special_chars = True
            case 4:
                if use_capital_letters:
                    CHARS = list(set(CHARS) - set(CAPITAL_LETTERS))
                    use_capital_letters = False
                    continue
                if CAPITAL_LETTERS not in CHARS:
                    CHARS += CAPITAL_LETTERS
                    use_capital_letters = True
            case 5:
                if use_numbers:
                    CHARS = list(set(CHARS) - set(NUMBERS))
                    use_numbers = False
                    continue
                if NUMBERS not in CHARS:
                    CHARS += NUMBERS
                    use_numbers = True

if __name__ == "__main__":
    main()
