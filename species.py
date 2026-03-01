import operator
import random

class Species:
    def __init__(self,player):
        self.players = []
        self.average_fitness = 0
        self.threshold = 1.2
        self.players.append(player)
        self.bench_mark_fitness = player.fitness
        self.bench_mark_brain = player.brain.clone()
        self.champion = player.clone()

    def similarity(self,brain):
        similarity = self.weight_difference(self.bench_mark_brain, brain)
        return self.threshold>similarity

    @staticmethod
    def weight_difference(brain, brain2):
        total_diff=0
        for i in range(0,len(brain.connections)):
            for ii in range(0,len(brain2.connections)):
                if i==ii:
                    total_diff+=abs(brain.connections[i].weight-brain2.connections[i].weight)

        return total_diff


    def add_to_species(self,player):
        self.players.append(player)

    def sort_players_by_fitness(self):
        self.players.sort(key=operator.attrgetter('fitness'),reverse=True)
        if self.players[0].fitness > self.bench_mark_fitness:
            self.bench_mark_fitness = self.players[0].fitness
            self.champion.fitness = self.players[0].clone()

    def calculate_average_fitness(self):
        total_fitness = 0
        for player in self.players:
            total_fitness += player.fitness
        if self.players:
            self.average_fitness = int(total_fitness/len(self.players))
        self.average_fitness=0

    def offspring(self):
        # If only champion exists, clone it
        if len(self.players) <= 1:
            baby = self.players[0].clone()
        else:
            # Exclude champion (index 0)
            baby = random.choice(self.players[1:]).clone()

        baby.brain.mutate()
        return baby













