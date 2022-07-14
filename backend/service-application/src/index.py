import sys

import colorama
from colorama import Fore
from colorama import Style

from PySide6.QtWidgets import QApplication
from screens.main_controller import Main

from os import system


if __name__ == '__main__':
    app = QApplication()
    
    colorama.init()
    window = Main()
    window.showMaximized()
    
    system('clear')
    print(Fore.GREEN + Style.BRIGHT + "Application current in local")

    sys.exit(app.exec())