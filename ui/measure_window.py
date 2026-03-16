from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

class MeasureWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 100)
        
        self.voltage = 0.0
        self.current = 0.0
        self.power = 0.0

        layout = QVBoxLayout()

        self.label_voltage = QLabel()
        self.label_current = QLabel()
        self.label_power = QLabel()

        layout.addWidget(self.label_voltage)
        layout.addWidget(self.label_current)
        layout.addWidget(self.label_power)

        self.setLayout(layout)
        self.refresh_labels() 
        

    def refresh_labels(self):
        self.power = self.voltage * self.current
        self.label_voltage.setText(f"Voltage: {self.voltage:.2f} V")
        self.label_current.setText(f"Current: {self.current:.3f} A")
        self.label_power.setText(f"Power: {self.power:.4f} W")

    def set_measurements(self, voltage, current):
        self.voltage = voltage
        self.current = current
        self.refresh_labels()