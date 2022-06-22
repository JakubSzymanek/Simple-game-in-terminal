import time
import random
import keyboard
import os

class Gra:
    def __init__(self):
        self.monsters = ["👾", "👻", "🤖", "🐙", "🐉"]
        self.character = "🔪"
        self.speed = 0.1
        self.x , self.y = 20, 10
        self.board = {i:["  " for _ in range(1, self.x + 1)] for i in range(1, self.y + 1)}
        for i in range(2, self.x - 1):
            self.board[random.randint(1, self.y)][i] = random.choice(self.monsters)
    
    def menu(self):
        print(f""" 
        O================================================O
        |1. Graj                                         |
        |2. Wybierz postac                               |
        |3. Samouczek                                    |  
        |4. Ekwipunek                                    |
        |5. Test komend                                  |
        |6. Wybiersz predkosc poruszania sie             |
        |                                                |
        |                                                |
        |                                                |
        O================================================O
        """)
        user_choice = int(input("Wybierz opcje: "))

        if user_choice == 1:
            self.start()

        elif user_choice == 2:
            os.system('cls')
            self.character = str(input(f"Aktualnie wybrana postac: '{self.character}'. \nWybierz postac: "))
            os.system('cls')
            self.menu()

        elif user_choice == 3:
            os.system('cls')
            print("Gra polega na niszczeniu potworow, aby zlikwidowac potwora nalezy na niego najechac.\nAby opuscic gre nasisnij ESC.\n")
            self.menu()

        elif user_choice == 4:
            os.system('cls')
            print("Ekwipunek")
            self.menu()

        elif user_choice == 5:
            eval(input("Wpisz komende: "))
            self.menu()

        elif user_choice == 6:
            self.speed = float(input("Wpisz predkosc (Np. 0.02s): "))
            self.menu()

    def game_board(self):
        os.system('cls')
        print(f"O{'=' * (2 *(len(self.board[1]) + 1))}O")
        for i in self.board:    
            print(f"| {''.join(self.board[i])} |")
        print(f"O{'=' * (2 *(len(self.board[1]) + 1))}O")

    def start(self):
        position_x = 10
        position_y = 5
        self.game_board()
        self.board[position_x][position_y] = self.character
        self.game_board()

        while True:

            if keyboard.is_pressed("w") and position_x != 1:
                time.sleep(self.speed)
                self.board[position_x][position_y] = "  "
                position_x -= 1
                self.board[position_x][position_y] = self.character
                self.game_board()

            elif keyboard.is_pressed("s") and position_x != self.y:
                time.sleep(self.speed)
                self.board[position_x][position_y] = "  "
                position_x += 1
                self.board[position_x][position_y] = self.character
                self.game_board()

            elif keyboard.is_pressed("a") and position_y != 0:
                time.sleep(self.speed / 2)
                self.board[position_x][position_y] = "  "
                position_y -= 1
                self.board[position_x][position_y] = self.character
                self.game_board()

            elif keyboard.is_pressed("d") and position_y != self.x - 1:
                time.sleep((self.speed / 2))
                self.board[position_x][position_y] = "  "
                position_y += 1
                self.board[position_x][position_y] = self.character
                self.game_board()

            elif keyboard.is_pressed("esc"):
                self.board[position_x][position_y] = "  "
                os.system('cls')
                self.menu()
                

game = Gra()

game.menu()