from Products.CMFCore.utils import getToolByName
from ZPublisher.HTTPRequest import FileUpload
from zope.app.component.hooks import getSite

class FakeData:
    """ portal_transforms expects some data object, we fake it
    here.
    """
    def setData(self, d):
        self.data = d

    def getData(self):
        return self.data

def is_pdf(file):
    """ Tells if a file is a PDF or not.
    """
    return file.headers.get('content-type') == 'application/pdf'

def is_transformable_pdf(file):
    """ Tells if a file can be transformed using pdfpeek.
    """
    if not is_pdf(file):
        return False

    portal = getSite()
    transform = getToolByName(portal, 'portal_transforms')
    data = FakeData()

    file.seek(0)
    transformable = True
    try:
        transform.pdf_to_image.convert(file.read(), data)
    except:
        transformable = False

    if not data.getData():
        transformable = False

    file.seek(0)
    return transformable

def update_form(context, request, fields = []):
    """ Transforms every pdf files in request.form
    into images.
    fields can be used to limit to a certain list of
    fields.
    """
    transform = getToolByName(context, 'portal_transforms')
    if not fields:
        fields = request.form.keys()

    for field in fields:
        if not field in request.form:
            # Should not happen, except if the user specified a wrong
            # field name.
            # XXX - raise an exception or log something.
            continue

        if not isinstance(request.form[field], FileUpload):
            # That not a file upload.
            continue

        f = request.form[field]
        if not is_transformable_pdf(f):
            # Not a PDF we can transform, nothing to do.
            continue

        data = FakeData()
        f.seek(0)
        transform.pdf_to_image.convert(f.read(), data)

        f.seek(0)
        f.truncate()
        f.write(data.getData())
        f.filename = f.filename.replace('.pdf', '.jpg')
        f.headers['content-type'] = 'image/jpeg'
        f.seek(0)

        request.form[field] = f

    return request.form
