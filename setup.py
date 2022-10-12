# setup tools
# pyproject
# external build tools (poetry, flit)

from setuptools import setup, find_packages

setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    author="Fabio Barros",
    packages=find_packages(),
)