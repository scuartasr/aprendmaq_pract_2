from setuptools import setup, find_packages

setup(
    name="mi_proyecto",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "scipy",
        "matplotlib",
        "seaborn",
    ],
)
