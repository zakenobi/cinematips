from setuptools import setup, find_packages


setup(
    name='cinematips',
    version='0.1.0',
    author='Zachary Gagnou and Alexandra Mille-Egea',
    url='https://github.com/zakenobi/cinematips',
    packages=find_packages(include=['cinematips', 'cinematips.*']),
    install_requires=[
        'requests==2.28.1',
    ]
)
