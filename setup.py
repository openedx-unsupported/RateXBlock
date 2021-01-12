"""Setup for rate XBlock."""

import os
from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


def load_requirements(*requirements_paths):
    """
    Load all requirements from the specified requirements files.
    Returns a list of requirement strings.
    """
    requirements = set()
    for path in requirements_paths:
        with open(path) as reqs:
            requirements.update(
                line.split('#')[0].strip() for line in reqs
                if is_requirement(line.strip())
            )
    return list(requirements)


def is_requirement(line):
    """
    Return True if the requirement line is a package requirement;
    that is, it is not blank, a comment, a URL, or an included file.
    """
    return line and not line.startswith(('-r', '#', '-e', 'git+', '-c'))


setup(
    name='rate-xblock',
    version='2.0.1',
    description='rate XBlock',   # TODO: write a better description.
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ],
    packages=[
        'rate',
    ],
    install_requires=load_requirements('requirements/base.in'),
    entry_points={
        'xblock.v1': [
            'rate = rate:RateXBlock',
        ]
    },
    package_data=package_data("rate", ["static", "public"]),
)
