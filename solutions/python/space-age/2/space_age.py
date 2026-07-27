"""
Given an age in seconds, calculate how old someone would be on a planet in our Solar System.

One Earth year equals 365.25 Earth days, or 31,557,600 seconds. If you were told someone was 1,000,000,000 seconds old, their age would be 31.69 Earth-years.

For the other planets, you have to account for their orbital period in Earth Years:

Planet	Orbital period in Earth Years
Mercury	0.2408467
Venus	0.61519726
Earth	1.0
Mars	1.8808158
Jupiter	11.862615
Saturn	29.447498
Uranus	84.016846
Neptune	164.79132
"""

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
        """
        Converts seconds into Earth years
        """
        return round(self.seconds / YEAR_SECONDS, 2)

    def on_mercury(self):
        """
        Converts seconds into Mercury years
        """
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Mercury'], 2)

    def on_venus(self):
        """
        Converts seconds into Venus years
        """
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Venus'], 2)

    def on_mars(self):
        """
        Converts seconds into Mars years
        """
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Mars'], 2)

    def on_jupiter(self):
        """
        Converts seconds into Jupiter years
        """
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Jupiter'], 2)

    def on_saturn(self):
        """
        Converts seconds into Saturn years
        """
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Saturn'], 2)

    def on_uranus(self):
        """
        Converts seconds into Uranus years
        """
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Uranus'], 2)

    def on_neptune(self):
        """
        Converts seconds into Neptune years
        """
        return round(self.seconds / YEAR_SECONDS / conversion_rates['Neptune'], 2)