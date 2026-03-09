from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from constants.enums import StatusEnum
from widgets.button_motor_power import ButtonMotorPower
from controllers.main_controller import MainController

class MainWindow(QWidget):

    status = StatusEnum.STOPPED

    def __init__(self):
        super().__init__()

        self.button_motor_power = ButtonMotorPower()
        self.controller = MainController(view=self, button=self.button_motor_power)

        self.setWindowTitle("Motor Control")
        # self.showFullScreen()
        self.resize(800, 600)

        layout = QVBoxLayout()

        self.label_status = QLabel(f"Status: {self.status.value}")


        layout.addWidget(self.label_status)
        layout.addWidget(self.button_motor_power)

        self.setLayout(layout)

  