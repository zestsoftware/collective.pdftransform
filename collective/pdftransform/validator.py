import PIL

from Products.validation.interfaces import ivalidator
from zope.i18n import translate
from collective.pdftransform import PDFTransformMessageFactory as _

from utils import is_pdf, is_transformable_pdf

class ImageOrPDFValidator:
    """ Checks that the file uploaded is a pdf or an image file.
    Also check that it is not a BMP file.
    """
    __implements__ = (ivalidator, )

    def __init__(self, name):
        self.name = name

    def __call__(self, value, *args, **kwargs):
        error = ''
        if value == 'DELETE_IMAGE':
            return True

        if is_pdf(value):
            if is_transformable_pdf(value):
                return True

            error = _(u'error_pdf_no_transformable',
                      default = u'The PDF file provided can not be used, ' + \
                      'please ensure that this is a valid PDF file and ' + \
                      'that it is not password protected.')
            return translate(error, context=kwargs['REQUEST'])

        value.seek(0)
        try:
            image = PIL.Image.open(value)
            if image.format == 'BMP':
                error = _(u'error_img_validation_bmp',
                          default=u'Bitmap images can not be used. ' + \
                          'Please use one of the following type: ' + \
                          'jpg, gif, png or pdf')

        except:
            error = _(u'error_img_validation_no_image',
                      default=u'The file you submitted in not an image' + \
                      ' file. Please use one of the following type: ' + \
                      'jpg, gif, png or pdf')

        if error:
            return translate(error, context=kwargs['REQUEST'])
        return True
