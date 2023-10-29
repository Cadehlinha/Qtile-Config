import os
from libqtile.lazy import lazy
from libqtile.config import Key

# Define constants
mod = "mod4"
terminal = "xfce4-terminal"
browser = "firefox"
file_manager = "thunar"

keys = [

    # Spawn items
    Key([mod],
        "d",
        lazy.spawn(os.path.expanduser("~/.config/qtile/rofi/launchers/app_launcher/apps.sh")),
        desc="spawn rofi"),

    Key([mod, "shift"],
        "d",
        lazy.spawn("dmenu_run -p 'Search Apps:' -i -nb '#2f343f' -nf '#5294e2' -sb '#5294e2' -sf '#2f343f'"),
        desc="spawn dmenu"),

    Key(["control", "mod1"],
        "o",
        lazy.spawn(os.path.expanduser("~/.config/qtile/scripts/picom-toggle.sh")),
        desc="toggle picom"),

    Key([mod, "shift"],
        "x",
        lazy.spawn(os.path.expanduser("~/.config/qtile/rofi/launchers/powermenu/powermenu.sh")),
        desc="spawn rofi powermenu"),

    Key([mod],
        "w",
        lazy.spawn(browser),
        desc="spawn browser"),

    Key([mod],
        "n",
        lazy.spawn(file_manager),
        desc="spawn file manager"),

    Key([],
        "print",
        lazy.spawn("flameshot full"),
        desc="Take a full-screen shot with Flameshot"),

    Key(["control"],
        "print",
        lazy.spawn("flameshot gui"),
        desc="Take a custom screenshot with Flameshot's GUI"),

    Key([mod],
        "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"),

    Key([mod],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"),

    Key([mod],
        "Down",
        lazy.layout.shuffle_down(),
        desc="Move window down"),

    Key([mod], 
        "Up",
        lazy.layout.shuffle_up(),
        desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "shift"],
        "Left",
        lazy.layout.grow(),
        desc="Grow window"),

    Key([mod, "shift"],
        "Right",
        lazy.layout.shrink(),
        desc="Shrink window"),

    Key([mod, "shift"],
        "Down",
        lazy.layout.normalize(),
        desc="Reset all window sizes"),

    # Standard keybinds (EG: Kill Window, Switch Layout(s).. etc)
    Key([mod],
        "q",
        lazy.window.kill(),
        desc="Kill focused window"),

    Key([mod],
        "space",
        lazy.next_layout()),

    Key([mod, "shift"],
        "space",
        lazy.window.toggle_floating(),
        desc="Toggle floating"),

    Key([mod],
        "l",
        lazy.spawn("physlock -p 'Locked Session'"),
        desc="Lock the session"),

    Key([mod, "shift"],
        "r",
        lazy.restart(),
        desc="Restart Qtile"),
]
