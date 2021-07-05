from setuptools import find_packages, setup

with open("./README.md", encoding="utf-8") as readme:
    README = readme.read()

setup(
    name="inford",
    version="1.1.0",
    author="Prathamesh Bhaleakr",
    author_email="prathameshb1704@gmail.com",
    description="Simple module for sending dsicord webhooks",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Prathamesh-B/inford",
    license="MIT License",
    install_requires=[
        "requests>=2.19.1",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6",
)
