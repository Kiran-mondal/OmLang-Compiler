from setuptools import setup

setup(
    name='OmLang-Compiler',
    version='2.6.0',
    description='A clean, friendly, cross-platform standalone programming language for beginners.',
    author='Kiran Mondal',
    py_modules=['om'],
    entry_points={
        'console_scripts': [
            'om=om:cli',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
