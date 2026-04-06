from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QSizePolicy, QWidget

from app.models.mode import Mode
from app.ui.widgets.submode_button import SubModeButton


class ModeCard(QFrame):
    submode_selected = Signal(str, str)

    def __init__(self, mode: Mode) -> None:
        super().__init__()

        self.mode = mode
        self.setObjectName("modeCard")
        self.setMinimumSize(260, 320)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self._setup_ui()

    def _setup_ui(self) -> None:
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        icon_label = QLabel(self.mode.emoji)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setObjectName("cardIcon")

        title_label = QLabel(self.mode.name)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("cardTitle")

        description_label = QLabel(self.mode.description)
        description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        description_label.setWordWrap(True)
        description_label.setObjectName("cardDescription")

        submodes_container = QWidget()
        submodes_container.setObjectName("submodesContainer")
        submodes_layout = QVBoxLayout()
        submodes_layout.setContentsMargins(0, 8, 0, 0)
        submodes_layout.setSpacing(10)

        for submode in self.mode.submodes:
            button = SubModeButton(submode.name)
            button.clicked_with_name.connect(self._handle_submode_click)
            submodes_layout.addWidget(button)

        submodes_layout.addStretch()
        submodes_container.setLayout(submodes_layout)

        layout.addWidget(icon_label)
        layout.addWidget(title_label)
        layout.addWidget(description_label)
        layout.addWidget(submodes_container, 1)

        self.setLayout(layout)

    def _handle_submode_click(self, submode_name: str) -> None:
        self.submode_selected.emit(self.mode.name, submode_name)