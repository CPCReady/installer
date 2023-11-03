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
