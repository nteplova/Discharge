def default_astra_config():
    cfg = [
        ["astra_path", "\home\Astra", "Path to astra user folder"],
        ["exp", "readme", "exp file name"],
        ["equ", "showdata", "equ file name"],
        ["option1", "op1", "option 1"],
        ["option2", "op2", "option 2"]
    ]
    return ('Astra config', cfg)

def default_sbr_config():
    cfg = [
        ["sbr1", "\home\Astra", "subrutine 1"],
        ["sbr2", "readme", "subrutine 2"],
        ["sbr3", "showdata", "subrutine 3"],
        ["sbr4", "", "subrutine 4"],
        ["sbr5", "", "subrutine 5"]
    ]
    return ('Subrutine config', cfg)

def default_config():
    astra_cfg = default_astra_config()
    sbr_cfg = default_sbr_config()
    return dict([astra_cfg, sbr_cfg])    

import os
import ipywidgets as widgets
from IPython.display import display

output = []
config = []
all_items = []

import json

def init_config():
    global config
    config = default_config()

def save_config():
    fp = os.path.abspath("astra.json")
    with open( fp , "w" ) as write:
        json.dump( config , write, indent = 2 )

def save_changes(b):
    no_changes = True
    for items, pp in zip(all_items, config.items()):
        for w, p in zip(items, pp[1]):
            if (w.value != p[1]):
                no_changes = False
                p[1] = w.value
                with output:
                    print(w.value, p)
    if no_changes:
        with output:
            print("no changes")
    else:                
        save_config()
        with output:
            print("save config")
   



def widget():
    global all_items
    global output
    output = widgets.Output()
    tab_children = []
    all_items = []
    for pp in config.items():
        items = [widgets.Text(value=p[1], sync=True, description=p[0], disabled=False) for p in pp[1] ]
        all_items.append(items)
        tab_children.append(widgets.GridBox(items, layout=widgets.Layout(grid_template_columns="repeat(3, 300px)")))
    tab = widgets.Tab()
    tab.children = tab_children
    for id, p in enumerate(config.items()):
        tab.set_title(id, p[0])

    save_btn = widgets.Button(
        description='Save config',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Save config',
        icon='check' # (FontAwesome names without the `fa-` prefix)
       
    )
    load_btn = widgets.Button(
        description='Load config',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Load config',
        icon='check' # (FontAwesome names without the `fa-` prefix)
       
    )
    save_btn.on_click(save_changes)
    btn_box = widgets.HBox([load_btn, save_btn])
    return widgets.VBox([widgets.Label('Astra configuration'), tab, btn_box, output])
