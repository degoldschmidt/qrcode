import os
from setuptools import setup
import distutils.util

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="qread",
    version="1.0",
    author="Dennis Goldschmidt",
    author_email="dennis.goldschmidt@neuro.fchampalimaud.org",
    description=("Script for reading and logging QR codes using Raspberry Pi camera."),
    license="GPLv3",
    url="https://pypi.python.org/pypi/qread",
    packages=['qread'],
    python_requires='>=3.6',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
    ],
    platforms=['Windows10Pro', 'MacOSX-HighSierra'],
    setup_requires=['opencv-python', 'imutils', 'pyzbar', 'pygame'],
    entry_points={
        'console_scripts': [
            'qread = qread.main:main',
        ],
    },
)
