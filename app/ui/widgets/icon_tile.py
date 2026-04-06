from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout


class IconTile(QFrame):
    clicked = Signal()

    def __init__(self, emoji: str, label: str) -> None:
        super().__init__()

        self.setObjectName("iconTile")
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(80, 80)

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(6)

        icon_label = QLabel(emoji)
        icon_label.setAlignment(Qt.AlignCenter)
        icon_label.setObjectName("iconTileEmoji")

        text_label = QLabel(label)
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setObjectName("iconTileLabel")

        layout.addStretch()
        layout.addWidget(icon_label)
        layout.addWidget(text_label)
        layout.addStretch()

        self.setLayout(layout)

    def mousePressEvent(self, event) -> None:
        self.clicked.emit()
        super().mousePressEvent(event)