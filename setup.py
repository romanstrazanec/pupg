import os
import codecs

from setuptools import setup, find_packages


HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(HERE, *parts), 'rb', 'utf-8') as f:
        return f.read()


setup(name='pipu',
      # scripts=['src/__main__.py'],
      version='1.1.1',
      description='Upgrade all python packages.',
      long_description=read('README.md'),
      keywords="pip install upgrade package all",
      author='Roman Stražanec',
      author_email='strazanec.roman@gmail.com',
      maintainer='Roman Stražanec',
      maintainer_email='strazanec.roman@gmail.com',
      license='MIT',
      url='https://github.com/romanstrazanec/pipu',
      download_url='https://github.com/romanstrazanec/pipu/archive/v1.1.1.tar.gz',
      packages=find_packages(where='src'),
      package_dir={'': 'src'},
      entry_points={
          'console_scripts': [
              'pipu = pipu._cli:main',
          ],
      },
      install_requires=['pip'],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.7",
          "Topic :: Other/Nonlisted Topic"
      ]
      )
