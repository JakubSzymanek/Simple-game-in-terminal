import time
import random
import keyboard
import os

class Gra:
    def __init__(self):
        self.rewards = [" ", "X"]
        self.character = "O"
        x = 100  # szerokosc  
        y = 20  # wysokosc
        self.a = {i:[" " for z in range(1, x + 1)] for i in range(1, y + 1)}
    
    def menu(self):
        print(f""" 
        O================================================O
        |1. Graj                                         |
        |2. Wybierz postac                               |
        |3. Samouczek                                    |  
        |                                                |
        |                                                |
        |                                                |
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
            self.character = str(input("Postać Domyslna 'O'. \nWybierz postac: "))
            os.system('cls')
            self.menu()
        elif user_choice == 3:
            os.system('cls')
            print("Gra polega na niszczeniu potworow, aby zlikwidowac potwora nalezy na niego najechac.\nAby opuscic gre nasisnij ESC.\n")
            self.menu()
    def game_board(self):
        os.system('cls')
        for i in self.a:
            if i == 1 or i == 20:
                print(f"O{'=' * (len(self.a[1]) + 2)}O")
            else:
                print(f"| {''.join(self.a[i])} |")

    def start(self):
        position_x = 10
        position_y = 5
        self.game_board()
        self.a[position_x][position_y] = self.character
        self.game_board()

        while True:
            if keyboard.is_pressed("w"):
                time.sleep(0.05)
                self.a[position_x][position_y] = " "
                position_x -= 1
                self.a[position_x][position_y] = self.character
                self.game_board()

            elif keyboard.is_pressed("s"):
                time.sleep(0.05)
                self.a[position_x][position_y] = " "
                position_x += 1
                self.a[position_x][position_y] = self.character
                self.game_board()

            elif keyboard.is_pressed("a"):
                time.sleep(0.005)
                self.a[position_x][position_y] = " "
                position_y -= 1
                self.a[position_x][position_y] = self.character
                self.game_board()

            elif keyboard.is_pressed("d"):
                time.sleep(0.005)
                self.a[position_x][position_y] = " "
                position_y += 1
                self.a[position_x][position_y] = self.character
                self.game_board()
            elif keyboard.is_pressed("esc"):
                self.a[position_x][position_y] = " "
                os.system('cls')
                self.menu()
                
        






game = Gra()

game.menu()