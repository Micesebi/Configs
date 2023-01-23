from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background="#ff7faa"),
                widget.Sep(padding=4, linewidth=0, background="#ff7faa"),
		widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#faff74',
		       Background='#ff99bb',
                       ),  
	        widget.GroupBox(
                       highlight_method='line',
                       this_screen_border="#ffffff",
                       this_current_screen_border="#ff54ef",
                       active="#f51200",
                       inactive="#fd14ff",
                       background="#faff74"),
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#faff74'
                       ),    
                widget.Prompt(),
                widget.Spacer(length=5),
                widget.WindowName(foreground='#ffffff',fmt='{}'),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
		widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#ff00bb',
                       ), 
                widget.CurrentLayoutIcon(
			scale=0.75,
			background='#ff00bb',
			),
                widget.Systray(
		       icon_size = 20,
                       foreground='#faff74',
                       background='#ff00bb',
		       ),			
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#faff74',
                       background='#ff00bb',
			), 
                volume,
                widget.TextBox(                                                                    
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#faff74',
		       Background='#ff99bb',
                       ),   
                widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#faff74',
		       Background='#ff99bb',
                       ),    
                widget.Clock(format=' %Y-%m-%d %a %I:%M %p',
                             background="#faff74",
                             foreground='#2e035b'),
                
		widget.TextBox(                                                                                                
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#faff74',
		       Background='#ff99bb',
                       ),   
		
		widget.TextBox(
                       text = '',
                       padding = 0,
                       fontsize = 28,
                       foreground='#faff74',
		       Background='#ff99bb',
                       ),                    

		widget.BatteryIcon(
			padding = 0,
			fontsize = 28,
			background = '#faff74',
			foreground = '#2e035b',
			),
		
		widget.Battery(
			fontsize = 13,
			padding = 0,
			background = '#faff74',
			foreground = '#000000',
			update_interval=15,
			),

		widget.TextBox(
			text = '',
			padding = 0,
			fontsize = 28,
			foreground = '#faff74',
		        Background='#ff99bb',	
			),
		widget.TextBox(
                    text='',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground='#000000',
		    background='#ff99bb'
                )
                
            ],
            30,  # height in px
            background="#ff7faa"  # background color
        ), ),
]
