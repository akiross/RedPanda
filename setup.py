from distutils.core import setup

setup(
    name='bio-d3',
    version='0.1.0',
    author='L. De Sano',
    author_email='l.desano@campus.unimib.it',
    packages=['biodf',],
 #   scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
 #   url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Bio data analysis with pandas and d3',
    long_description=open('README.txt').read(),
    install_requires=[
        "Numpy >= 1.6.1",
        "Scipy >= 0.10.1",
        "Pandas >= 0.11.0",
        "python-dateutil >= 1.5",
        "matplotlib",
        "statsmodel",
    ],
)