import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jutge-joapuiib",
    version="1.0.0",
    author="joapuiib",
    author_email="joapuiib@gmail.com",
    description="CLI Judge to validate SQL and programming exercises",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joapuiib/jutge",
    project_urls={
        "Issues": "https://github.com/joapuiib/jutge/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU GPT v3",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
