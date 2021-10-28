from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bldc/__init__.py
from bldc import __version__ as version

setup(
	name="bldc",
	version=version,
	description="ecommerce portal from bldc fans",
	author="wahni",
	author_email="wahni@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
