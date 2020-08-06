class Player(object):

    def __init__(self, name): 
        self.name = name
        self._lives = 3
        self._level = 1
        self.score = 0

    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("_lives cannot be negative!")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            self.score += (level - self._level) * 1000
            self._level = level
        
        else:
            print("Cannot go below level 1")
         


    level = property(_get_level,_set_level)
    lives = property(_get_lives, _set_lives)

    def __str__(self):
        return "Name: {0.name}, Lives : {0.lives}, Level: {0.level}, Score: {0.score}".format(self)


    

        