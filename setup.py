from setuptools import setup, find_packages

setup(
    name="preplify",
    version="1.0.3",
    packages=find_packages(),
    description="Preprocess any tabular dataset in one line — clean, encode, scale, engineer, and ML-ready.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Muhammad Hussnain",
    author_email="muhammadhussnain1227@gmail.com",
    url="https://github.com/muhammadhussnain1227-debug/preplify",
    project_urls={
        "Source Code": "https://github.com/muhammadhussnain1227-debug/preplify",
        "Bug Tracker": "https://github.com/muhammadhussnain1227-debug/preplify/issues",
        "PyPI": "https://pypi.org/project/preplify/",
    },
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
    ],
    python_requires=">=3.8",
    keywords=[
        "preprocessing", "machine learning", "data science",
        "pandas", "sklearn", "feature engineering", "automl",
        "data cleaning", "tabular data", "pipeline"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
)