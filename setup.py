#Used to setup the MOGONET package.
#The use of include_package_date also requires a MANIFEST.in file

from setuptools import setup

setup(
	name='MOGONET',
	version='0.1',
	description='Multi-omics integration using graph convolution networks',
	author='Tongxin Wang',
	url='https://github.com/txWang/MOGONET',
    py_modules=[],
	include_package_date=True,
	license='MIT'
)
