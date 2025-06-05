from PyQt5.QtWidgets import QApplication
from capture import ScreenshotTool
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScreenshotTool()
    window.show()
    
    # 确保窗口关闭时完全退出应用
    def on_window_close():
        # 确保所有窗口都已关闭
        for widget in app.topLevelWidgets():
            widget.close()
        # 强制退出应用
        app.quit()
        # 确保Python进程退出
        sys.exit(0)
    
    # 连接窗口关闭信号
    window.destroyed.connect(on_window_close)
    
    # 设置应用退出时的处理
    app.aboutToQuit.connect(lambda: sys.exit(0))
    
    # 执行应用主循环
    ret = app.exec_()
    
    # 确保完全退出
    sys.exit(ret)