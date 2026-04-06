from dataclasses import dataclass, field


@dataclass
class Action:
    type: str
    value: str


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