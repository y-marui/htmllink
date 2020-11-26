from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    packages=find_packages("src"),
    package_data={"htmllink":["template.html"]},
    install_requires=_requires_from_file('requirements.txt'),
)
