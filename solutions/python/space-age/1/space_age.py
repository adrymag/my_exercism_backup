YEAR_SECONDS = 31557600 # 31,557,600

conversion_rates = {
    'Mercury' : 0.2408467,
    'Venus' : 0.61519726,
    'Earth' : 1.0,
    'Mars' : 1.8808158,
    'Jupiter' : 11.862615,
    'Saturn' : 29.447498,
    'Uranus' : 84.016846,
    'Neptune' : 164.79132
}

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / YEAR_SECONDS, 2)

    def on_mercury(self):
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Mercury'], 2)

    def on_venus(self):
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Venus'], 2)

    def on_mars(self):
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Mars'], 2)

    def on_jupiter(self):
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Jupiter'], 2)

    def on_saturn(self):
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Saturn'], 2)

    def on_uranus(self):
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Uranus'], 2)

    def on_neptune(self):
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Neptune'], 2)