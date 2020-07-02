from setuptools import setup


setup(
    name="nb-tensorflow-playground-serverproxy",
    packages= ['nb_tensorflow_playground_serverproxy'],
    version='0.0.1',
    include_package_data=True,
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    url="https://github.com/innovationOUtside/nb_tensorflow_playground_serverproxy",
    author="Tony Hirst",
    description="tony.hirst@gmail.com",
    entry_points={
        'jupyter_serverproxy_servers': [
            'nb_tensorflow_playground_serverproxy = nb_tensorflow_playground_serverproxy:setup_nb_tensorflow_playground_serverproxy',
        ]
    }
)
