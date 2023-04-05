from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in machine_shop/__init__.py
from machine_shop import __version__ as version

setup(
	name="machine_shop",
	version=version,
	description="Machine Shop",
	author="Machine shop",
	author_email="kinikarsonali@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
