from setuptools import setup

setup(
    name="dozenos-http-api-tools",
    version="0.1.0",
    author="DozenOS maintainers and contributors",
    author_email="maintainers@dozenos.local",
    python_requires=">=3.7",
    license="BSD",
    url="http://www.dozenos.io",
    packages=["dozenos-http-api-tools"],
    description=("A debian wrapper of packages to support the DozenOS http api."),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License", 
        "Topic :: Internet :: WWW/HTTP",
    ],
)
