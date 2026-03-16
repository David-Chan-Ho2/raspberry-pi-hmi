from PySide6.QtCore import QObject

from constants.enums import StatusEnum

class MainController(QObject):

    def __init__(self, view):
        super().__init__()
        self.view = view
        self.view.button_motor_power.toggled.connect(self.toggle_motor)

    def toggle_motor(self, is_checked):
        if is_checked:
            self.view.status = StatusEnum.RUNNING
        else:
            self.view.status = StatusEnum.STOPPED

        self.update_ui()

    def update_ui(self):
        self.view.label_status.setText(f"Status: {self.view.status.value}")
        self.view.measure_window.setVisible(self.view.status == StatusEnum.RUNNING)