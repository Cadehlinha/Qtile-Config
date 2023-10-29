from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod


groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        # mod4 + letter of group = switch to group
        Key([mod],
            i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod4 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"],
            i.name,
            lazy.window.togroup(i.name, switch_group=False),
            desc="Switch to & move focused window to group {}".format(i.name)),
    ])
