class HighScores:
    def __init__(self, scores):
        """Stores a copy of the scores list
        
        list(scores) creates a defensive copy (if you just did self._scores = scores, then 
        mutating the original list outside the class would also mutate the internal state)
        """
        self._scores = list(scores) # turns the iterable parameter/argument into the list attribute

    @property
    def scores(self):
        """Returns the full list
        
        The @property decorator used for scores lets you read the scores naturally:
        
        hs = HighScores([30, 50, 20, 70])
        hs.scores          # [30, 50, 20, 70]  — looks like an attribute
        hs.latest()        # 70
        hs.personal_best() # 70
        hs.personal_top_three()  # [70, 50, 30]
        """
        return self._scores # a "property getter" / accessor - in fact, 

    def latest(self):
        """Returns the most recently added score"""
        return self._scores[-1] # returns only the latest (last introduced/added) score

    def personal_best(self):
        """Returns the single highest score"""
        return max(self._scores) # only the (very) best score

    def personal_top_three(self):
        """Returns top 3 in descending order"""
        return sorted(self._scores, reverse=True)[:3] # descendingly sorted -> take only the first 3