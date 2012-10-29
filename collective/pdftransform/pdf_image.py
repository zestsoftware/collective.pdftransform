from zope.interface import implements
from Products.PortalTransforms.interfaces import itransform

from collective.pdfpeek.transforms import convertPDFToImage, DEFAULT_OPTIONS

class PdfToImage:
    """Transforms PDF to jpg images."""

    __implements__ = itransform

    __name__ = "pdf_to_image"
    output = "image/jpeg"

    def __init__(self,
                 name=None,
                 inputs=None,
                 tab_width=None,
                 resolution=None,
                 quality=None):

        if inputs is None:
            inputs = ('application/pdf',)

        if tab_width is None:
            tab_width = 4

        if resolution is None:
            resolution = DEFAULT_OPTIONS['resolution']

        if quality is None:
            quality = DEFAULT_OPTIONS['quality']

        self.config = {'inputs' : inputs,
                       'tab_width' : 4,
                       'resolution': resolution,
                       'quality': quality}

        self.config_metadata = {
            'inputs' : ('list', 'Inputs',
                        'Input(s) MIME type. Change with care.'),
            'tab_width' : ('string', 'Tab width',
                           'Number of spaces for a tab in the input'),
            'resolution' : ('string', 'Resolution',
                            'Default resolution'),
            'quality': ('string', 'Quality',
                        'PDF quality')
            }
        if name:
            self.__name__ = name

    def get_options(self):
        """ Uses the default options from pdfpeek.
        Checks in portal_properties if any is overriden.
        """
        options = dict([(k, v) for k, v in DEFAULT_OPTIONS.items()])
        for key in options:
            p_val = self.config.get(key, None)
            if p_val is not None:
                options[key] = p_val

        return options

    def name(self):
        return self.__name__

    def __getattr__(self, attr):
        if attr in self.config:
            return self.config[attr]
        raise AttributeError(attr)

    def convert(self, orig, data, **kwargs):
        converter = convertPDFToImage()
        options = self.get_options()

        if kwargs.get('pdf_resolution', None) is not None:
            options['resolution'] = kwargs['pdf_resolution']

        img = converter.ghostscript_transform(orig, 1, options)
        data.setData(img)
        return data

def register():
    return PdfToImage()
