from setuptools import setup


setup(name='romanstrazanec_pip_upgrade_all',
      scripts=['src/installall.py'],
      version='1.1.0',
      description='Upgrade all python packages.',
      keywords="pip install upgrade package all",
      author='Roman Stražanec',
      author_email='roman.strazanec007@gmail.com',
      license='MIT',
      url='https://github.com/romanstrazanec/pip_upgrade_all',
      install_requires=['pip']
      )
