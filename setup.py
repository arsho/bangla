# -*- coding: utf-8 -*-
from setuptools import setup
import io


def readme():
    with io.open('README.rst', encoding='utf8', errors='ignore') as f:
        return f.read()


setup(name='bangla',
      version='0.0.5',
      description='Bangla is a Python package for converting Gregorian dates to the Bengali calendar, translating English numerals to Bangla numerals, and generating Bangla ordinals for dates.',
      long_description=readme(),
      install_requires=[],
      classifiers=[
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Development Status :: 5 - Production/Stable',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='bangla bangla date bongabdo bangla digit',
      url='http://github.com/arsho/bangla',
      author='Ahmedur Rahman Shovon',
      author_email='shovon.sylhet@gmail.com',
      license='MIT',
      packages=['bangla'],
      include_package_data=True,
      zip_safe=False
      )
