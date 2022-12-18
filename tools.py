import os

RED = "\u001b[31m"
GREEN = "\u001b[32m"
CYAN = "\u001b[36m"

BRIGHT_WHITE = "\u001b[37;1m"
BRIGHT_CYAN = "\u001b[36;1m"

RESET = "\u001b[0m"

def ClearScreen():
    try:
        os.system("cls")
    except:
        pass

def IntInput(msg, bounds=(None, None), digit=None):
    while(True):
        try:
            out = input(msg).strip()
            out = int(out)
            if(bounds != (None, None) and not (bounds[0] <= out <= bounds[1])):
                print(f"{RED}Enter A Value Between {bounds[0]} and {bounds[1]}{RESET}\n")
                continue
            if(digit != None):
                if(len(str(out)) != digit):
                    print(f"{RED}Enter A {digit} digit No. please{RESET}\n")
                    continue
            return out
        except:
            print(f"{RED}Enter A Numeric Value Only{RESET}\n")
            pass

# Console
def Menu(HEADER, CONTENTS):
    # No. of spaces Before and After text
    PADDING = 2
    # String containing no. of spaces equal to PADDING (For Convinience)
    PADD = ' '*PADDING

    # List of lengths of each menu word including the header
    _CONTENTS = [len(content) for content in CONTENTS]
    _CONTENTS.append(len(HEADER))

    # Maximum length of a menu element excluding the PADD
    # len(str(len(CONTENTS))) + len(". ") stands for length of Digit of index with format; ex: "13. " would be 4
    # max(_CONTENTS) stands for maximum length of an existing menu word
    MAX_LEN = max(_CONTENTS) + len(str(len(CONTENTS))) + len(". ")
    OFF_CENTRE = ''
    # Offcentre the Header in case
    if(len(HEADER) % 2 == 0):
        OFF_CENTRE = ' '

    # output string of the menu
    out = ""
    
    # basically -> +---------------------+
    SEPERATOR = '+' + '-'*(MAX_LEN+(PADDING*2)) + '+' + '\n'
    # Space on both sides of HEADER to centre it
    HEADER_SPACE = ' '*(int((MAX_LEN - len(HEADER))/2))

    out += SEPERATOR
    # Header FORMATTED
    out += '|' + PADD + HEADER_SPACE + OFF_CENTRE + HEADER + HEADER_SPACE + PADD + '|' + '\n'
    out += SEPERATOR

    # Contents FORMATTED with index
    for (index, content) in zip(range(len(CONTENTS)),CONTENTS):
        out += '|' + PADD + str(index+1) + ". " + content + ' '*(MAX_LEN-(len(content)+len(str(index))+len(". "))) + PADD + '|' + '\n'
    
    out += SEPERATOR

    print(out)


if __name__ == "__main__":

    HEADER = "WELCOME TO ATM"
    CONTENTS = [
        "Account",
        "Withdraw",
        "Deposit",
        "Exit",
        "sdfsdfsdfsdfsdfsdfsdfsdfsdfsdf",
        "Dummy text to test formatting capabilities"
    ]

    Menu(HEADER, CONTENTS)
    print()
    IntInput("INPUT: ", bounds=(1,6))
