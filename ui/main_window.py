from PySide6.QtWidgets import QWidget, QLabel, QGridLayout

from constants.enums import StatusEnum
from widgets.button_motor_power import ButtonMotorPower
from controllers.main_controller import MainController
from ui.measure_window import MeasureWindow

class MainWindow(QWidget):

    status = StatusEnum.STOPPED
    motor_speed = 100

    def __init__(self):
        super().__init__()

        self.button_motor_power = ButtonMotorPower(parent=self)
        self.controller = MainController(view=self)

        self.setWindowTitle("Motor Control")
        self.showFullScreen()

        layout = QGridLayout()
        self.measure_window = MeasureWindow()

        self.label_status = QLabel(f"Status: {self.status.value}")
        self.label_motor_speed = QLabel(f"Motor Speed: {self.motor_speed} RPM")

        layout.addWidget(self.label_status, 0, 1)
        layout.addWidget(self.label_motor_speed, 0, 2)
        layout.addWidget(self.measure_window, 1, 1)
        layout.addWidget(self.button_motor_power, 0, 4)

        self.measure_window.setVisible(False)

        self.setLayout(layout)

