from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from app.config.modes_data import MODES
from app.core.launcher_service import LauncherService
from app.models.mode import SubMode
from app.ui.styles.main_styles import MAIN_STYLES
from app.ui.widgets.mode_card import ModeCard


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.launcher_service = LauncherService()

        self.setWindowTitle("PC Mode Launcher")
        self.resize(1200, 720)

        self._setup_ui()
        self._apply_styles()

    def _setup_ui(self) -> None:
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(20)
        central_widget.setLayout(main_layout)

        header = self._build_header()
        cards_section = self._build_cards_section()
        status_bar = self._build_status_section()

        main_layout.addWidget(header)
        main_layout.addWidget(cards_section, 1)
        main_layout.addWidget(status_bar)

    def _build_header(self) -> QFrame:
        header = QFrame()
        header.setObjectName("header")

        layout = QVBoxLayout()
        layout.setContentsMargins(24, 20, 24, 20)
        layout.setSpacing(6)

        title = QLabel("PC Mode Launcher")
        title.setObjectName("windowTitle")

        subtitle = QLabel("Choose a mode and then a specific setup")
        subtitle.setObjectName("windowSubtitle")

        layout.addWidget(title)
        layout.addWidget(subtitle)
        header.setLayout(layout)

        return header

    def _build_cards_section(self) -> QWidget:
        container = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(18)
        container.setLayout(layout)

        for mode in MODES:
            card = ModeCard(mode)
            card.submode_selected.connect(self._handle_submode_selected)
            layout.addWidget(card)

        return container

    def _build_status_section(self) -> QFrame:
        status_frame = QFrame()
        status_frame.setObjectName("statusFrame")

        layout = QHBoxLayout()
        layout.setContentsMargins(18, 14, 18, 14)

        self.status_label = QLabel("Status: Ready")
        self.status_label.setObjectName("statusLabel")

        layout.addWidget(self.status_label)
        status_frame.setLayout(layout)

        return status_frame

    def _handle_submode_selected(self, mode_name: str, submode_name: str) -> None:
        submode = self._find_submode(mode_name, submode_name)

        if submode is None:
            self.status_label.setText(f"Status: {mode_name} > {submode_name} not found")
            return

        self.status_label.setText(f"Status: launching {mode_name} > {submode_name}")

        try:
            self.launcher_service.run_actions(
                submode.actions,
                status_callback=self._update_status,
            )
            self.status_label.setText(f"Status: launched {mode_name} > {submode_name}")
        except Exception as error:
            self.status_label.setText(f"Status: error - {error}")

    def _find_submode(self, mode_name: str, submode_name: str) -> SubMode | None:
        for mode in MODES:
            if mode.name == mode_name:
                for submode in mode.submodes:
                    if submode.name == submode_name:
                        return submode
        return None

    def _update_status(self, message: str) -> None:
        self.status_label.setText(f"Status: {message}")

    def _apply_styles(self) -> None:
        self.setStyleSheet(MAIN_STYLES)