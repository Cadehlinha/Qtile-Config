from libqtile import bar, qtile
from libqtile.config import Screen
from libqtile import widget
from .colors import *
import os


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=bg_color
                ),

                widget.GroupBox(
                    highlight_method="block",
                    this_screen_border=accent_color,
                    this_current_screen_border=accent_color,
                    active="#ffffff",
                    inactive="#ffffff",
                    background=bg_color,
                    hide_unused=True
                ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=bg_color
                ),

                widget.Spacer(),

                widget.WindowName(
                    foreground=fg_color,
                    width=bar.CALCULATED
                ),

                widget.Spacer(),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=bg_color
                ),

                widget.Systray(
                    icon_size=26,
                    background=bg_color
                ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=bg_color
                ),
            ],

            30,  # height in px
            background=bar_bg,  # background color
            margin=8, # bar margin
            border_color=accent_color, # bar border color
            border_width=1 # bar border width
        ),

        bottom=bar.Bar(
            [
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=bg_color
                ),

                widget.CurrentLayoutIcon(
                    scale=0.70,
                    background=bg_color
                ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=bg_color
                ),

                widget.Spacer(),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=bg_color
                ),

                widget.Clock(
                    format="󰥔 %I:%M:%S %p - %a %b %d",
                    foreground=fg_color,
                    background="#2f343f"
                ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=bg_color
                ),
            ],

            30,  # height in px
            background=bar_bg,  # background color
            margin=8, # bar margin
            border_color=accent_color, # bar border color
            border_width=1 # bar border width
        ),
    ),
]