import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'colander',
    'deform',
    'deform_bootstrap',
    'html2text',
    'psutil',
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'pyramid_mako',
    'simplejson',
    'waitress',
    ]

setup(name='niak_server',
      version='0.0',
      description='niak_server',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='P-O Quirion',
      author_email='pioliqui@gmail.com',
      url='',
      keywords='web pyramid neuroscience NIAK',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="niak_server",
      entry_points="""\
      [paste.app_factory]
      main = niak_server:main
      """,
      )
