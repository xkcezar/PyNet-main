from setuptools import setup, find_packages

setup(
    name='NETOPIA_Payments',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'pyopenssl',
        'pycryptodome',
        'requests',
        'flask',
        'hashlib',
        'random',
        'time',
        'decimal',
        'xml.dom.minidom',
        'urllib.parse',
        'datetime',
        'locale',

    ], )