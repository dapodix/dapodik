from setuptools import setup

setup(
    name="dapodik",
    version="0.8.0",
    description="SDK python untuk aplikasi dapodik.",
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["dapodik"],
    install_requires=["python", "requests", "beautifulsoup4", "attrs", "cachetools"],
    entry_points={"console_scripts": ["dapodik=dapodik.main:main"]},
)
