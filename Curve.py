from CurvePoint import Vec2D, CurvePoint
import math
import random

class Curve:

    def __init__(self, curve_id):
        self.curve_id = curve_id
        self.curve_points = []
    


    def add_point(self, point):

        self.curve_points.append(point)


    def create_curve_from_points(self, points):

        for point in points:

            self.curve_points.append(point)
        

    def get_curve_points(self):

        return self.curve_points


    def create_straight_line(self, width, angle, length, num_points, window_width=100, window_height=100, margin=10):

        # Convert angle to radians
        angle_rad = math.radians(angle)

        # Calculate the unit direction vector based on the angle
        direction = Vec2D(math.cos(angle_rad), math.sin(angle_rad))

        # Calculate the spacing between points
        spacing = length / (num_points - 1)

        # Adjust the starting position to ensure the entire line fits within the window
        max_start_x = window_width - abs(direction.x * length) - margin
        max_start_y = window_height - abs(direction.y * length) - margin
        start_x = random.uniform(margin, max_start_x)
        start_y = random.uniform(margin, max_start_y)
        start_point = Vec2D(start_x, start_y)

        # Generate points along the fixed-size line
        for i in range(num_points):
            position = start_point + direction * (i * spacing)
            self.curve_points.append(CurvePoint(pos=position, radius=width))
            print(f"Generated point: ({position.x}, {position.y})")  # Debug print

        return self.curve_points

