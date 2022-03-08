from setuptools import setup, find_packages

setup(
	name='project0',
	version='1.0',
	author='Pradipkumar Rajasekaran',
	author_email='pradipkumar.rajasekaran-1@ou.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
