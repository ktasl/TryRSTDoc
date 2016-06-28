
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TryRst',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.01",
    description='Test restructuredtext documentation',
    long_description=long_description,
    # Author details
    author='Michael Angelo',
    author_email='michaelangelo@cht.com.tw',
    # The project's main homepage.
    url='http://readthedocs.org',
    # Choose your license
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable    
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
    ],
    # What does your project relate to?
    keywords='sample setuptools development',
)