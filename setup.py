from os import listdir
from setuptools import setup, find_packages


src = 'src'
name = next(i for i in listdir(src) if len(i.split('.')) == 1)
version = '0.0.2'

author = 'Roman Stražanec'
email = 'strazanec.roman@gmail.com'
url = f'https://github.com/romanstrazanec/{name}'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(name=name,
      version=version,
      description='Upgrade all python packages.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      keywords="pip install upgrade package all",
      author=author,
      author_email=email,
      maintainer=author,
      maintainer_email=email,
      license='MIT',
      url=url,
      download_url=f'{url}/archive/v{version}.tar.gz',
      packages=find_packages(where=src),
      package_dir={'': src},
      entry_points={
          'console_scripts': [
              f'{name} = {name}._cli:main',
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
