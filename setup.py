#!/usr/bin/env python
import codecs
import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    with codecs.open(os.path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version():
    f = codecs.open('version', 'r', 'utf-8-sig')
    line = f.readline()
    f.close()
    return line


def install_requires():
    requires = [
        'pycoin>=0.90.20201031', 'requests>=2.21.0', 'websockets>=7.0', 'aiohttp>=3.5.4',
        'secp256k1>=0.13.2', 'protobuf>=3.6.1', 'mnemonic>=0.18', 'ujson>=1.35'
    ]
    return requires


setup(
    name='binancechainpy',
    version=find_version(),
    packages=find_packages(),
    description='Binance Chain HTTP API python implementation',
    url='https://github.com/tokenchain/binancepy',
    author='Heskemo',
    license='MIT',
    author_email='ccp@ccp.com',
    install_requires=install_requires(),
    zip_safe=False,
    extras_require={
        'ledger': ['btchip-python>=0.1.28', ],
    },
    keywords='binance dex exchange rest api bitcoin ethereum btc eth bnb ledger',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
