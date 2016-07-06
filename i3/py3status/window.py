# -*- coding: utf-8 -*-


import json
from subprocess import Popen, PIPE
from pprint import pprint
from time import sleep


def get_active_workspace():
    """
    """
    workspaces = json.load(Popen(['i3-msg', '-t', 'get_workspaces'], stdout=PIPE).stdout)
    tree = json.load(Popen(['i3-msg', '-t', 'get_tree'], stdout=PIPE).stdout)
    workspace = None

    for ws in workspaces:
        if ws['visible'] is True and ws['focused'] is True:
            for o in tree['nodes']:
                if o['name'] == ws['output']:
                    workspace = o['nodes'][1]['nodes']
            break

    return workspace

def get_active_window(tree=None):
    """
    """
    if tree is None:
        tree = get_active_workspace()

    if isinstance(tree, list):
        tree = {'list': tree}

    if 'focused' in tree:
        if tree['focused'] == True:
            #pprint(tree)
            if 'name' in tree:
                print tree['name']

    for nodes in ['nodes', 'floating_nodes', 'list']:
        if nodes in tree:
            for node in tree[nodes]:
                get_active_window(node)

while True:
    get_active_window()
    sleep(1)
