import os
from setuptools import setup, find_packages

setup(
    name = "blackjacksim",
    version = "0.0.1",
    author = "Charlie Lehman",
    author_email = "charlie.k.lehman@gmail.com",
    description = ("BlackJack Simulator"),
    license = "Apache",
    keywords = "BlackJack, 21, simulation",
    url = "https://github.com/charlieLehman/blackjacksim",
    packages=['blackjacksim',
              'blackjacksim.simulations',
              'blackjacksim.entities',
              'blackjacksim.pytorch',
              'blackjacksim.data',
              'blackjacksim.strategies'],
    data_files = [('blackjacksim', ['blackjacksim/data/basic.json', 'blackjacksim/data/default_config.json'])],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: Apache",
    ],
    install_requires=[
        "numpy",
        "pandas",
        "seaborn",
        "scipy",
        "tqdm",
        "torch",
],
     dependency_links=[
    ]
)

