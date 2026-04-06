from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout


class SubModeChip(QFrame):
    clicked = Signal()

    def __init__(self, icon: str, name: str, description: str) -> None:
        super().__init__()

        self.setObjectName("subModeChip")
        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(58)

        layout = QHBoxLayout()
        layout.setContentsMargins(14, 10, 14, 10)
        layout.setSpacing(10)

        icon_label = QLabel(icon if icon else "•")
        icon_label.setObjectName("subModeIcon")
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setFixedWidth(28)

        name_label = QLabel(name)
        name_label.setObjectName("subModeName")

        layout.addWidget(icon_label)
        layout.addWidget(name_label)
        layout.addStretch()

        self.setLayout(layout)

    def mousePressEvent(self, event) -> None:
        self.clicked.emit()
        super().mousePressEvent(event)