import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="st-annotated-text",
    version="2.0.0",
    author="Thiago Teixeira",
    author_email="me@thiagot.com",
    description="A simple component to display annotated text in Streamlit apps.",
    license="Apache 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tvst/st-annotated-text",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=["htbuilder"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
