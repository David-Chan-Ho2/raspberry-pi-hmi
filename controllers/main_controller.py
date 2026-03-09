from PySide6.QtCore import QObject

from constants.enums import StatusEnum

class MainController(QObject):

    def __init__(self, view, button):
        super().__init__()
        self.view = view
        self.button = button
        self.button.toggled.connect(self.button_motor_power_clicked)

    def button_motor_power_clicked(self, is_checked):
        if is_checked:
            self.view.status = StatusEnum.RUNNING
        else:
            self.view.status = StatusEnum.STOPPED
        
        self.view.label_status.setText(f"Status: {self.view.status.value}")