from Products.PortalTransforms.libtransforms.utils import MissingBinary
from zope.i18nmessageid import MessageFactory
PDFTransformMessageFactory = MessageFactory(u'collective.pdftransform')

from Products.validation import validation
from validator import ImageOrPDFValidator
validation.register(ImageOrPDFValidator('isValidImageOrPDF'))

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
