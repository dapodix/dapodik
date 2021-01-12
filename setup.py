from setuptools import setup

setup(
    name="dapodik",
    version="0.6.0",
    description="SDK python untuk aplikasi dapodik.",
    author="Habib Rohman",
    author_email="habibrohman@protonmail.com",
    url="https://github.com/hexatester/dapodik",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Education",
    ],
    packages=["dapodik"],
    install_requires=["python", "requests", "beautifulsoup4"],
    entry_points={"console_scripts": ["dapodik=dapodik.__main__:main"]},
)
