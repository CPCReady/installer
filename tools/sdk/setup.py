##-----------------------------LICENSE NOTICE------------------------------------
##  CPCReady: SDK for programming in Locomotive Amstrad Basic and Basic Compiled
##            with Ugbasic (https://ugbasic.iwashere.eu/)
##
##  Copyright (C) 2023 destroyer
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU Lesser General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU Lesser General Public License for more details.
##
##  You should have received a copy of the GNU Lesser General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##------------------------------------------------------------------------------

import os
from setuptools import setup, find_packages
from CPCReady import __version__ as version
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

if os.name != 'posix':
    raise RuntimeError("CPCReady is only compatible with Linux operating systems.")

VERSION =  version
DESCRIPTION = 'Software Developer Kit for programming in Basic for Amstrad CPC'

setup(
    name='CPCReady',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=VERSION,
    author="Destroyer",
    author_email="<cpcready@gmail.com>",
    description=DESCRIPTION,
    license="GPL",
    packages=find_packages(),
    install_requires=[
        'click',
        'configparser',
        'rich',
        'jinja2',
        'emoji',
        'requests',
        'inquirer',
        'packaging'
    ],
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License (GPL)',   
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'cpcr     = CPCReady.main:main',
            'cpc      = CPCReady.main:main',
            'cpcready = CPCReady.main:main',
        ]
    }
)
