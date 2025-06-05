from PyQt5.QtWidgets import QMainWindow, QPushButton, QFileDialog, QMessageBox, QDialog
from PyQt5.QtCore import Qt
from region import RegionSelector

class ScreenshotTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Region Screenshot Tool")
        self.setGeometry(100, 100, 300, 200)
        
        self.region_btn = QPushButton("Select Region", self)
        self.region_btn.setGeometry(50, 50, 200, 40)
        self.region_btn.clicked.connect(self.select_region)
        
        self.selector = None
        self.screenshot = None
    
    def select_region(self):
        self.hide()
        self.selector = RegionSelector()
        
        # 使用exec_()等待对话框关闭
        if self.selector.exec_() == QDialog.Accepted:
            self.screenshot = self.selector.get_screenshot()
            self.show()
            if self.screenshot:
                self.save_screenshot()
    
    def save_screenshot(self):
        if not self.screenshot:
            return
            
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Save Screenshot", 
            "", 
            "PNG Image (*.png);;JPEG Image (*.jpg);;BMP Image (*.bmp)",
            options=options)
            
        if file_path:
            try:
                self.screenshot.save(file_path)
                QMessageBox.information(self, "Success", "截图保存成功！")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"保存截图失败: {str(e)}")