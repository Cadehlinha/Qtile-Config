#!/bin/sh

function run {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

feh --bg-scale ~/.config/qtile/wallpaper/fox.png
nm-applet & disown
# test with function so it wont
# exit right after running
run volumeicon &

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown
# Python version if you'd prefer it
#python ~/.config/qtile/scripts/check_battery.py & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME

~/.config/qtile/scripts/picom-toggle.sh & disown