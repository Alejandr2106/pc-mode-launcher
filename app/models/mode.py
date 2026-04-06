from dataclasses import dataclass, field
from app.models.action_type import ActionType

@dataclass
class Action:
    type: ActionType
    target: str
    label: str = ""
    enabled: bool = True
    delay_ms: int = 0


@dataclass
class SubMode:
    name: str
    description: str = ""
    actions: list[Action] = field(default_factory=list)


@dataclass
class Mode:
    name: str
    emoji: str
    description: str
    submodes: list[SubMode] = field(default_factory=list)