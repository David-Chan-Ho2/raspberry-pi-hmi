from constants import Constants
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import math


class HMI:
    FONT = ("Arial", 18)

    def __init__(self):
        self.speed = 0
        self.isRunning = False
        self.initTk()
        self.setupUI()

    def initTk(self):
        self.root = ttk.Window(themename="darkly")
        self.root.title(Constants.TITLE)

        # Fullscreen mode (Raspberry Pi kiosk)
        self._initDisplay()

        # Press ESC to exit fullscreen (for development)
        self.root.bind("<Escape>", lambda e: self.root.attributes("-fullscreen", False))

        # Hide cursor for production
        # self.root.configure(cursor="none")

    def _initDisplay (self):
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        self.root.geometry("{0}x{1}+0+0".format(width, height))
        self.root.attributes("-fullscreen", True)

    def setupUI(self):

        self.titleLabel = ttk.Label(
            self.root,
            text="Motor Speed",
            font=self.FONT,
            bootstyle=PRIMARY
        )
        self.titleLabel.pack(pady=20)

        self.speedMeter = ttk.Meter(
            self.root,
            amountused=0,
            amounttotal=100,     # Max RPM (change if needed)
            metersize=280,
            metertype="semi",
            bootstyle=SUCCESS,
            subtext="RPM",
            interactive=False
        )
        self.speedMeter.pack(pady=30)

        self.startStopBtn = ttk.Button(
            self.root,
            text="Start",
            bootstyle=SUCCESS,
            command=self.toggleMotor
        )
        self.startStopBtn.pack(pady=10, padx=20)

    def run(self):
        self.root.mainloop()

    # -------------------------
    # Motor Control Logic
    # -------------------------

    def toggleMotor(self):
        if self.isRunning:
            self.stopMotor()
        else:
            self.startMotor()

    def startMotor(self):
        self.isRunning = True
        self.startStopBtn.configure(text="Stop", bootstyle=DANGER)
        self._exp_ramp(t=self.speed)

    def stopMotor(self):
        self.isRunning = False
        self.startStopBtn.configure(text="Start", bootstyle=SUCCESS)
        self.updateMeter()

    # -------------------------
    # Exponential Ramp
    # -------------------------

    def _exp_ramp(self, t):
        if not self.isRunning:
            return

        target = 100     # Max speed
        k = 0.08         # Acceleration factor

        # Exponential acceleration formula
        self.speed = int(target * (1 - math.exp(-k * t)))

        if self.speed >= target - 1:
            self.speed = target
            self.updateMeter()
            return

        self.updateMeter()
        self.root.after(50, lambda: self._exp_ramp(t + 1))

    def updateMeter(self):
        self.speedMeter.configure(amountused=self.speed)