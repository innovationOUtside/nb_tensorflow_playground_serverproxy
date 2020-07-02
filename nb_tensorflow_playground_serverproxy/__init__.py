"""
Return config on servers to start for nb_tensorflow_playground_serverproxy

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os

def setup_nb_tensorflow_playground_serverproxy():
    return {
        'command': [["python", "-m", "http.server", "--directory", "/home/jovyan/nb_tensorflow_playground_serverproxy/tensorflow_playground", "&>", "/dev/null", "&"],
        'environment': {},
        'launcher_entry': {
            'title': 'nb_tensorflow_playground_serverproxy',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'nb_tensorflow_playground_serverproxy.svg')
        }
    }
