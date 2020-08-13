class Player(object):

    def __init__(self, name): 
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives
    
    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("lives cannot be negative!")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if level > 0:
            self._score += (level - self._level) * 1000
            self._level = level
        
        else:
            print("cannot go below level 1")
         


    level = property(_get_level, _set_level)
    lives = property(_get_lives, _set_lives)

    @property

    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def __str__(self):
        return "Name: {0.name}, Lives : {0.lives}, Level: {0.level}, : {0.}".format(self)


    

        