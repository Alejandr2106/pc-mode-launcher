from app.models.mode import Action, Mode, SubMode
from app.models.action_type import ActionType

MODES: list[Mode] = [
    Mode(
        name="Gaming",
        emoji="🎮",
        description="Launch your gaming setup with your favorite games and tools.",
        submodes=[
            SubMode(
                name="Dofus",
                description="Open Ankama Launcher, DofusGuide and Discord.",
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
                name="League of Legends",
                description="Open your Riot setup.",
                actions=[],
            ),
        ],
    ),
    Mode(
        name="Cinema",
        emoji="🎬",
        description="Prepare your entertainment environment quickly.",
        submodes=[
            SubMode(
                name="Movie",
                description="Open your movie apps.",
                actions=[],
            ),
            SubMode(
                name="YouTube",
                description="Open browser and media environment.",
                actions=[],
            ),
        ],
    ),
    Mode(
        name="Study",
        emoji="📚",
        description="Set up your environment for focus and learning.",
        submodes=[
            SubMode(
                name="Coding",
                description="Open development tools.",
                actions=[],
            ),
        ],
    ),
]