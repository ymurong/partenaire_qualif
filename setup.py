import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="partenaire-qualif",
    version='0.2.2',
    author="Yanchao MURONG",
    author_email="yanchao.murong@gmail.com",
    description="A simple tool that automates the qualification of a partner(reseller/integrator/editor) by finding its website, industries, business functions and services.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ymurong/partenaire_qualif.git",
    packages=setuptools.find_packages(),
    package_data={
        "qualif.templates": ["*.txt"],
    },
    include_package_data=True,
    install_requires=[
        'openai',
        'pandas',
        'httpx',
        'validators',
        'beautifulsoup4',
        'importlib_resources'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
