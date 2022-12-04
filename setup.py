from setuptools import setup, find_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name='cinematips',
    version='0.1.0',
    author='Zachary Gagnou & Alexandra Mille-Egea',
    url='https://github.com/zakenobi/cinematips',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(include=['cinematips', 'cinematips.*']),
    install_requires=[
        'requests==2.28.1',
    ]
)
