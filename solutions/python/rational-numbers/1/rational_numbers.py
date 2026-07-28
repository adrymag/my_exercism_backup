import math

class Rational:
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError("Denominator cannot be zero")
        
        # Reduce to lowest terms using GCD
        g = math.gcd(numer, denom)
        if g != 0:
            numer //= g
            denom //= g
        
        # Standard form: positive denominator
        if denom < 0:
            numer = -numer
            denom = -denom
        
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        if isinstance(other, int):
            return self.denom == 1 and self.numer == other
        if not isinstance(other, Rational):
            return NotImplemented
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        n = self.numer * other.denom + other.numer * self.denom
        d = self.denom * other.denom
        return Rational(n, d)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        n = self.numer * other.denom - other.numer * self.denom
        d = self.denom * other.denom
        return Rational(n, d)

    def __rsub__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        return other.__sub__(self)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        n = self.numer * other.numer
        d = self.denom * other.denom
        return Rational(n, d)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        if other.numer == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        n = self.numer * other.denom
        d = self.denom * other.numer
        return Rational(n, d)

    def __rtruediv__(self, other):
        if isinstance(other, int):
            other = Rational(other, 1)
        return other.__truediv__(self)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int):
            if power >= 0:
                return Rational(self.numer ** power, self.denom ** power)
            else:
                return Rational(self.denom ** abs(power), self.numer ** abs(power))
        else:
            return (self.numer ** power) / (self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)