import setuptools

# This all is for the PyPI package
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_NAME = "Dhruval Bhuva"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "dhruvalbhuva2000@gmail.com"

setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"",
    project_urls={
        "Bug Tracker": f"",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
