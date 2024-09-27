from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("requirements-dev.txt") as f:
    required_dev = f.read().splitlines()

setup(
    name="economics",
    version="0.0.1",
    description="Economic simulation",
    keywords="economics, simulation",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={"chb": ["py.typed"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python ::3",
        "Programming Language :: Python ::3.10"
        "License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE v3 License",
        "Operating System :: Linux",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=required,
    extras_require={
        "dev": required_dev,
    },
    python_requires=">=3",
    url="https://github.com/EStorvik/economics.git",
    author="Erlend Storvik",
    maintainer="Erlend Storvik",
    maintainer_email="erlend.storvik@hvl.no",
    platforms=["Linux"],
    license="GNU GPL v3",
)