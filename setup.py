import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

requirements = ["pandas >= 0.2", "joblib >= 0.1", "numpy >= 1"]

setuptools.setup(
    name='HBNDmodel',
    version="0.0.19",
    author='Andre Frade',
    author_email="andre.frade@hertford.ox.ac.uk",
    description='HBND predictive model package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/apfrade/HBNDmodel.git",
    packages=['HBNDmodel'],
    install_requires= requirements,
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],    
    include_package_data=True)


