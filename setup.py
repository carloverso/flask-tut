from setuptools import find_packages, setup

setup(
    name="flaskr",
    version="0.0000000001",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)