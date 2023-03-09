import random
# that method provide random value

class Die:
 
    def __init__(self,value=None): 
        self._value=value

    @property
    def value(self):
        return self._value

    def Roll(self):
        new_value=random.randint(1,6)
        self._value=new_value
        return new_value

# Access the value at the time when we create Die class
# object1=Die()
# o1=object1.Roll()
# print(o1)

class Player:
    # die has taken as a object of Die class to access attribute and method into aggregateclass

    def __init__(self,die,is_computer=False):
        self._die=die
        self._is_computer=is_computer
        self._counter=10
        # direct value ma value argument ma nhi dani padti

    @property
    def die(self):
        return self._die

    @property
    def is_computer(self):
        return self._is_computer

    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

    def decrement_counter(self):
        self._counter -= 1

    def roll_die(self):
        return self._die.Roll(self)

# test the player class
# die=Die()
# player=Player(die,is_computer=True)


# print(player.is_computer)
# print(player.die)
# print(player.counter)
# print(player.increment_counter())
# print(player.counter)
# print(player.decrement_counter())
# print(player.counter)
# print(player._die.value) 
# roll=player.roll_die()
# print(player._die.value)
# print(roll)

class DiceGame:

    def __init__(self,player,computer):
        self._player=player
        self._computer=computer

    def play(self):
        print("===================================================")
        print("🎲🎲WELCOME TO ROLL THE DIE🎲🎲")
        print("===================================================")
        while True:
            self.play_round()
            game_over=self.check_game_over()
            # yaha provide karaga true or false 
            # agar True retuen hua to game_over True mananga
            if game_over:
                break

    def play_round(self):
        self.print_round_welcome()
        #as a breaker
        player_value=self._player.roll_die()
        computer_value=self._computer.roll_die()

        self.show_dice(player_value,computer_value)

        if player_value>computer_value:
            print("you win this round🎉🎉🎉")
            # self._player.decrement_counter()    #winner
            # self._computer.increment_counter()  # losser
            self.update_counter(winner=self._player,looser=self._computer)

        elif computer_value>player_value:
            print("Computer win this round || Try Again😔")
            # self._computer.decrement_counter()  #winner
            # self._player.increment_counter()  # losser
            self.update_counter(winner=self._computer,looser=self._player)

        else:
            print("Match has tied || Have a chance to win😃😃")

        self.show_counter()

    def print_round_welcome(self):
         print("-----------NEW ROUND-----------")
         input("press any key to start the game")

    def show_dice(self,player_value,computer_value):
        print(f"player_value is {player_value}")
        print(f"computer_value is {computer_value}")

    def update_counter(self,winner,looser):
        winner.decrement_counter()
        looser.increment_counter()

    def show_counter(self):
        print(f"Player Counter: {self._player.counter}")
        print(f"Computer Counter: {self._computer.counter}")

    def check_game_over(self):
        if self._computer.counter == 0:
            self.show_winner(self._computer)
            return True

        elif self._player.counter == 0:
            self.show_winner(self._player)
            return True

        else:
            return False

    def show_winner(self,winner):
        if winner.is_computer:
            print("\n=======================")
            print(" G A M E   O V E R ✨")
            print("=======================")
            print("The computer won the game. Sorry...")
            print("=================================")
        else:
            print("\n=======================")
            print(" G A M E   O V E R ✨")
            print("=======================")
            print("You won the match || Congratulaion🎉🎉🎉🎉🎉🎉")
            print("=================================")
        

# Die Instances
player_die=Die()
computer_die=Die()

# Player Instances
my_player=Player(Die,is_computer=False)
computer_player=Player(Die,is_computer=True)

# DiceGame Instances
game=DiceGame(my_player,computer_player)
game1=game.play()
print(game1)


        



        


