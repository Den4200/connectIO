import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="connectIO", # Replace with your own username
    version="0.0.3",
    author="Dennis Pham",
    author_email="dpham.42@hotmail.com",
    description="A simple module for sending data across the internet!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Den4200/connectIO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",

        "Topic :: Communications ",
        "Topic :: Communications :: Chat",
        "Topic :: Communications :: File Sharing",

        "Topic :: Games/Entertainment",
    ],
    python_requires='>=3.6',
)
