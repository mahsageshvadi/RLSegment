import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QColor
import numpy as np
import vescl_binding

class VesselContouringWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vescl = vescl_binding.VesselContouring()
        self.setMouseTracking(True)
        self.drawing = False
        self.radius = 5.0  # Default radius for vessel drawing
        
        # Load an image (replace with your image path)
        self.vescl.loadImage("path/to/your/image.png")
        
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = True
            pos = event.position()
            self.vescl.startDraw(pos.x(), pos.y(), self.radius)
            self.update()
            
    def mouseMoveEvent(self, event):
        if self.drawing:
            pos = event.position()
            self.vescl.updateDraw(pos.x(), pos.y(), self.radius)
            self.update()
            
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawing = False
            pos = event.position()
            self.vescl.endDraw(pos.x(), pos.y(), self.radius)
            self.update()
            
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_F:
            # Fit selected vessel to nearest vessel
            self.vescl.fitSelectedToVessel(self.radius)
            self.update()
        elif event.key() == Qt.Key.Key_W:
            # Fit vessel width
            self.vescl.fitSelectedVesselWidth(self.radius)
            self.update()
            
    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Get the rendered image from VESCL
        width = self.width()
        height = self.height()
        image = self.vescl.getRenderedImage(width, height)
        
        # Convert numpy array to QImage and draw it
        # Note: You'll need to implement the actual image conversion
        # This is a placeholder that draws a blank background
        painter.fillRect(self.rect(), QColor(0, 0, 0))

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vessel Contouring")
        self.setGeometry(100, 100, 800, 600)
        
        self.widget = VesselContouringWidget(self)
        self.setCentralWidget(self.widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())