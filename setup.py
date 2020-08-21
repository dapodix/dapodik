from setuptools import setup

setup(
    name='dapodik',
    version='0.1.0',
    description='Client & alat bantu aplikasi Dapodik',
    author='Habib Rohman',
    author_email="habibrohman@protonmail.com",
    url='https://github.com/hexatester/dapodik',
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["dapodik"],
    install_requires=[
        'python'
        'requests'
        'openpyxl'
        'beautifulsoup4'
        'lxml'
    ],
    entry_points={
        'console_scripts': [
            'dapodik=dapodik.__main__:main'
        ]
    }
)
