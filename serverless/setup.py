"""Package setup"""
from setuptools import setup, find_packages

setup(
    name="serverless-inference",
    version="0.1.0",
    author="Jacopo Maragna",
    description="Deploying ML Models as Serverless Functions",
    packages=find_packages(),
    install_requires=[
        "pydantic==2.4.2",
        "scikit-learn==1.3.2",
    ],
    extras_require={
        "dev": [
            "black==23.1.0",
            "pylint==2.17.0",
            "pytest==7.3.1",
        ]
    },
)
