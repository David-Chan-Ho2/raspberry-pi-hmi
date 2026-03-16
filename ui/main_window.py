from PySide6.QtWidgets import QWidget, QLabel, QGridLayout

from widgets.button_motor_power import ButtonMotorPower
from controllers.main_controller import MainController
from constants.enums import StatusEnum

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 100)
        self.status = StatusEnum.STOPPED
        self.motor_speed = 100
        self.voltage = 0.0
        self.current = 0.0
        self.power = 0.0

        self.button_motor_power = ButtonMotorPower(parent=self)
        self.controller = MainController(view=self)

        self.setWindowTitle("Motor Control")
        
        layout = QGridLayout()

        self.label_status = QLabel(f"Status: {self.status.value}")
        self.label_motor_speed = QLabel(f"Motor Speed: {self.motor_speed} RPM")
        self.label_voltage = QLabel()
        self.label_current = QLabel()
        self.label_power = QLabel()

        layout.addWidget(self.label_status, 0, 0)
        layout.addWidget(self.label_motor_speed, 0, 1)
        layout.addWidget(self.button_motor_power, 0, 2)

        layout.addWidget(self.label_voltage, 1, 0)
        layout.addWidget(self.label_current, 1, 1)
        layout.addWidget(self.label_power, 1, 2)

        self.setLayout(layout)

        self.controller.refresh_labels()

        self.showFullScreen()