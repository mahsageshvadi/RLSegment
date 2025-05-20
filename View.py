import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QMouseEvent
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

        self.resize(800, 600)

    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        
        # Get screen size
        screen = QApplication.primaryScreen().geometry()
        max_width = screen.width() * 0.8  # 80% of screen width
        max_height = screen.height() * 0.8  # 80% of screen height
        
        # Calculate scaled size maintaining aspect ratio
        scaled_pixmap = pixmap.scaled(
            int(max_width),
            int(max_height),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        
        # Set the window size to match the scaled image size
        self.resize(scaled_pixmap.width(), scaled_pixmap.height())
        
        # Display the image
        self.imageLabel.setPixmap(scaled_pixmap)
    
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
            


def main():

    app = QApplication(sys.argv)
    view = View()
    view.load_image("Images/1.png")
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()