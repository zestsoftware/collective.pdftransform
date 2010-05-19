Introduction
============

The main goal of this product is to allow PDF into ImageFields in
Plone. It uses code written by David Brenneman for
collective.pdfpeek.

Install
=======

Just add the following lines in your buildout:
  collective.pdfpeek
  collective.pdftransform

You must install pdftransform with the quick installer (no need to
install pdkpeek, but it must be in the buildout as we use its methods)


Using pdftransform in your site
===============================

collective.pdftransform adds a 'pdf_to_image' transform in Plone
portal_transform.
As transforms can not be used with FileField (or at least I did not
find how ...) it also provides a method in utils called update_form.
You can use it in the 'post_validate' method of your Archetype
objects.

Here is an example (from Products.plonehrm, the Employee Archetype
object):

  ...
  from collective.pdftransform.utils import update_form
  ...
  class Employee(BaseFolder):
      ...

      security.declarePrivate('post_validate')
      def post_validate(self, REQUEST, errors):
          update_form(self, REQUEST)

      ...

With this, all files submitted in the edit form, if they are PDF, are
transformed into jpg files.
You can specify an extra argument in update_form which is the list of
fields, for example, if we had written this:

      security.declarePrivate('post_validate')
      def post_validate(self, REQUEST, errors):
          update_form(self, REQUEST,
                      ['portrait_file', 'idScan_file'])

only the files submitted in the portrait and idScan fields would have
been transformed.

You can also use the validator called 'isValidImageOrPDF' in your
Image fields.
