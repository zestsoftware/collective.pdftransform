from zope.interface import implements
from Products.PortalTransforms.interfaces import itransform

from collective.pdfpeek.transforms import convertPDFToImage

class PdfToImage:
    """Transforms PDF to jpg images."""

    __implements__ = itransform

    __name__ = "pdf_to_image"
    output = "image/jpeg"

    def __init__(self,
                 name=None,
                 inputs=('application/pdf',),
                 tab_width = 4):
        self.config = { 'inputs' : inputs, 'tab_width' : 4}
        self.config_metadata = {
            'inputs' : ('list', 'Inputs',
                            'Input(s) MIME type. Change with care.'),
            'tab_width' : ('string', 'Tab width',
                            'Number of spaces for a tab in the input')
            }
        if name:
            self.__name__ = name

    def name(self):
        return self.__name__

    def __getattr__(self, attr):
        if attr in self.config:
            return self.config[attr]
        raise AttributeError(attr)

    def convert(self, orig, data, **kwargs):
        converter = convertPDFToImage()
        img = converter.ghostscript_transform(orig, 1)
        data.setData(img)
        return data

def register():
    return PdfToImage()
