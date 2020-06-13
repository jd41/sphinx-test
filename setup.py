import hoverxref
import setuptools


with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='sphinx-test',
    version=hoverxref.version,
    author='jd41',
    author_email='',
    description='Sphinx glossary test',
    license='MIT',
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Extension',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation',
    ],
    keywords='tooltip hoverxref sphinx',
    project_urls={
        'Documentation': 'https://sphinx-hoverxref.readthedocs.io/',
        'Source': 'https://github.com/readthedocs/sphinx-hoverxref',
        'Tracker': 'https://github.com/readthedocs/sphinx-hoverxref/issues',
    },
)
