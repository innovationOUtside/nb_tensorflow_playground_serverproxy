import setuptools

setuptools.setup(
    name="nb-tensorflow-playground-serverproxy",
    version='1.0.1',
    url="https://github.com/innovationOUtside/nb_tensorflow_playground_serverproxy",
    author="Tony Hirst",
    description="tony.hirst@gmail.com",
    packages= ['nb_tensorflow_playground_serverproxy'],
    include_package_data=True,
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy',
        'notebook'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'nb_tensorflow_playground_serverproxy = nb_tensorflow_playground_serverproxy:setup_nb_tensorflow_playground_serverproxy',
        ]
    },
    data_files=[],
    zip_safe=False
)
