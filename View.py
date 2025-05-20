import sys
import random
import math
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent, QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QPoint



class View(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Vessel Contouring")
        self.imageLabel = QLabel()
        self.setCentralWidget(self.imageLabel)

        self.last_mouse_pos = QPoint()
        self.mouse_pos_down = QPoint()
        self.mouse_pressed = False
        
        # Store the original pixmap and the drawing pixmap
        self.original_pixmap = None
        self.drawing_pixmap = None
        
        # Line properties
        self.line_radius = 5  # Default radius for line thickness
        
        self.resize(800, 600)

    def load_image(self, image_path):
        self.original_pixmap = QPixmap(image_path)
        
        # Get screen size
        screen = QApplication.primaryScreen().geometry()
        max_width = screen.width() * 0.8  # 80% of screen width
        max_height = screen.height() * 0.8  # 80% of screen height
        
        # Calculate scaled size maintaining aspect ratio
        self.original_pixmap = self.original_pixmap.scaled(
            int(max_width),
            int(max_height),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        
        # Create a copy for drawing
        self.drawing_pixmap = self.original_pixmap.copy()
        
        # Set the window size to match the scaled image size
        self.resize(self.original_pixmap.width(), self.original_pixmap.height())
        
        # Display the image
        self.imageLabel.setPixmap(self.drawing_pixmap)
    
    def draw_line(self, start_point, end_point):
        if self.drawing_pixmap is None:
            return
            
        # Create a painter for the drawing pixmap
        painter = QPainter(self.drawing_pixmap)
        # Set pen with radius (thickness)
        painter.setPen(QPen(QColor(255, 0, 0), self.line_radius * 2))  # Multiply by 2 to get diameter
        painter.drawLine(start_point, end_point)
        painter.end()
        
        # Update the display
        self.imageLabel.setPixmap(self.drawing_pixmap)

    def create_straight_line(self, start_x, start_y, end_x, end_y):
        start_point = QPoint(start_x, start_y)
        end_point = QPoint(end_x, end_y)
        self.draw_line(start_point, end_point)

    def create_random_line(self, length=50):
        if self.drawing_pixmap is None:
            return
            
        # Get the dimensions of the current pixmap
        width = self.drawing_pixmap.width()
        height = self.drawing_pixmap.height()
        
        # Generate random start point
        start_x = random.randint(0, width)
        start_y = random.randint(0, height)
        
        # Generate random angle in radians
        angle = random.uniform(0, 2 * 3.14159)  # 2π radians = 360 degrees
        
        # Calculate end point using trigonometry
        end_x = start_x + length * math.cos(angle)
        end_y = start_y + length * math.sin(angle)
        
        # Ensure the end point is within the image bounds
        end_x = max(0, min(width, end_x))
        end_y = max(0, min(height, end_y))
        
        self.create_straight_line(int(start_x), int(start_y), int(end_x), int(end_y))

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_mouse_down = True
            self.mouse_down_pos = event.pos()
            self.last_mouse_pos = event.pos()
            print(f"Mouse pressed at: ({event.pos().x()}, {event.pos().y()})")

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.is_mouse_down = False
            print(f"Mouse released at: ({event.pos().x()}, {event.pos().y()})")

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.is_mouse_down:
            # Calculate the movement delta
            delta = event.pos() - self.last_mouse_pos
            print(f"Mouse moved to: ({event.pos().x()}, {event.pos().y()})")
            print(f"Movement delta: ({delta.x()}, {delta.y()})")
            
            # Update last position
            self.last_mouse_pos = event.pos()
            
    def set_line_radius(self, radius):
        """Set the radius (thickness) of the lines"""
        self.line_radius = radius


def main():
    app = QApplication(sys.argv)
    view = View()
    view.load_image("Images/1.png")
    
    # Set line radius (thickness)
    view.set_line_radius(3)  # You can adjust this value to change line thickness
    
    for _ in range(10):
        view.create_random_line(length=50)
    
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()