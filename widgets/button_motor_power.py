from PySide6.QtWidgets import QPushButton

class ButtonMotorPower(QPushButton):
    def __init__(self, parent=None):
        super().__init__("Power", parent)
        self.setCheckable(True)