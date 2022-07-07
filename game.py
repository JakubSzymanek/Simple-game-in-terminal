import time
import random
import keyboard
import os

class Gra:
    def __init__(self):
        self.obstacles = ["🌲", "🌳", "🌵"]
        self.monsters = ["👾", "👻","🐙", "🐉"]
        self.mystery_box = ["🎁", "💰", "💎"]
        self.items = ["⚡", "🔥"]
        self.eq = []
        self.the_best_score = open("equipment.txt", "r").readline()
        self.character = "🔪"
        self.speed = 0.2
        self.x , self.y = 20, 10
        self.win = self.x
        self.score_of_game = 0
        self.create_board("Easy")

    def create_board(self, level):
        if level == "Easy":
            self.set_size(20, 10, 0.2)
        elif level == "Medium":
            self.set_size(40, 20, 0.1)
        elif level == "Hard":
            self.set_size(50, 25, 0.05)
        self.board = {i:["  " for _ in range(1, self.x + 1)] for i in range(1, self.y + 1)}
        if random.randint(1, 2) == 1:
            self.board[random.randint(1, self.y - 1)][random.randint(1, self.x - 1)] = random.choice(self.mystery_box)
        for i in range(2, self.x - 1):
            self.board[random.randint(1, self.y)][i] = random.choice(self.obstacles)
            self.board[random.randint(1, self.y)][i] = random.choice(self.monsters)

        self.menu()

    def set_size(self, x, y, speed):
        self.speed = speed
        self.x = x
        self.y = y
        self.win = self.x
    def menu(self):
        os.system("cls")
        list_of_choices = ["Graj","Wybierz postac","Samouczek","Ekwipunek","Test komend",
        "Wybiersz predkosc poruszania sie","Wybierz wielkosc planszy", "Wybierz Poziom trudnosci"]
        self.generate_table(list_of_choices)
        try:
            user_choice = int(input("Wybierz opcje: "))
        except:
            print("Nie wybrales opcji!")
            self.menu()

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
            print(self.items)
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
            self.win = self.x
            self.create_board("Easy")
            self.menu()
        elif user_choice == 8:
            list_of_levels = ["Easy", "Medium", "Hard"]
            self.generate_table(list_of_levels)
            user_choice = int(input("Wybierz poziom trudnosci: "))
            choices = {1: "Easy", 2: "Medium", 3: "Hard"}
            self.create_board(choices[user_choice])
        else:
            print("Nie wybrales opcji!")
            self.menu()
    def generate_table(self, list_of_choices, numerate_list = True):
        if numerate_list:
            print(f"O{'=' * 60}O")
            for i in list_of_choices:
                print(f"| {list_of_choices.index(i) + 1}. {i}{' ' * (56 - len(i))}|")
            print(f"O{'=' * 60}O")
        else:
            print(f"O{'=' * 60}O")
            for i in list_of_choices:
                print(f"| {i}{' ' * (59 - len(i))}|")
            print(f"O{'=' * 60}O")


    def score(self):
        if self.board[self.position_x][self.position_y] in self.monsters:
            self.score_of_game += 1
        elif self.board[self.position_x][self.position_y] in self.mystery_box:
            self.score_of_game += 10
            self.win += 10
            self.eq.append(random.choice(self.items))
            a = random.randint(1, self.y - 1)
            b = random.randint(1, self.x - 1)
            if self.board[a][b] == "  ":
                self.board[a][b] = random.choice(self.mystery_box)
        if self.score_of_game == self.win - 3:
            self.win = self.x
            os.system('cls')
            self.generate_table(["Wygrales!", f"Twoj wynik to: {self.score_of_game}", f"Twoj czas to: {round(time.time() - self.time_of_game)}s"], False)
            if self.score_of_game > int(open("equipment.txt", "r").readline()):
                open("equipment.txt", "w").write(f"{self.score_of_game}")
            self.the_best_score = open("equipment.txt", "r").readline()
            self.score_of_game = 0
            time.sleep(2)
            self.create_board("Easy")
            self.menu()
            

    def game_board(self):
        os.system('cls')
        stats = [f"Czas gry: {round(time.time() - self.time_of_game)}s, (Odswiezany po ruchu)",
        f"Twoj najlepszy wynik to: {self.the_best_score}",
        f"Aktualny wynik: {self.score_of_game}"]

        print(f"O{'=' * (2 *(len(self.board[1]) + 1))}O")
        for i in stats:
            print(f"| {i}{' ' * ((2 *(len(self.board[1]))) - len(i) + 1)}|")
        print(f"O{'=' * (2 *(len(self.board[1]) + 1))}O")

        for i in self.board:    
            print(f"| {''.join(self.board[i])} |")
        print(f"O{'=' * (2 *(len(self.board[1]) + 1))}O")

    def move(self):
        time.sleep(self.speed)
        self.score()   
        self.board[self.position_x][self.position_y] = self.character
        self.game_board()


    def start(self):
        self.time_of_game = time.time()
        self.position_x = 1
        self.position_y = 0
        self.board[self.position_x][self.position_y] = self.character
        self.game_board()

        while True:

            if keyboard.is_pressed("w") and self.position_x != 1 and self.board[self.position_x - 1][self.position_y] not in self.obstacles:
                self.board[self.position_x][self.position_y] = "  "
                self.position_x -= 1
                self.move()

            elif keyboard.is_pressed("s") and self.position_x != self.y and self.board[self.position_x + 1][self.position_y] not in self.obstacles:
                self.board[self.position_x][self.position_y] = "  "
                self.position_x += 1
                self.move()

            elif keyboard.is_pressed("a") and self.position_y != 0 and self.board[self.position_x][self.position_y - 1] not in self.obstacles:
                self.board[self.position_x][self.position_y] = "  "
                self.position_y -= 1
                self.move()

            elif keyboard.is_pressed("d") and self.position_y != self.x - 1 and self.board[self.position_x][self.position_y + 1] not in self.obstacles:
                self.board[self.position_x][self.position_y] = "  "
                self.position_y += 1
                self.move()

            elif keyboard.is_pressed("esc"):
                self.board[self.position_x][self.position_y] = "  "
                os.system('cls')
                self.menu()
                

game = Gra()

game.menu()