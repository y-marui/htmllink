from setuptools import setup, find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    packages=find_packages("src"),
    install_requires=_requires_from_file('requirements.txt'),
)
