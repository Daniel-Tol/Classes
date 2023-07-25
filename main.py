# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

# Part 1: Players

class Player(): 
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        if not 0 <= speed <= 1:
            raise ValueError("Speed must be between 0 and 1.")
        self.speed = speed
        if not 0 <= endurance <= 1:
            raise ValueError("Endurance must be between 0 and 1.")
        self.endurance = endurance
        if not 0 <= accuracy <= 1:
            raise ValueError("Accuracy must be between 0 and 1.")
        self.accuracy = accuracy

    def introduce(self): 
        if self:
            return f"Hello everyone, my name is {self.name}."
        else:
            return "Hello everyone, my name is Bob."
        
    def strength(self):

        if self.speed >= self.endurance and self.speed >= self.accuracy:
            return ('speed', self.speed)
        if self.endurance >= self.speed and self.endurance >= self.accuracy:
            return ('endurance', self.endurance)
        if self.accuracy >= self.speed and self.accuracy >= self.endurance:
            return ('accuracy', self.accuracy)



alice = Player('Alice', 0.3, 0.4, 0.7)
print(alice.speed)
print(alice.introduce())
print(alice.strength())

# Part 2: Commentators

class Commentator(): 
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy
    
    def compare_players(self, player_1, player_2, attr):
        attr_player_1 = getattr(player_1, attr)
        attr_player_2 = getattr(player_2, attr)

        if attr_player_1 > attr_player_2:
            return player_1.name
        if attr_player_1 < attr_player_2:
            return player_2.name
        if attr_player_1 == attr_player_2:
            strength_player_1 = player_1.strength()
            strength_player_2 = player_2.strength()
            if strength_player_1 > strength_player_2:
                return player_1.name
            if strength_player_1 < strength_player_2:
                return player_2.name
            if strength_player_1 == strength_player_2:
                highest_sum_player_1 = self.sum_player(player_1)
                highest_sum_player_2 = self.sum_player(player_2)
                if highest_sum_player_1 > highest_sum_player_2:
                    return player_1.name
                if highest_sum_player_1 < highest_sum_player_2:
                    return player_2.name
                if highest_sum_player_1 == highest_sum_player_2:
                    return 'These two players might as well be twins!'


ray = Commentator('Ray Hudson')
print(ray.name)
print(ray.sum_player(alice))
alice = Player('Alice', 0.8, 0.2, 0.6)
bob = Player('Bob', 0.9, 0.2, 0.6)
print(ray.compare_players(alice, bob, 'endurance'))