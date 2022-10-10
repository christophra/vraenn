import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()
# strip version numbers
required = [_r.split('=')[0] for _r in required]
required += ['wheel']

setuptools.setup(
    name="vraenn",
    version="0.0.1",
    author="Villar et al.",
    author_email="chraab@fzu.cz",
    description="Extension of V. Ashley Villar's VRAENN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/christophra/vraenn",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
