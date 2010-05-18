from Products.PortalTransforms.libtransforms.utils import MissingBinary
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
