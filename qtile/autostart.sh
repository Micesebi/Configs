#!/bin/sh

function run {
	if ! pgrep $1 ;
	then
		$@&
	fi
}







picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed &
flameshot &
variety &

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown &

# Start welcome
eos-welcome & disown &

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME &
