#!/usr/bin/env python
req = ['nose','setuptools','pillow','scipy','numpy',
       'future-fstrings', 'pathlib']
preq = ['matplotlib']
# %%
from setuptools import setup,find_packages

setup(name='pyoptflow',
      packages=find_packages(),
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/fucusy/pyoptflow27',
      version='1.1.0',
      classifiers=[
      'Topic :: Scientific/Engineering',
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python :: 2',
      ],
      python_requires = '>=2.7',
      install_requires = req,
      extras_require={'plot':preq},
      description='Pure Python optical flow: Horn-Schunck, Lucas-Kanade',
	  )
