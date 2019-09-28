from setuptools import setup


setup(name='romanstrazanec_pip_upgrade_all',
      scripts=['src/upgradeall.py'],
      version='1.1.0',
      description='Upgrade all python packages.',
      keywords="pip install upgrade package all",
      author='Roman Stražanec',
      author_email='roman.strazanec007@gmail.com',
      license='MIT',
      url='https://github.com/romanstrazanec/pip_upgrade_all',
      download_url='https://github.com/romanstrazanec/pip_upgrade_all/releases/tag/v1.1.0',
      install_requires=['pip'],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3.7",
          "Topic :: Other/Nonlisted Topic"
      ]
      )
