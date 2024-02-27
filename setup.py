from setuptools import setup, find_packages

# def install_requires():
#     with open('requirements.txt', 'r') as f:
#         return [line.strip() for line in f.readlines()]

setup(
    name='sphinx-pigweed',
    version='0.0.1',
    packages=['sphinx-pigweed'],
    package_data={
        'sphinx-pigweed': [
            'static/sphinx-pigweed.css',
        ],
    },
    # install_requires=install_requires(),
    install_requires=[],
    classifiers=[],
)
