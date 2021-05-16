import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lightspeed-api-client-dmizrahi",
    version="0.2.0",
    author="Daniel Mizrahi",
    author_email="dmizrahi@nodedevelopment.net",
    description="An API client to execute REST services by Lightspeed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.nodedevelopment.net/",
    project_url={
        'Documentation': 'https://github.com/DanielDM325/Lightspeed-API-Python-Client/wiki',
        'Source': 'https://github.com/DanielDM325/Lightspeed-API-Python-Client'
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Build Tools"
    ],
    python_requires='>=3.5',
    license='GNU General Public License v3.0',
    install_requires=['requests']
)
