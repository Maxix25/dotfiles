import os
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List
mod = "mod4"

@lazy.function
def window_to_prev_group(qtile):
	if qtile.currentWindow is not None:
		i = qtile.groups.index(qtile.currentGroup)
		qtile.currentWindow.togroup(qtile.groups[i - 1].name)

@lazy.function
def window_to_next_group(qtile):
	if qtile.currentWindow is not None:
		i = qtile.groups.index(qtile.currentGroup)
		qtile.currentWindow.togroup(qtile.groups[i + 1].name)

keys = [
	# Switch between windows in current stack pane
	Key(
		[mod], "Down",
		lazy.layout.down()
	),
	Key(
		[mod], "Up",
		lazy.layout.up()
	),
	Key(
		[mod], "Right",
		lazy.layout.right()
	),
	Key(
		[mod], "Left",
		lazy.layout.left()
	),

	# Move windows up or down in current stack
	Key(
		[mod, "shift"], "Down",
		lazy.layout.shuffle_down()
	),
	Key(
		[mod, "shift"], "Up",
		lazy.layout.shuffle_up()
	),
	Key(
		[mod, "shift"], "Right",
		lazy.layout.swap_right()
	),
	Key(
		[mod, "shift"], "Left",
		lazy.layout.swap_left()
	),

	# Switch window focus to other pane(s) of stack
	Key(
		[mod], "space",
		lazy.layout.next()
	),

	# Swap panes of split stack
	Key(
		[mod, "shift"], "space",
		lazy.layout.rotate()
	),

	# Toggle between split and unsplit sides of stack.
	# Split = all windows displayed
	# Unsplit = 1 window displayed, like Max layout, but still with
	# multiple stack panes
	Key(
		[mod, "shift"], "Return",
		lazy.layout.toggle_split()
	),
	Key(
			[mod], "Return", 
			lazy.spawn("mate-terminal")
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
			lazy.spawn("rofi -show run -font 'Comic Sans 10' -width '30'  -fullscreen")
		),
	Key(
			[mod], "b", 
			lazy.spawn("firefox")
		),
	Key(
			[mod], "c", 
			lazy.spawn("discord")
		),
	Key(
			[mod], "f", 
			lazy.window.toggle_fullscreen()
		)]

colors = [["#292d3e", "#292d3e"], # panel background
		  ["#434758", "#434758"], # background for current screen tab
		  ["#ffffff", "#ffffff"], # font color for group names
		  ["#ff5555", "#ff5555"], # border line color for current tab
		  ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
		  ["#668bd7", "#668bd7"], # color for the even widgets
		  ["#e1acff", "#e1acff"]] # window name
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
groups = []
group_names = ["1", "2", "3", "4", "5", "6"]
group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]
for i in range(len(group_names)):
	groups.append(
		Group(
			name=group_names[i],
			layout=group_layouts[i].lower(),
		))

for i in groups:
	keys.extend([

#CHANGE WORKSPACES
		Key([mod], i.name, lazy.group[i.name].toscreen()),
		Key([mod], "Tab", lazy.screen.next_group()),
		Key(["mod1"], "Tab", lazy.screen.next_group()),
		Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

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
layout_theme = {"border_width": 2,
				"margin": 6,
				"border_focus": "e1acff",
				"border_normal": "1D2330"
				}

layouts = [
	layout.MonadTall(**layout_theme),
]

widget_defaults = dict(
	font='Arial',
	fontsize=18,
	padding=3,
		background = colors[2]
)

def init_widgets_list():
	widgets_list = [
			  widget.Sep(
					   linewidth = 0,
					   padding = 6,
					   foreground = colors[2],
					   background = colors[0]
					   ),
			  widget.GroupBox(
					   font = "Ubuntu Bold",
					   fontsize = 14,
					   margin_y = 3,
					   margin_x = 0,
					   padding_y = 5,
					   padding_x = 3,
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
			  widget.Prompt(
					   prompt = prompt,
					   font = "Ubuntu Mono 10",
					   padding = 10,
					   foreground = colors[3],
					   background = colors[1]
					   ),
			  widget.Sep(
					   linewidth = 730,
					   padding = 40,
					   foreground = colors[0],
					   background = colors[0]
					   ),
			  widget.CurrentLayoutIcon(
					   custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
					   foreground = colors[0],
					   background = colors[4],
					   padding = 0,
					   scale = 0.7
					   ),
			  widget.CurrentLayout(
					   foreground = colors[2],
					   background = colors[4],
					   padding = 5
					   ), 
			  widget.Clock(
					   foreground = colors[2],
					   background = colors[5],
					   format = "%A, %B %d  [ %H:%M ]"
					   ),
			  widget.Sep(
					   linewidth = 0,
					   padding = 10,
					   foreground = colors[0],
					   background = colors[5]
					   )]
	return widgets_list


def init_widgets_screen1():
	widgets_screen1 = init_widgets_list()
	return widgets_screen1                       # Slicing removes unwanted widgets on Monitors 1,3

def init_screens():
	return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]
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
	Click([mod], "Button2", lazy.window.bring_to_front())
]

@hook.subscribe.client_new
def assign_app_group(client):
	d = {}
	d["1"] = ["Navigator", "Firefox""navigator", "firefox" ]
	d["2"] = ["mate-terminal", "Mate-terminal"]
	d["3"] = ["Atom", "Sublime_text", "Code", "Discord","atom", "sublime_text", "code"]
	d["4"] = ["VirtualBox Manager", "VirtualBox Machine","virtualbox manager", "virtualbox machine"]
	d["5"] = ["Discord"]
	d["6"] = ["Spotify_client" ]
	wm_class = client.window.get_wm_class()[0]
	for i in range(len(d)):
		if wm_class in list(d.values())[i]:
			group = list(d.keys())[i]
			client.togroup(group)
			if wm_class == "Mate-terminal" or wm_class == "mate-terminal":
				group = list(d.keys())[i]
				client.togroup(group)
				client.group.cmd_toscreen()


dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating()
auto_fullscreen = True
focus_on_window_activation = "smart"
extentions = []
@hook.subscribe.startup_once
def autostart():
	home = os.path.expanduser('~/.config/qtile/autostart.sh')
	subprocess.call([home])


wmname = "LG3D"
