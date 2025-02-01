#!/usr/bin/python

import os
from random import randint

### CONSTANTS & VARIABLES #############################################################################

board = {
    "a1": " ", "a2": " ", "a3": " ",
    "b1": " ", "b2": " ", "b3": " ",
    "c1": " ", "c2": " ", "c3": " "
}

winning_combinations = [
    
    # Rows
    ["a1", "a2", "a3"],
    ["b1", "b2", "b3"],
    ["c1", "c2", "c3"],
    
    # Columns
    ["a1", "b1", "c1"],
    ["a2", "b2", "c2"],
    ["a3", "b3", "c3"],
    
    # Diagonals
    ["a1", "b2", "c3"],
    ["a3", "b2", "c1"]
    
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

### FUNCTIONS #########################################################################################

def startAscii():
    print("""
        ███      ▄█   ▄████████          ███        ▄████████  ▄████████          ███      ▄██████▄     ▄████████ 
    ▀█████████▄ ███  ███    ███      ▀█████████▄   ███    ███ ███    ███      ▀█████████▄ ███    ███   ███    ███ 
       ▀███▀▀██ ███▌ ███    █▀          ▀███▀▀██   ███    ███ ███    █▀          ▀███▀▀██ ███    ███   ███    █▀  
        ███   ▀ ███▌ ███                 ███   ▀   ███    ███ ███                 ███   ▀ ███    ███  ▄███▄▄▄     
        ███     ███▌ ███                 ███     ▀███████████ ███                 ███     ███    ███ ▀▀███▀▀▀  
        ███     ███  ███    █▄           ███       ███    ███ ███    █▄           ███     ███    ███   ███    █▄ 
        ███     ███  ███    ███          ███       ███    ███ ███    ███          ███     ███    ███   ███    ███
       ▄████▀   █▀   ████████▀          ▄████▀     ███    █▀  ████████▀          ▄████▀    ▀██████▀    ██████████
    
                                    - Juan Dalmau Santandreu | ASIX 2024 -
    """)
    input("\n\nPress any key to continue...")
    clear()

def stopAscii(winner):
    
    clear()
            
    print(f"""
       ▄██████▄     ▄████████   ▄▄▄▄███▄▄▄▄      ▄████████       ▄██████▄   ▄█    █▄     ▄████████    ▄████████ 
      ███    ███   ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
      ███    █▀    ███    ███ ███   ███   ███   ███    █▀       ███    ███ ███    ███   ███    █▀    ███    ███ 
     ▄███          ███    ███ ███   ███   ███  ▄███▄▄▄          ███    ███ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
    ▀▀███ ████▄  ▀███████████ ███   ███   ███ ▀▀███▀▀▀          ███    ███ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
      ███    ███   ███    ███ ███   ███   ███   ███    █▄       ███    ███ ███    ███   ███    █▄  ▀███████████ 
      ███    ███   ███    ███ ███   ███   ███   ███    ███      ███    ███ ███    ███   ███    ███   ███    ███ 
      ████████▀    ███    █▀   ▀█   ███   █▀    ██████████       ▀██████▀   ▀██████▀    ██████████   ███    ███
    
                                              - Player {winner} wins! GG -
    """)

def selectTurn():
    
    print("""

            ▒██   ██▒       ██▒   █▓  ██████        ▒█████  
            ▒▒ █ █ ▒░      ▓██░   █▒▒██    ▒       ▒██▒  ██▒
            ░░  █   ░       ▓██  █▒░░ ▓██▄         ▒██░  ██▒
             ░ █ █ ▒         ▒██ █░░  ▒   ██▒      ▒██   ██░
            ▒██▒ ▒██▒         ▒▀█░  ▒██████▒▒      ░ ████▓▒░
            ▒▒ ░ ░▓ ░         ░ ▐░  ▒ ▒▓▒ ▒ ░      ░ ▒░▒░▒░ 
            ░░   ░▒ ░         ░ ░░  ░ ░▒  ░ ░        ░ ▒ ▒░ 
            ░    ░             ░░  ░  ░  ░        ░ ░ ░ ▒  
            ░    ░              ░        ░            ░ ░  
                                ░                           
          """)
     
    sel = input("Anything for random\nSelect the player to start (X - O): ").upper()
    
    if sel == "O":
        return 1

    elif sel == "X":
        return 0
        
    else:
        return randint(0, 1)

def playerMode():
    
    while True:
        
        int(input("Selecciona el numero de jugadores: "))

def selectPosition(player):
    
    drawBoard(player)
    
    while True:
            
        position = input("\nSelect a position: ").lower()
            
        if position in board:
            
            if board[position] != " ":
                
                print(f"La casilla {position} ya esta seleccionada!")
                    
            else:
                    
                board[position] = player
                break
                        
        else:
                
            print("\nError! Introduce valores de la A a la C y del 1 al 3 \nEj: A1, B2, C3")
    
def drawBoard(player):
    
    clear()
    
    print(f" ═════ {player} turn ════════════\n")

    game_board = (
        "       ╔═════╦═════╦═════╗\n"
        "       ║  1  ║  2  ║  3  ║\n"
        " ╔═════╬═════╬═════╬═════╣\n"
        f" ║  A  ║  {board['a1']}  ║  {board['a2']}  ║  {board['a3']}  ║\n"
        " ╠═════╬═════╬═════╬═════╣\n"
        f" ║  B  ║  {board['b1']}  ║  {board['b2']}  ║  {board['b3']}  ║\n"
        " ╠═════╬═════╬═════╬═════╣\n"
        f" ║  C  ║  {board['c1']}  ║  {board['c2']}  ║  {board['c3']}  ║\n"
        " ╚═════╩═════╩═════╩═════╝\n"
    )
    
    print(game_board)
        
    
def check_winner():
    
    for combination in winning_combinations:
        
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != " ":
            
            return board[combination[0]]
    
    else: 
    
        return None

### MAIN CODE #########################################################################################
    
def main(): 
    
    clear()
    
    startAscii()

    turn = selectTurn()
    
    for _ in range(9):
                
        if (turn % 2) == 0:
            player = "X"
            
        else:
            player = "0"
        
        selectPosition(player)    
        
        winner = check_winner()
        
        if winner:
            break
        
        turn += 1
    else:
    
        player = "Nobody"
    
    clear()
    drawBoard("Final")
    input("\nPress any key to continue... ")
    
    stopAscii(player)
        
if __name__ == "__main__": 
    main()
