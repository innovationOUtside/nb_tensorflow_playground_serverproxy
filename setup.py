import setuptools

setuptools.setup(
    name="nb-tensorflow-playground-serverproxy",
    version='1.0dev',
    url="https://github.com/innovationOUtside/nb_tensorflow_playground_serverproxy",
    author="Tony Hirst",
    description="tony.hirst@gmail.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'nb_tensorflow_playground_serverproxy = nb_tensorflow_playground_serverproxy:setup_nb_tensorflow_playground_serverproxy',
        ]
    },
    package_data={
        'nb_tensorflow_playground_serverproxy': ['icons/*'],
    },
)
