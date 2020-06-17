import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read()

setuptools.setup(
    name="flexpoolapi",
    version="0.1.0",
    author="Flexpool",
    author_email="office@flexpool.io",
    description="🐍 Pythonic wrapper for Flexpool Public API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flexpool/py-flexpoolapi",
    packages=["flexpoolapi"],
    requirements=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
