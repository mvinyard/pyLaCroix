from setuptools import setup
import re, os, sys

setup(
    name="pyLaCroix",
    version="0.0.11",
    python_requires=">3.8.0",
    author="Michael E. Vinyard - Harvard University - Massachussetts General Hospital - Broad Institute of MIT and Harvard",
    author_email="mvinyard@broadinstitute.org",
    url="https://github.com/mvinyard/pyLaCroix",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    description="pyLaCroix - a python color palette for those that love sparkling water.",
    packages=[
        "pyLaCroix",
    ],
    install_requires=[
        "colour"
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    license="MIT",
)
