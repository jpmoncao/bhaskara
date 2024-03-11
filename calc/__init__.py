from math import sqrt

def delta(a, b, c):
    return b**2 - 4 * a * c

def bhaskara(a, b, delta):
    if delta < 0:
        return {"x1": "A equação não possui raízes reais.", "x2": None}
    else:
        x1 = ((b * -1) + sqrt(delta)) / (2 * a)
        x2 = ((b * -1) - sqrt(delta)) / (2 * a)
        return {"x1":x1, "x2":x2}