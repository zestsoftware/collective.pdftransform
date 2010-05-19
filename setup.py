from setuptools import setup, find_packages
import os

def get_file_contents_from_main_dir(filename):
    file_path = os.path.join('collective', 'pdftransform', filename)
    this_file = open(file_path)
    contents = this_file.read().strip()
    this_file.close()
    return contents

version = get_file_contents_from_main_dir('version.txt')
history = get_file_contents_from_main_dir('HISTORY.txt')
readme = get_file_contents_from_main_dir('README.txt')
long = "%s\n\n\n%s" % (readme, history)

setup(name='collective.pdftransform',
      version=version,
      description="A set of portal transform to change pdf into images",
      long_description=long,
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Zest software',
      author_email='info@zestsoftware.nl',
      url='http://github.com/vincent-psarga/collective.pdftransform',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'collective.pdfpeek'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],
      )
