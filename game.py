import time
import random
import keyboard
import os






class Gra:
    def __init__(self):
        self.monsters = ["👾", "👻", "🤖", "🐙", "🐉"]
        self.character = "🔪"
        self.speed = 0.2
        self.x , self.y = 20, 10
        self.score_of_game = 0
        self.position_x = 1
        self.position_y = 0
        self.create_board()

    def create_board(self):
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
        |7. Wybierz wielkosc planszy                     |
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
        elif user_choice == 7:
            self.x = int(input("Wpisz wielkosc planszy (Np. 20): "))
            self.y = int(input("Wpisz wielkosc planszy (Np. 10): "))
            self.create_board()
            self.menu()

    def score(self):
        if self.board[self.position_x][self.position_y] in self.monsters:
            self.score_of_game += 1
        if self.score_of_game == self.x - 3:
            os.system('cls')
            print("Wygrales!")
            time.sleep(2)
            self.menu()
            

    def game_board(self):
        os.system('cls')
        print(f"Aktualny wynik: {self.score_of_game}")
        print(f"O{'=' * (2 *(len(self.board[1]) + 1))}O")
        for i in self.board:    
            print(f"| {''.join(self.board[i])} |")
        print(f"O{'=' * (2 *(len(self.board[1]) + 1))}O")

    def move(self, position, char):
        time.sleep(self.speed)
        self.board[self.position_x][self.position_y] = "  "
        if char == "-" and position == "x":
            self.position_x -= 1
        elif char == "+" and position == "x":
            self.position_x += 1
        elif char == "-" and position == "y":
            self.position_y -= 1
        else:
            self.position_y += 1
        self.score()   
        self.board[self.position_x][self.position_y] = self.character
        self.game_board()


    def start(self):
        self.game_board()
        self.board[self.position_x][self.position_y] = self.character
        self.game_board()

        while True:

            if keyboard.is_pressed("w") and self.position_x != 1:
                self.move("x", "-")

            elif keyboard.is_pressed("s") and self.position_x != self.y:
                self.move("x", "+")

            elif keyboard.is_pressed("a") and self.position_y != 0:
                self.move("y", "-")

            elif keyboard.is_pressed("d") and self.position_y != self.x - 1:
                self.move("y", "+")

            elif keyboard.is_pressed("esc"):
                self.board[self.position_x][self.position_y] = "  "
                os.system('cls')
                self.menu()
                

game = Gra()

game.menu()