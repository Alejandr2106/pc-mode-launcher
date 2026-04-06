from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget

from app.models.mode import Mode
from app.ui.widgets.submode_chip import SubModeChip


class CategoryPage(QWidget):
    submode_selected = Signal(str, str)

    def __init__(self) -> None:
        super().__init__()
        self.current_mode: Mode | None = None

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(6, 6, 6, 6)
        self.layout.setSpacing(10)
        self.layout.addStretch()

        self.setLayout(self.layout)

    def set_mode(self, mode: Mode) -> None:
        self.current_mode = mode
        self._clear_submodes()

        insert_index = 0
        for submode in mode.submodes:
            chip = SubModeChip(
                icon=submode.icon,
                name=submode.name,
                description=submode.description,
            )
            chip.clicked.connect(
                lambda checked=False, mode_name=mode.name, submode_name=submode.name:
                self.submode_selected.emit(mode_name, submode_name)
            )
            self.layout.insertWidget(insert_index, chip)
            insert_index += 1

        self.layout.addStretch()

    def _clear_submodes(self) -> None:
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()