
from setuptools import find_packages
from setuptools import setup

setup (
	name="file_size",
	version="v0.1.0",
	description="""
    Make a tree map of all the files in a folder
    """,
	author="Jonathon Chew",
	author_email="jonchew626@hotmail.com",
	url="",
    package_dir={"": "src"},
	packages=find_packages(exclude=("tests*")),
)
	
