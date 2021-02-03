import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dna-J-E-J-S",
    version="0.0.1",
    author="James Sanders",
    author_email="james.sanders1711@gmail.com",
    description="A living package of DNA related functions.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/J-E-J-S/dna-package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
