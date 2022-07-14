from PySide6.QtWidgets import QWidget
from widgets.main import Ui_Form

class Main(QWidget, Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)