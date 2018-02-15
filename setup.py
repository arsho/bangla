# -*- coding: utf-8 -*-
from setuptools import setup
import io
def readme():
    with io.open('README.rst', encoding='utf8', errors='ignore') as f:
        return f.read()
setup(name='bangla',
      version='0.0.2',
      description='Bangla is a package for Bangla language users with various functionalities including Bangla date and Bangla numeric conversation.',
      long_description=readme(),
      install_requires=[],
      classifiers=[
        'Operating System :: OS Independent',
                'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',		
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
