from setuptools import setup, find_packages

setup(
    name="logging-util",  # 🔹 package name on PyPI
    version="1.0.0",
    author="Afreed Mohammed",
    author_email="youremail@example.com",
    description="A reusable logging setup utility for Python projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/afreed9395/logs_utility",
    packages=find_packages(),
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)


