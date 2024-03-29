import os
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import bar, hook
from libqtile.widget import GroupBox, Clock, CurrentLayout, CurrentLayoutIcon, Sep, Systray, Volume
from libqtile.layout.xmonad import MonadTall
from libqtile.layout.floating import Floating
from typing import List
mod = "mod4"
terminal = "gnome-terminal -- fish"
browser = "brave"
screen = ""

keys = [
	# Switch between windows in current stack pane
	Key(
		[mod], "j",
		lazy.layout.down()
	),
	Key(
		[mod], "k",
		lazy.layout.up()
	),
	Key(
		[mod], "l",
		lazy.layout.right()
	),
	Key(
		[mod], "h",
		lazy.layout.left()
	),

	# Move windows up or down in current stack
	Key(
		[mod, "shift"], "j",
		lazy.layout.shuffle_down()
	),
	Key(
		[mod, "shift"], "k",
		lazy.layout.shuffle_up()
	),
	Key(
		[mod, "shift"], "l",
		lazy.layout.swap_right()
	),
	Key(
		[mod, "shift"], "h",
		lazy.layout.swap_left()
	),


	# Toggle between split and unsplit sides of stack.
	# Split = all windows displayed
	# Unsplit = 1 window displayed, like Max layout, but still with
	# multiple stack panes
	Key(
		[mod], "Return", 
		lazy.spawn(terminal)
	),

	# Toggle between different layouts as defined below
	Key(
			[mod], "Tab", 
			lazy.next_layout()
		),
	Key(
			[mod, "shift"], "q", 
			lazy.window.kill()
		),

	Key(
			[mod, "shift"], "r", 
			lazy.restart()
		),
	Key(
			[mod, "shift"], "e", 
			lazy.shutdown()
		),
	Key(
			[mod], "d", 
			lazy.spawn("rofi -show run -font 'DaddyTimeMono Nerd Font 11' -width '30'  -fullscreen")
		),
	Key(
			[mod], "b", 
			lazy.spawn(browser)
		),
	Key(
			[mod], "c", 
			lazy.spawn("discord")
		),
	Key(
			[mod], "f", 
			lazy.window.toggle_fullscreen()
		),
	Key(
		["control"], "Up",
		lazy.spawn("amixer -c 0 -q set Master 2dB+")
	),
	Key(
		["control"], "Down",
		lazy.spawn("amixer -c 0 -q set Master 2dB-")
	),
	Key(
		[], "XF86AudioRaiseVolume",
		lazy.spawn("amixer -c 0 -q set Master 2dB+")
	),
	Key(
		[], "XF86AudioLowerVolume",
		lazy.spawn("amixer -c 0 -q set Master 2dB-")
	),
	Key(
		[], "XF86AudioMute",
		lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
	),
        Key(
            [mod], "v",
            lazy.spawn("code")
        ),
        Key(
            [], "Print",
                lazy.spawn("spectacle -r")
        ),
        Key(
                [mod], "i",
                lazy.spawn("Thunar")
        )]
	
colors = [["#292d3e", "#292d3e"], # panel background
		  ["#434758", "#434758"], # background for current screen tab
		  ["#ffffff", "#ffffff"], # font color for group names
		  ["#ff5555", "#ff5555"], # border line color for current tab
		  ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
		  ["#668bd7", "#668bd7"], # color for the even widgets
		  ["#e1acff", "#e1acff"]] # window name

groups = []
group_names = ["1", "2", "3", "4", "5", "6"]
group_labels = ["", "", "", "", "ﭮ", ""]
for i in range(len(group_names)):
	groups.append(
		Group(
			name=group_names[i],
			label = group_labels[i],
		))

for i in groups:
	keys.extend([

#CHANGE WORKSPACES
		Key([mod], i.name, lazy.group[i.name].toscreen()),

# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
		#Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
# MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
		Key([mod, "shift"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),
	])

"""
def init_group_names():
	return [("1: ", {'layout':'monadtall'}),
			("2: ", {'layout':'monadtall'}),
			("3: ", {'layout':'monadtall'}),
			("4: ", {'layout':'monadtall'}),
			("5: ", {'layout':'monadtall'}),
			("6: ", {'layout':'monadtall'})]

def init_groups():
	return [Group(name, **kwargs) for name, kwargs in group_names]

if __name__ in ["config", "__main__"]:
	group_names = init_group_names()
	groups = init_groups()
for i, (name, kwargs) in enumerate(group_names, 1):
	keys.append(Key([mod], str(i), lazy.group[name].toscreen()))      # Switch to another group
	keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))    # Send current window to another group
"""
layout_theme = {"border_width": 1,
				"margin": 6,
				"border_focus": "e1acff",
				"border_normal": "1D2330"
				}

layouts = [
	MonadTall(**layout_theme),
	Floating(**layout_theme),
]

widget_defaults = dict(
	font='Arial',
	fontsize=18,
	padding=3,
	background = colors[2]
)

def init_widgets_list():
	widgets_list = [
							
				GroupBox(
					   font = "DaddyTimeMono Nerd Font",
					   fontsize = 20,
					   margin_y = 3,
					   margin_x = 3,
					   padding_y = 5,
					   padding_x = 5,
					   borderwidth = 3,
					   active = colors[2],
					   inactive = colors[2],
					   rounded = False,
					   highlight_color = colors[1],
					   highlight_method = "line",
					   this_current_screen_border = colors[3],
					   this_screen_border = colors [4],
					   other_current_screen_border = colors[0],
					   other_screen_border = colors[0],
					   foreground = colors[2],
					   background = colors[0]
					   ),
				
			
				Sep(
					   linewidth = 720,
					   padding = 40,
					   foreground = colors[0],
					   background = colors[0]
					   ),

				CurrentLayoutIcon(
					   custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
					   foreground = colors[0],
					   background = colors[4],
					   padding = 0,
					   scale = 0.7
					   ),
				CurrentLayout(
					   foreground = colors[2],
					   background = colors[4],
					   padding = 5
					   ), 
				Clock(
					   foreground = colors[2],
					   background = colors[5],
					   format = "%A, %B %d  [ %H:%M ]"
					   ),
				
				Sep(
					   linewidth = 0,
					   padding = 10,
					   foreground = colors[0],
					   background = colors[5]
					   ),
                                Systray(
                                        background = colors[5]
                                ),
                                Sep(
                                        linewidth = 720,
                                        padding = 40,
                                        foreground = colors[0],
                                        background = colors[0]
                                )]
	return widgets_list


def init_widgets_screen1():
	widgets_screen1 = init_widgets_list()
	return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_screens():
	global screen
	screen = [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=25))]
	return screen
if __name__ in ["config", "__main__"]:
	screens = init_screens()
	widgets_list = init_widgets_list()
	widgets_screen1 = init_widgets_screen1()


# Drag floating layouts.
mouse = [
	Drag([mod], "Button1", lazy.window.set_position_floating(),
		start=lazy.window.get_position()),
	Drag([mod], "Button3", lazy.window.set_size_floating(),
		start=lazy.window.get_size()),
]

@hook.subscribe.client_new
def assign_app_group(client):
	d = {}
	d["1"] = ["Navigator", "qutebrowser", "brave-browser"]
	# d["2"] = []
	d["3"] = ["atom", "sublime_text", "code", "emacs"]
	d["4"] = ["VirtualBox Manager", "Transmission-gtk", "sqlitebrowser", "zoom", "virt-manager", "simplescreenrecorder"]
	d["5"] = ["discord"]
	d["6"] = ["spotify", "audacious"]
	wm_class = client.window.get_wm_class()[0]
	for i in range(len(d)):
		if wm_class in list(d.values())[i]:
			group = list(d.keys())[i]
			client.togroup(group)

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []
@hook.subscribe.startup_once
def autostart():
	processes = [
		['feh', '--bg-scale', '/home/maxi/Pictures/onedark.webp'],
		["discord"],
        ["wal", "-R"],
        ["picom"],
        ["imwheel"]
	]
	for p in processes:
		subprocess.Popen(p)

# wmname = "LG3D"
wmname = "Qtile"
