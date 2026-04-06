from PySide6.QtCore import Signal
from PySide6.QtWidgets import QGridLayout, QWidget

from app.models.mode import Mode
from app.ui.widgets.icon_tile import IconTile


class HomePage(QWidget):
    mode_selected = Signal(object)

    def __init__(self, modes: list[Mode]) -> None:
        super().__init__()
        self.modes = modes
        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QGridLayout()
        layout.setContentsMargins(6, 6, 6, 6)
        layout.setHorizontalSpacing(12)
        layout.setVerticalSpacing(12)

        row = 0
        col = 0

        for mode in self.modes:
            tile = IconTile(mode.emoji, mode.name)
            tile.clicked.connect(lambda checked=False, selected_mode=mode: self.mode_selected.emit(selected_mode))
            layout.addWidget(tile, row, col)

            col += 1
            if col > 1:
                col = 0
                row += 1

        self.setLayout(layout)