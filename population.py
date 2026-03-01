import config
import player

class Population:
    def __init__(self,size):
        self.players=[]
        self.size=size
        for i in range(0,self.size):
            self.players.append(player.Player())
    def update_live_players(self):
        for p in self.players:
            if p.alive:
                p.look()
                p.think()
                p.draw(config.window)
                p.update(config.ground)

    def extinct(self):
        extent=True
        for p in self.players:
            if p.alive:
                extent=False
        return extent