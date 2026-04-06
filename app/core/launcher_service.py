import os
import time
import webbrowser

from app.models.mode import Action
from app.models.action_type import ActionType


class LauncherService:
    def run_actions(self, actions: list[Action], status_callback=None) -> None:
        for action in actions:
            if not action.enabled:
                continue

            if action.label and status_callback:
                status_callback(action.label)

            if action.delay_ms > 0:
                time.sleep(action.delay_ms / 1000)

            if action.type == ActionType.OPEN_APP:
                self._open_app(action.target)

            elif action.type == ActionType.OPEN_URL:
                self._open_url(action.target)

            elif action.type == ActionType.CLOSE_PROCESS:
                self._close_process(action.target)

            elif action.type == ActionType.WAIT:
                pass

            else:
                if status_callback:
                    status_callback(f"Unknown action type: {action.type}")

    def _open_app(self, path: str) -> None:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Path not found: {path}")

        os.startfile(path)

    def _open_url(self, url: str) -> None:
        webbrowser.open(url)

    def _close_process(self, process_name: str) -> None:
        os.system(f"taskkill /F /IM {process_name} >nul 2>&1")