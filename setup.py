from setuptools import find_packages, setup

description = """
Simple, powerful and non-obstructive django email middleware.
"""

setup(
    name="djmail",
    url="https://github.com/niwibe/djmail",
    author="Andrey Antukh",
    author_email="niwi@niwi.be",
    version="0.9",
    packages=find_packages(include=['djmail*']),
    description=description.strip(),
    zip_safe=False,
    include_package_data=True,
    package_data={
        "": ["*.html"],
    },
    classifiers=[
        # "Development Status :: 5 - Production/Stable",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
