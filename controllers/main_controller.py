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

    def refresh_labels(self):
        self.view.power = self.view.voltage * self.view.current
        self.view.label_voltage.setText(f"Voltage: {self.view.voltage:.2f} V")
        self.view.label_current.setText(f"Current: {self.view.current:.3f} A")
        self.view.label_power.setText(f"Power: {self.view.power:.4f} W")

    def set_measurements(self, voltage, current):
        self.view.voltage = voltage
        self.view.current = current
        self.view.refresh_labels()