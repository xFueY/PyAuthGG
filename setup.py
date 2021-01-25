from setuptools import setup, find_packages


Classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "License :: OSI Approved :: MIT License",
  "Natural Language :: English",
  "Programming Language :: Python :: 3.8"
]

setup(
  name="PyAuthGG",
  version="1.0.7",
  description="Simple Python Auth.GG Package",
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type="text/markdown",
  url="https://github.com/xFueY/PyAuthGG/",
  author="xFueY",
  author_email="xFueY@protonmail.com",
  license="MIT",
  classifiers=Classifiers,
  packages=find_packages(),
  keywords="AuthGG",
  install_requires=["requests", "bs4"]
)
