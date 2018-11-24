import os
from setuptools import setup, find_packages

setup(
	name='birdcraft',
	version='0.1',
	long_description='birdcraft is a social website.',
	packages=find_packages(),
	include_package_data=True,
	zip_safe=False,
	install_requires=['Flask', 'requests']
)
