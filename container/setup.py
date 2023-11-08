"""Package setup"""
from setuptools import setup, find_packages

setup(
    name="container-inference",
    version="0.1.0",
    author="Jacopo Maragna",
    description="Deploying ML Models as Docker Containers",
    packages=find_packages(),
    install_requires=[
        "fastapi==0.100.0",
        "uvicorn==0.22.0",
        "python-multipart==0.0.6",
        "scikit-learn==1.3.2",
        "pandas==2.1.2",
    ],
    extras_require={
        "dev": [
            "black==23.1.0",
            "pylint==2.17.0",
            "pytest==7.3.1",
            "httpx==0.23.3",
            "uvicorn==0.22.0",
        ]
    },
)
