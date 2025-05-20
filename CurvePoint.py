class Vec2D:
    """A simple 2D vector class to mimic Math::Vec2D."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vec2D(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vec2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vec2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vec2D(self.x / scalar, self.y / scalar)

    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        l = self.length()
        if l != 0:
            self.x /= l
            self.y /= l

    @staticmethod
    def dot_product(v1, v2):
        return v1.x * v2.x + v1.y * v2.y

    def __repr__(self):
        return f"Vec2D(x={self.x}, y={self.y})"


class CurvePoint:
    """Minimal point representation for variable width curves."""
    def __init__(self, pos=None, radius=0):
        self.pos = pos if pos is not None else Vec2D(0, 0)
        self.radius = radius

    def __repr__(self):
        return f"CurvePoint(pos={self.pos}, radius={self.radius})"
