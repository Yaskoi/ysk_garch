# setup package
from setuptools import setup, find_packages

setup(
    name='ysk_garch',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pandas',
    ],
)

# setup package ends