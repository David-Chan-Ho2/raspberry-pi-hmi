from PySide6.QtWidgets import QWidget, QLabel, QGridLayout

from widgets.button_motor_power import ButtonMotorPower
from controllers.main_controller import MainController
from constants.enums import StatusEnum
from ui.measure_window import MeasureWindow

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.status = StatusEnum.STOPPED
        self.motor_speed = 100

        self.button_motor_power = ButtonMotorPower(parent=self)
        self.controller = MainController(view=self)

        self.setWindowTitle("Motor Control")
        
        layout = QGridLayout()
        self.measure_window = MeasureWindow()
        self.measure_window.setVisible(False)

        self.label_status = QLabel(f"Status: {self.status.value}")
        self.label_motor_speed = QLabel(f"Motor Speed: {self.motor_speed} RPM")

        layout.addWidget(self.label_status, 0, 0)
        layout.addWidget(self.label_motor_speed, 0, 1)
        layout.addWidget(self.button_motor_power, 0, 2)
        layout.addWidget(self.measure_window, 1, 0, 1, 3)

        self.setLayout(layout)
        
        self.showFullScreen()