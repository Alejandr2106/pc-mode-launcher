from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QFrame, QLabel, QHBoxLayout, QPushButton


class TopBar(QFrame):
    back_requested = Signal()
    close_requested = Signal()

    def __init__(self, title: str, subtitle: str = "", show_back: bool = False) -> None:
        super().__init__()

        self.setObjectName("topBar")

        layout = QHBoxLayout()
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(8)

        self.back_button = QPushButton("←")
        self.back_button.setObjectName("iconButton")
        self.back_button.setVisible(show_back)
        self.back_button.setCursor(Qt.PointingHandCursor)
        self.back_button.clicked.connect(self.back_requested.emit)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("topBarTitle")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.close_button = QPushButton("✕")
        self.close_button.setObjectName("iconButton")
        self.close_button.setCursor(Qt.PointingHandCursor)
        self.close_button.clicked.connect(self.close_requested.emit)

        layout.addWidget(self.back_button)
        layout.addStretch()
        layout.addWidget(self.title_label)
        layout.addStretch()
        layout.addWidget(self.close_button)

        self.setLayout(layout)

    def set_content(self, title: str) -> None:
        self.title_label.setText(title)

    def set_back_visible(self, visible: bool) -> None:
        self.back_button.setVisible(visible)