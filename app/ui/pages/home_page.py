from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout

from app.models.mode import Mode
from app.ui.widgets.icon_tile import IconTile


class HomePage(QWidget):
    mode_selected = Signal(object)

    def __init__(self, modes: list[Mode]) -> None:
        super().__init__()
        self.modes = modes
        self._setup_ui()

    def _setup_ui(self) -> None:
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        column_layout = QVBoxLayout()
        column_layout.setSpacing(10)

        for mode in self.modes:
            tile = IconTile(mode.emoji, mode.name)
            tile.clicked.connect(
                lambda checked=False, selected_mode=mode:
                self.mode_selected.emit(selected_mode)
            )
            column_layout.addWidget(tile)

        column_layout.addStretch()

        center_layout = QHBoxLayout()
        center_layout.addStretch()
        center_layout.addLayout(column_layout)
        center_layout.addStretch()

        main_layout.addLayout(center_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)