from libqtile import layout
from libqtile.config import Match
from .colors import *


pad = 8

layouts = [
    layout.MonadTall(margin=pad, border_focus=accent_color, border_normal=accent_dark),
    #layout.Columns(border_focus_stack='#d75f5f'),
    #layout.Max(),
    # Try more layouts by unleashing below layouts.
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    layout.Matrix(margin=pad, border_focus=accent_color, border_normal=accent_dark),
    layout.MonadWide(margin=pad, border_focus=accent_color, border_normal=accent_dark),
    layout.RatioTile(margin=pad, border_focus=accent_color, border_normal=accent_dark),
    layout.Tile(margin=pad, border_focus=accent_color, border_normal=accent_dark),
    #layout.TreeTab(),
    layout.VerticalTile(margin=pad, border_focus=accent_color, border_normal=accent_dark),
    #layout.Zoomy(),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
