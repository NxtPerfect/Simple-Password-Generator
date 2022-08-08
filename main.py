import random

# two underscores in class make method/variable private

CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k',
         'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
LOWERCASE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
CAPITAL_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
                   'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'V', 'X', 'Y', 'Z']
SPECIAL_CHARACTERS = ['~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','{','}',':',';','/','<','>','.','?','`']
NUMBERS = ['1','2','3','4','5','6','7','8','9','0']
VERSION = '0.1.0'


def get_password(chars: list, length: int):
    password = ''
    for x in range(length):
        index = random.randint(0, (len(chars)-1))
        password += chars[index]
        # load password encrypted into json with the seed using caesar's algorithm
    return password


def generate_seed(length: int):
    for x in range(length):
        seed = random.randint(0, 9)
    pass


# def add_chars_to_list(self, chars):
#     if chars not in CHARS:
#         CHARS += chars
#     pass


if __name__ == "__main__":
    random.seed()
    length = 5
    use_special_chars = False
    use_capital_letters = False
    use_numbers = False
    while True:
        menu = "Welcome to Password Generator v%s\nPick your option:\n1. Generate password\n2. Change password length %s\n3. Include special characters %s\n4. Include capital letters %s\n5. Include numbers %s\t" % (
        VERSION, length, str(use_special_chars), str(use_capital_letters), str(use_numbers))
        choice = int(input(menu))
        match choice:
            case 1:
                password = get_password(CHARS, length)
                print(password)
                input()
            case 2:
                while True:
                    length = int(input("How long should the password be?\t"))
                    if length != 0:
                        break
            case 3:
                if SPECIAL_CHARACTERS not in CHARS:
                    CHARS += SPECIAL_CHARACTERS
                    use_special_chars = True
            case 4:
                if CAPITAL_LETTERS not in CHARS:
                    CHARS += CAPITAL_LETTERS
                    use_capital_letters = True
            case 5:
                if NUMBERS not in CHARS:
                    CHARS += NUMBERS
                    use_numbers = True
