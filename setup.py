# setup tools
# pyproject
# external build tools (poetry, flit)

from setuptools import setup, find_packages
import os

def read(*paths):
    """Read the contexts of a text file safely"""
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()

def read_requirements(path):
    """return a list of requitrements from a text file"""

    return [
        line.strip() for line in read(path).split("\n")
        if not line.startswith(("#", "git+", '"', "-"))
    ]
    



setup(
    name="dundie",
    version="0.1.0",
    description="Reward Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Fabio Barros",
    python_requires=">=3.8",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundie = dundie.__main__:main"
        ]
    },
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "test": read_requirements("requirements.test.txt"),
        "dev": read_requirements("requirements.dev.txt")
    }
)