import codecs
import os
from setuptools import setup, find_packages


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open("requirements.txt") as requirements:
        for install in requirements:
            requirements_list.append(install.split(";")[0].strip())

    return requirements_list


__version__ = "0.0.0"
packages = find_packages(exclude=["tests*"])
requirements = requirements()

fn = os.path.join("dapodik", "version.py")
with open(fn) as fh:
    code = compile(fh.read(), fn, "exec")
    exec(code)

with codecs.open("README.md", "r", "utf-8") as fd:
    setup(
        name="dapodik",
        version=__version__,
        description="SDK python untuk aplikasi dapodik.",
        long_description=fd.read(),
        author="Habib Rohman",
        author_email="habibrohman@protonmail.com",
        url="https://github.com/dapodix/dapodik",
        project_urls={
            "Documentation": "https://dapodix.github.io/dapodik/",
            "Bug Tracker": "https://github.com/dapodix/dapodik/issues",
            "Source Code": "https://github.com/dapodix/dapodik",
        },
        license="MIT",
        classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Intended Audience :: Developers",
            "Topic :: Education",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
        ],
        packages=packages,
        install_requires=requirements,
        entry_points={"console_scripts": ["dapodik=dapodik.main:main"]},
    )
