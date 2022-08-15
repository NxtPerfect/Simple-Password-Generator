import random, os, sys
from PyQt5 import QtWidgets,QtGui

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
def generate_seed(length: int):
    seed: int = 0
    for x in range(length):
        seed = random.randint(0, 9)
    return seed

# Function to clear console after use put keyboard input after password was shown on the
# screen
def clear_console():
    command = 'clear'
    if os.name in ('nt','dos'):
        command = 'cls'
    os.system(command)


# Main function where magic happens
def main():
    #Makes simple pyqt window
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    
    w.setWindowTitle('Simple Password Generator PyQt')
    # after there actually is an icon to show
    #w.setWindowIcon(QtGui.QIcon('icon.png'))
    layout = QtWidgets.QHBoxLayout()
    btn = QtWidgets.QPushButton("Hello")
    layout.addWidget(btn)
    w.setLayout(layout)
    w.resize(500,500)
    w.move(0,0)
    w.show()
    sys.exit(app.exec_())

    random.seed()
    length = 5
    use_special_chars = False
    use_capital_letters = False
    use_numbers = False
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
