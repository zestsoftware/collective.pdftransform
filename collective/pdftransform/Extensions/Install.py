from Products.CMFCore.utils import getToolByName

from StringIO import StringIO
from types import InstanceType


def registerTransform(self, out, name, module):
    transforms = getToolByName(self, 'portal_transforms')
    transforms.manage_addTransform(name, module)
    print >> out, "Registered transform", name

def unregisterTransform(self, out, name):
    transforms = getToolByName(self, 'portal_transforms')
    try:
        transforms.unregisterTransform(name)
        print >> out, "Removed transform", name
    except AttributeError:
        print >> out, "Could not remove transform", name, "(not found)"


def install(self):

    out = StringIO()

    print >> out, "Installing pdf to image transform"

    # Register transforms
    registerTransform(self, out, 'pdf_to_image',
                      'collective.pdftransform.pdf_image')

    return out.getvalue()

def uninstall(self):

    out = StringIO()

    # Remove transforms
    unregisterTransform(self, out, 'pdf_to_image')

    return out.getvalue()
