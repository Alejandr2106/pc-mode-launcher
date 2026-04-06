import os
import webbrowser

from app.models.mode import Action


class LauncherService:
    def run_actions(self, actions: list[Action], status_callback=None) -> None:
        for action in actions:
            if status_callback:
                status_callback(f"Running {action.type}: {action.value}")

            if action.type == "open_app":
                self._open_app(action.value)
            elif action.type == "open_url":
                self._open_url(action.value)
            else:
                if status_callback:
                    status_callback(f"Unknown action type: {action.type}")

    def _open_app(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Path not found: {path}")

        os.startfile(path)

    def _open_url(self, url: str) -> None:
        webbrowser.open(url)