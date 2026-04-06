MAIN_STYLES = """
    QMainWindow {
        background-color: transparent;
    }

    QWidget#rootBackground {
        background-color: transparent;
    }

    QFrame#appShell {
        background-color: #0b0f17;
        border: 1px solid #1a2332;
        border-radius: 28px;
    }

    QWidget {
        background-color: transparent;
        color: #f5f7fb;
        font-family: "Segoe UI";
    }

    QFrame#topBar {
        background-color: transparent;
        border: none;
    }

    QLabel#topBarTitle {
        font-size: 15px;
        font-weight: 700;
        color: #f7fbff;
    }

    QPushButton#iconButton {
        background-color: #121927;
        border: 1px solid #233049;
        border-radius: 14px;
        min-width: 32px;
        max-width: 32px;
        min-height: 32px;
        max-height: 32px;
        color: #eef4ff;
        font-size: 14px;
    }

    QPushButton#iconButton:hover {
        background-color: #182133;
        border: 1px solid #5da2ff;
    }

    QFrame#iconTile {
        background-color: #101724;
        border: 1px solid #1f2b40;
        border-radius: 24px;
    }

    QFrame#iconTile:hover {
        background-color: #141d2d;
        border: 1px solid #5da2ff;
    }

    QLabel#iconTileEmoji {
        font-size: 30px;
    }

    QLabel#iconTileLabel {
        font-size: 12px;
        font-weight: 600;
        color: #dce7ff;
    }

    QFrame#subModeChip {
        background-color: #101724;
        border: 1px solid #1f2b40;
        border-radius: 18px;
    }

    QFrame#subModeChip:hover {
        background-color: #141d2d;
        border: 1px solid #5da2ff;
    }

    QLabel#subModeIcon {
        font-size: 18px;
        color: #ffffff;
    }

    QLabel#subModeName {
        font-size: 13px;
        font-weight: 700;
        color: #eef4ff;
    }

    QFrame#statusBar {
        background-color: #101724;
        border: 1px solid #1f2b40;
        border-radius: 16px;
    }

    QLabel#statusLabel {
        font-size: 11px;
        color: #aebddb;
    }
"""