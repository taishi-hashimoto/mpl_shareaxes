from setuptools import setup
from setuptools import find_packages


package_dir = "src"

setup(
    name='mpl_shareaxes',
    version="v1.0.0",
    description=(
        "Share X/Y axis of two or more Axes after they have been created."),
    package_dir={
        "": package_dir
    },
    packages=find_packages(package_dir),
    package_data={},
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    entry_points={
        "console_scripts": [
        ]
    },
    author="Taishi Hashimoto",
    author_email="hashimoto.taishi@outlook.com")
