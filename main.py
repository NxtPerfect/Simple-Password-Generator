import random

# two underscores in class make method/variable private

CHARS = []
LOWERCASE_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k',
                     'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'v', 'x', 'y', 'z']
VERSION = '0.1.0'


def get_password(self, chars, length: int, seed: int):
    for x in range(length):
        index = random.randrange(0, len(chars))
        password = LOWERCASE_LETTERS[index]
        # load password encrypted into json with the seed using caesar's algorithm
    return password

def generate_seed(self, length: int):
    for x in range(length):
        seed = rand.random(0, 9)
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
    menu = "Welcome to Password Generator v%s\nPick your option:\n1. Generate password\n2. Change password length %s\n3. Include special characters %s\n4. Include capital letters %s\n5. Include numbers %s\t" % (VERSION, length, str(use_special_chars), str(use_capital_letters), str(use_numbers))
    choice = int(input())
    match choice:
        case 1:
            password = get_password(CHARS, length, generate_seed(6))
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
        case 4:
            if CAPITAL_LETTERS not in CHARS:
                CHARS += CAPITAL_LETTERS
        case 5:
            if NUMBERS not in CHARS:
                CHARS += NUMBERS
