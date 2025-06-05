from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen, QCursor
from PIL import ImageGrab

class RegionSelector(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setCursor(Qt.CrossCursor)
        self.setMouseTracking(True)
        
        self.start_point = None
        self.end_point = None
        self.selection_rect = None
        self.screenshot = None
        
        # Get screenshot and set window to full screen
        self.screenshot = ImageGrab.grab()
        self.setGeometry(0, 0, self.screenshot.width, self.screenshot.height)
    
    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Draw semi-transparent background
        painter.fillRect(self.rect(), QColor(0, 0, 0, 100))
        
        # Draw selection rectangle if exists
        if self.selection_rect:
            painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
            painter.drawRect(self.selection_rect)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.end_point = event.pos()
            self.selection_rect = QRect(self.start_point, self.end_point)
            self.update()
    
    def mouseMoveEvent(self, event):
        if self.start_point:
            self.end_point = event.pos()
            self.selection_rect = QRect(self.start_point, self.end_point).normalized()
            self.update()
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.selection_rect:
            self.accept()
    
    def get_screenshot(self):
        if self.selection_rect:
            # Convert to PIL coordinates
            x1 = self.selection_rect.left()
            y1 = self.selection_rect.top()
            x2 = self.selection_rect.right()
            y2 = self.selection_rect.bottom()
            
            # Crop screenshot
            return self.screenshot.crop((x1, y1, x2, y2))
        return None
    
    def select_region(self):
        self.show()
        return True