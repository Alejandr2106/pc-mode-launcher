from enum import Enum


class ActionType(str, Enum):
    OPEN_APP = "open_app"
    OPEN_URL = "open_url"
    CLOSE_PROCESS = "close_process"
    WAIT = "wait"