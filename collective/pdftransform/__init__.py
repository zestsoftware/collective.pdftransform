# Import this first, to avoid circular import.
from collective.pdftransform.messagefactory import PDFTransformMessageFactory
# Then the rest.
from Products.PortalTransforms.libtransforms.utils import MissingBinary
from Products.validation import validation
from collective.pdftransform import patch
from collective.pdftransform.validator import ImageOrPDFValidator

validation.register(ImageOrPDFValidator('isValidImageOrPDF'))
patch.patch_pdfpeek()
PDFTransformMessageFactory  # pyflakes

modules = [
    'pdf_image',
]

g = globals()
transforms = []
for m in modules:
    try:
        ns = __import__(m, g, g, None)
        transforms.append(ns.register())
    except ImportError, e:
        print "Problem importing module %s : %s" % (m, e)
    except MissingBinary, e:
        print e
    except:
        import traceback
        traceback.print_exc()


def initialize(engine):
    pass
