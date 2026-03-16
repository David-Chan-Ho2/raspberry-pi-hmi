from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class MeasureWindow(QWidget):
    voltage = 10
    current = 3E-3
    power = voltage * current

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label_voltage = QLabel(f"Voltage: {self.voltage} V")
        self.label_current = QLabel(f"Current: {self.current} A")
        self.label_power = QLabel(f"Power: {self.power} W")

        layout.addWidget(self.label_voltage)
        layout.addWidget(self.label_current)
        layout.addWidget(self.label_power)

        self.setLayout(layout)
    
    def refresh_labels(self):
        self.power = self.voltage * self.current
        self.label_voltage.setText(f"Voltage: {self.voltage} V")
        self.label_current.setText(f"Current: {self.current} A")
        self.label_power.setText(f"Power: {self.power} W")

    def set_measurements(self, voltage, current):
        self.voltage = voltage
        self.current = current
        self.refresh_labels()
