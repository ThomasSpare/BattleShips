ships = [2,3,3,4,5]

def startMenu():
    """
    start menu to the game
    """
    clear_console()
    print(
        colored(
        """
    " ______     ______     ______   ______   __         ______     ______     __  __     __     ______  \n"
    "/\\  == \\   /\\  __ \\   /\\__  _\\ /\\__  _\\ /\\ \\       /\\  ___\\   /\\  ___\\   /\\ \\_\\ \\   /\\ \\   /\\  == \\ \n"
    "\\ \\  __<   \\ \\  __ \\  \\/_/\\ \\/ \\/_/\\ \\/ \\ \\ \\____  \\ \\  __\\   \\ \\___  \\  \\ \\  __ \\  \\ \\ \\  \\ \\  _-/ \n"
    " \\ \\_____\\  \\ \\_\\ \\_\\    \\ \\_\\    \\ \\_\\  \\ \\_____\\  \\ \\_____\\  \\/\\_____\\  \\ \\_\\ \\_\\  \\ \\_\\  \\ \\_\\   \n"
    "  \\/_____/   \\/_/\\/_/     \\/_/     \\/_/   \\/_____/   \\/_____/   \\/_____/   \\/_/\\/_/   \\/_/   \\/_/   \n"
                                                                                                       \n
                                                                                                       """,
    "aqua"))
"""print leaderBoard()"""
    while True:
        try:
            checkInput(
                colored("Hit [space] to start new game or [i] to see rules for the game:\n",
                "aqua"
                )
            ).upper()
            if checkInput == "i":
                print(
                    colored(
                        """
                        1.
                        2.
                        3.
                        4.
                        5.
                        Best of Luck\n""","goldenrod1"
                    )
                )
                elif checkInput == "space":
                    break
    





def checkInput(values):
"""
Start of program, check that user
input is correct. It checks that the user
has entered correct numbers for: Username, 
size of board and number of ships
"""
    if 