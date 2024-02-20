from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Library designed to process text with various filter criteria'
LONG_DESCRIPTION = 'a library containing a collection of utility functions designed to filter and process text data based on certain criteria. These functions are useful for various text processing tasks, such as removing unwanted characters, extracting specific information, or cleaning input data'

# Setting up
setup(
    name="dekimashita",
    version=VERSION,
    author="ryyos (Rio Dwi Saputra)",
    author_email="<riodwi12174@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    # install_requires=['logging'],
    keywords=['filter', 'dictionary', 'text', 'textCleaning', 'alphabetic'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: Microsoft :: Windows",
    ]
)