# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

version = '1.0.0.dev0'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='uwosh.oie.policy',
    version=version,
    description='parent product for OIE Study Abroad project',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.2',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
    ],
    keywords='Python Plone workflow study abroad',
    author='Wildcard Corp.',
    author_email='corporate@wildcardcorp.com',
    url='https://github.com/uwosh/uwosh.oie.studyabroadstudent',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    # namespace_packages=['uwosh', 'uwosh.oie'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'uwosh.oie.studyabroadstudent',
        'uwosh.oie.studyabroadtheme',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
