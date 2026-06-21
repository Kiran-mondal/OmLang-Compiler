from setuptools import setup

setup(
    name="om-lang",
    version="1.2.0",
    py_modules=["om"],
    entry_points={
        'console_scripts': [
            'om=om:cli',
        ],
    },
)
