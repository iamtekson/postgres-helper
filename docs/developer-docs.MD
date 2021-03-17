# Publish package

For publishing the python package, follow following steps,

1. install twine `pip install twine`
2. create dist folder by running setup.py file `python setup.py bdist_wheel sdist`
3. Push to PyPI `twine upload dist/*`

# Generating document

For generate the documentation of project, you need to follow following steps,

1. Install sphinx (`pip install sphinx`)

2. Run `sphinx-quickstart` and give the project author, project name, version etc.

3. Update the `index.rst` file according to your need (create other files and linked it back to `index` if necessary).

4. Create account on [readthedocs](https://readthedocs.org/dashboard/) and import project from github.

5. Run the build command

6. Run `make html` to generate the html code
