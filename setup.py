import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="postgres-helper",
    version="0.0.5",
    author="Tek Kshetri",
    author_email="iamtekson@gmail.com",
    description="Package for Postgres query on python",
    py_modules=['pg'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamtekson/postgres-helper",
    packages=['pg'],
    keywords=['postgresql', 'postgres', 'database',
              'sql', 'api', 'table', 'pg', 'postGIS'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['psycopg2'],
    python_requires='>=3.6',
)
