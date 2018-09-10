import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="greeter",
    version="0.0.1",
    author="Jeffrey Morgan",
    description="A simple Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrJeffreyMorgan/python-greeter.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
