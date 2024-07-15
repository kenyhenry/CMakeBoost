from setuptools import setup, find_packages

setup(
    name="CMakeBoost",
    version="0.1.0",
    author="Keet Stack",
    author_email="henry.keny@outlook.fr",
    description="A tool to simplify dependency management, compilation, and execution of C/C++ projects using CMake and YAML.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kenyhenry/CMakeBoost",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'yamllake=generate_and_build:main',
        ],
    },
)
