from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import (
    QFrame,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
    QLabel,
    QHBoxLayout,
)

from app.config.modes_data import MODES
from app.core.launcher_service import LauncherService
from app.models.mode import Mode, SubMode
from app.ui.pages.category_page import CategoryPage
from app.ui.pages.home_page import HomePage
from app.ui.styles.main_styles import MAIN_STYLES
from app.ui.widgets.top_bar import TopBar


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.launcher_service = LauncherService()
        self.current_mode: Mode | None = None
        self._drag_position = QPoint()

        self.setWindowTitle("PC Mode Launcher")
        self.resize(300, 460)
        self.setMinimumSize(260, 380)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self._setup_ui()
        self._apply_styles()

    def _setup_ui(self) -> None:
        central_widget = QWidget()
        central_widget.setObjectName("rootBackground")
        self.setCentralWidget(central_widget)

        outer_layout = QVBoxLayout()
        outer_layout.setContentsMargins(12, 12, 12, 12)
        outer_layout.setSpacing(0)
        central_widget.setLayout(outer_layout)

        self.shell = QFrame()
        self.shell.setObjectName("appShell")

        shell_layout = QVBoxLayout()
        shell_layout.setContentsMargins(14, 14, 14, 14)
        shell_layout.setSpacing(12)
        self.shell.setLayout(shell_layout)

        self.top_bar = TopBar(
            title="Launcher",
            subtitle="",
            show_back=False,
        )
        self.top_bar.back_requested.connect(self._show_home)
        self.top_bar.close_requested.connect(self.close)

        self.stack = QStackedWidget()

        self.home_page = HomePage(MODES)
        self.home_page.mode_selected.connect(self._show_category)

        self.category_page = CategoryPage()
        self.category_page.submode_selected.connect(self._handle_submode_selected)

        self.stack.addWidget(self.home_page)
        self.stack.addWidget(self.category_page)

        status_bar = self._build_status_bar()

        shell_layout.addWidget(self.top_bar)
        shell_layout.addWidget(self.stack, 1)
        # shell_layout.addWidget(status_bar)

        outer_layout.addWidget(self.shell)

    def _build_status_bar(self) -> QFrame:
        frame = QFrame()
        frame.setObjectName("statusBar")

        layout = QHBoxLayout()
        layout.setContentsMargins(12, 10, 12, 10)

        self.status_label = QLabel("Status: Ready")
        self.status_label.setObjectName("statusLabel")

        layout.addWidget(self.status_label)
        frame.setLayout(layout)

        return frame

    def _show_category(self, mode: Mode) -> None:
        self.current_mode = mode
        self.category_page.set_mode(mode)

        self.top_bar.set_back_visible(True)
        self.top_bar.set_content(mode.name)
        self.stack.setCurrentWidget(self.category_page)
        self._update_status(f"{mode.name} selected")

    def _show_home(self) -> None:
        self.current_mode = None
        self.stack.setCurrentWidget(self.home_page)

        self.top_bar.set_back_visible(False)
        self.top_bar.set_content("Launcher")
        self._update_status("Ready")

    def _handle_submode_selected(self, mode_name: str, submode_name: str) -> None:
        submode = self._find_submode(mode_name, submode_name)

        if submode is None:
            self._update_status(f"{mode_name} > {submode_name} not found")
            return

        self._update_status(f"Launching {mode_name} > {submode_name}")

        try:
            self.launcher_service.run_actions(
                submode.actions,
                status_callback=self._update_status,
            )
            self._update_status(f"Launched {mode_name} > {submode_name}")
        except Exception as error:
            self._update_status(f"Error: {error}")

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

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.LeftButton:
            self._drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event) -> None:
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_position)
            event.accept()