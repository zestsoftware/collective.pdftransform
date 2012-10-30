from collective.pdfpeek.transforms import subprocess, convertPDFToImage, logger

DEFAULT_OPTIONS = {'quality': '99',
                   'graphicsAlphaBits': '4',
                   'textAlphaBits': '4',
                   'resolution': '59x56',
                   'extra': ["-dDOINTERPOLATE",
                             "-dSAFER",
                             "-dBATCH",
                             "-dNOPAUSE"]}

def ghostscript_transform(self, pdf, page_num, options=None):
    """
    ghostscript_transform takes an AT based object with an IPDF interface
    and a page number argument and converts that page number of the pdf
    file to a png image file.
    """
    if options is None:
        options = DEFAULT_OPTIONS

    first_page = "-dFirstPage=%s" % (page_num)
    last_page = "-dLastPage=%s" % (page_num)

    gs_cmd = ["gs",
              "-q",
              "-sDEVICE=jpeg",
              "-dJPEGQ=%s" % options['quality'],
              "-dGraphicsAlphaBits=%s" % options['graphicsAlphaBits'],
              "-dTextAlphaBits=%s" % options['graphicsAlphaBits']
              ] + \
              options['extra'] + \
              ["-r%s" % options['resolution'],
               first_page,
               last_page,
               "-sOutputFile=%stdout",
               "-",
               ]

    jpeg = None
    """run the ghostscript command on the pdf file,
    capture the output png file of the specified page number"""
    gs_process = subprocess.Popen(gs_cmd,stdout=subprocess.PIPE,stdin=subprocess.PIPE,)
    gs_process.stdin.write(pdf)
    jpeg = gs_process.communicate()[0]
    gs_process.stdin.close()
    return_code = gs_process.returncode
    if return_code == 0:
        logger.info("Ghostscript processed one page of a pdf file.")
    else:
        logger.warn("Ghostscript process did not exit cleanly! Error Code: %d" % (return_code))
        jpeg = None
    return jpeg



def patch_pdfpeek():
    convertPDFToImage._old_gs_transform = convertPDFToImage.ghostscript_transform
    convertPDFToImage.ghostscript_transform = ghostscript_transform

def unpatch_pdfpeek():
    convertPDFToImage.ghostscript_transform = convertPDFToImage._old_gs_transform
