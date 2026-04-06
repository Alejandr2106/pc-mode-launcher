from PySide6.QtCore import Signal
from PySide6.QtWidgets import QPushButton


class SubModeButton(QPushButton):
    clicked_with_name = Signal(str)

    def __init__(self, submode_name: str) -> None:
        super().__init__(submode_name)
        self.submode_name = submode_name
        self.setObjectName("subModeButton")
        self.clicked.connect(self._emit_name)

    def _emit_name(self) -> None:
        self.clicked_with_name.emit(self.submode_name)