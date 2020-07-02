"""
Return config on servers to start for nb_tensorflow_playground_serverproxy

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import pkg_resources

def setup_nb_tensorflow_playground_serverproxy():
    fpath = pkg_resources.resource_filename('nb_tensorflow_playground_serverproxy', 'static/')
    return {
        'command': ["python", "-m", "http.server", "--directory", "/home/jovyan/nb_tensorflow_playground_serverproxy/static", "{port}"],
        'environment': {},
        'launcher_entry': {
            'title': 'nb_tensorflow_playground_serverproxy',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'nb_tensorflow_playground_serverproxy.svg')
        }
    }
