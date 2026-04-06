from app.models.action_type import ActionType
from app.models.mode import Action, Mode, SubMode


MODES: list[Mode] = [
    Mode(
        name="Gaming",
        emoji="🎮",
        description="Launch your games and gaming tools.",
        submodes=[
            SubMode(
                name="Dofus",
                description="Open Ankama Launcher, DofusGuide and Discord.",
                icon="🐉",
                actions=[
                    Action(
                        type=ActionType.OPEN_APP,
                        target=r"C:\Users\WIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Ankama\Ankama Launcher.lnk",
                        label="Opening Ankama Launcher",
                    ),
                    Action(
                        type=ActionType.OPEN_APP,
                        target=r"C:\Users\WIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\SBARBERI Enzo\DofusGuide\DofusGuide.appref-ms",
                        label="Opening DofusGuide",
                    ),
                    Action(
                        type=ActionType.OPEN_APP,
                        target=r"C:\Users\WIN\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk",
                        label="Opening Discord",
                    ),
                ],
            ),
            SubMode(
                name="LoL",
                description="Open your Riot setup.",
                icon="⚔️",
                actions=[],
            ),
        ],
    ),
    Mode(
        name="Cinema",
        emoji="🎬",
        description="Open media and entertainment tools.",
        submodes=[
            SubMode(
                name="Movie",
                description="Movie setup.",
                icon="🍿",
                actions=[],
            ),
            SubMode(
                name="YouTube",
                description="YouTube setup.",
                icon="▶️",
                actions=[],
            ),
        ],
    ),
    Mode(
        name="Study",
        emoji="📚",
        description="Focus and productive work.",
        submodes=[
            SubMode(
                name="Coding",
                description="Open dev tools.",
                icon="💻",
                actions=[],
            ),
        ],
    ),
]