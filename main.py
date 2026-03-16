import sys
import logging
import traceback
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

app = QApplication(sys.argv)

logging.basicConfig(
    filename='/home/dho/hmi_debug.log',
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s:%(message)s'
)

# with open("/home/dho/styles/styles.qss", "r") as f:
#     app.setStyleSheet(f.read())

try:
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
except Exception as e:
    logging.error("HMI Crashed!")
    logging.error(traceback.format_exc())
    sys.exit(1)

