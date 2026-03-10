from setuptools import setup, find_packages

setup(
    name="preplify",
    version="1.0.0",
    description="Modular, professional Python library for tabular data preprocessing with auto ML-ready pipelines.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Muhammad Hussnain",
    author_email="muhammadhussnain1227@gmail.com",
    url="https://github.com/yourusername/preplify",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)
