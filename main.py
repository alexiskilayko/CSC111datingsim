from charintro import *
from choice1 import *
from choice2 import *
from sidechoice import *
from choice3 import *

def main():    
    characters = charIntro()
    characters = choice1(characters)
    characters = choice2(characters)
    characters = sidechoice(characters)
    choice3(characters)

if __name__ == "__main__":
    main()
