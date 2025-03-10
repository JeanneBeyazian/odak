import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(
    name="odak",
    version="0.2.1",
    author="Kaan Akşit",
    author_email="kunguz@gmail.com",
    description="Odak, the fundamental Python library for scientific computing in optical sciences.",
    license=read('LICENSE.txt'),
    keywords="optics, holography, perception, graphics",
    url="https://github.com/kunguz/odak",
    install_requires=install_requires,
    packages=[
        'odak',
        'odak/raytracing',
        'odak/jones',
        'odak/tools',
        'odak/wave',
        'odak/learn/wave',
        'odak/learn/tools',
        'odak/learn/perception',
        'odak/learn/raytracing',
        'odak/visualize',
        'odak/visualize/blender',
        'odak/manager',
        'odak/measurement',
        'odak/catalog',
        'odak/learn'
    ],
    package_dir={'odak': 'odak'},
    package_data={'odak': ['catalog/data/*.json']},
    data_files=[
        ('', ['LICENSE.txt', 'README.md', 'THANKS.txt', 'requirements.txt'])],
    long_description=read('short_readme.md'),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Physics",
        "Programming Language :: Python",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
    ],
    python_requires='>=3.7.5',
)
