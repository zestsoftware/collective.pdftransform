Changelog
=========

0.6 (unreleased)
----------------

- Nothing changed yet.


0.5 (2015-08-27)
----------------

- Code cleanup.
  [maurits]


0.4 (2013-06-04)
----------------

- Do not explicitly require collective.pdfpeek 1.2, but make that a
  minimum.
  [maurits]


0.3 (2012-10-30)
----------------

- Patched pdfpeek to use the default 1.2 release. [vincent]

- Allow setting PDF resolution in update_form. [vincent]


0.2 (2010-06-21)
----------------

- Bugfix in utils/is_transformable_pdf. [vincent]


0.1 (2010-05-19)
----------------

- added translations for french and dutch. [vincent]

- updated the validator to return an error if the PDF file can not be
  transformed. [vincent]

- added is_transformable_pdf in utils, tells if the PDF file uploaded
  can be transformed with pdf_to_image. [vincent]

- added validator called 'isValidImageOrPDF' that checks that the
  submitted if is a PDF or an image (except BMP images as it can cause
  problems). [vincent]

- added update_form in utils, that can be used in 
  the post_validate method of your Archetype objects. [vincent]

- Added transform to the portal_transform. [vincent]
