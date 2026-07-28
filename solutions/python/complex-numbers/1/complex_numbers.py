import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        return

    def __eq__(self, other):
        if self.real == other.real and self.imaginary == other.imaginary:
            return True
        return False

    def __add__(self, other):
        added_real_part = 0
        added_imaginary_part = 0

        if hasattr(other, 'real'): # name 'hasAttr' is not defined # other.hasAttr('real'): # ' int' object has no attribute hasAttr
            added_real_part = other.real

        if hasattr(other, 'imaginary'):
            added_imaginary_part = other.imaginary

        self.real += added_real_part
        self.imaginary += added_imaginary_part

        return self # ComplexNumber(self.real, self.imaginary) # ComplexNumber(self.real + added_real_part, self.imaginary + added_imaginary_part)

    def __radd__(self, other):
        # Called when other + self fails, e.g. 5 + ComplexNumber(...)
        # Addition is commutative, so delegate to __add__
        return self.__add__(other)

    def __mul__(self, other):
        multiplied_real_part = 0
        multiplied_imaginary_part = 0

        if hasattr(other, 'real'): # name 'hasAttr' is not defined # other.hasAttr('real'): # ' int' object has no attribute hasAttr
            multiplied_real_part = other.real

        if hasattr(other, 'imaginary'):
            multiplied_imaginary_part = other.imaginary

        real = self.real
        self.real = self.real * multiplied_real_part - self.imaginary * multiplied_imaginary_part
        self.imaginary = real * multiplied_imaginary_part + self.imaginary * multiplied_real_part

        return self
        # return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __sub__(self, other):
        subtracted_real_part = 0
        subtracted_imaginary_part = 0

        if hasattr(other, 'real'): # name 'hasAttr' is not defined # other.hasAttr('real'): # ' int' object has no attribute hasAttr
            subtracted_real_part = other.real

        if hasattr(other, 'imaginary'):
            subtracted_imaginary_part = other.imaginary

        self.real -= subtracted_real_part
        self.imaginary -= subtracted_imaginary_part

        return self # return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __neg__(self):
        """Unary minus: -c"""
        return ComplexNumber(-self.real, -self.imaginary)

    def __rsub__(self, other):
        # Called when other + self fails, e.g. 5 + ComplexNumber(...)
        # Addition is commutative, so delegate to __add__
        c = -self.__sub__(other) # TypeError: bad operand type for unary -: 'ComplexNumber'
        return c

    def __truediv__(self, other):
        divisor_real_part = 0
        divisor_imaginary_part = 0

        if hasattr(other, 'real'): # name 'hasAttr' is not defined # other.hasAttr('real'): # ' int' object has no attribute hasAttr
            divisor_real_part = other.real

        if hasattr(other, 'imaginary'):
            divisor_imaginary_part = other.imaginary

        if divisor_real_part == 0 and divisor_imaginary_part == 0:
            raise ValueError("cannot perform division by 0")

        real = self.real
        self.real = (self.real * divisor_real_part + self.imaginary * divisor_imaginary_part) / (divisor_real_part ** 2 + divisor_imaginary_part ** 2)
        self.imaginary = (self.imaginary * divisor_real_part - real * divisor_imaginary_part) / (divisor_real_part ** 2 + divisor_imaginary_part ** 2)

        return self
        # return ComplexNumber( (self.real * other.real + self.imaginary * other.imaginary) / (other.real ** 2 + other.imaginary ** 2), (self.imaginary * other.real -  self.real * other.imaginary) / (other.real ** 2 + other.imaginary ** 2) )

    def __rtruediv__(self, other):
        # return self.__mul__(other)
        module = self.__module__()
        # print(module)
        c = self.conjugate()
        # print([c.real, c.imaginary])
        p = c.__mul__(other)
        # print([p.real, p.imaginary])
        z = p.__truediv__(module)
        # print([z.real, z.imaginary])
        return z


    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def __module__(self):
        return self.real ** 2 + self.imaginary ** 2

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        return ComplexNumber( math.exp(self.real) * math.cos(self.imaginary), math.exp(self.real) * math.sin(self.imaginary) )