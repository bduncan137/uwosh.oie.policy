.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
uwosh.oie.policy
==============================================================================

This project is intended to help developers working on the UWO Office of International Education's Plone workflow project
for study abroad programs and applications.

Once you have your python 3.7.8 or 3.7.9 environment set up, using `python3 -m venv env` for example,
install requirements with `env/bin/pip install -r requirements.txt` and then run the buildout with
`env/bin/buildout`.

Once this is complete you can start Plone with the UWO addons using `env/bin/instance fg`, then
log in at localhost:8080 using admin:admin, create a site and install the UWO study abroad student 
and theme packages to it in the Add Ons section of Site Setup.

For some functionality to work, the Plone site currently must be named "oie".

The student and theme packages are public on github here
https://github.com/uwosh/uwosh.oie.studyabroadstudent/
https://github.com/uwosh/uwosh.oie.studyabroadtheme/

Support
=======

If you are having issues, please let us know via the GitHub issue tracker.



License
-------

The project is licensed under the GPLv2.
