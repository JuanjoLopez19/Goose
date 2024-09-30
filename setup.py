import io
import logging
import subprocess
import sys

from setuptools import find_packages, setup
from setuptools.command.install import install

logging.basicConfig(
    level=logging.INFO,
    filename="install.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s",
)




def readme():
    with io.open("README.md", encoding="utf-8") as f:
        return f.read()


def requirements(filename):
    reqs = list()
    with io.open(filename, encoding="utf-8") as f:
        for line in f.readlines():
            reqs.append(line.strip())
    return reqs


setup(
    name="GooseDownloader",
    version="0.0.1",
    packages=find_packages(),
    license="LICENSE.md",
    long_description=readme(),
    long_description_content_type="text/markdown",
    install_requires=requirements("requirements.txt"),
    data_files=[],
    entry_points={"console_scripts": ["goose=goose.main:run"], },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
)
