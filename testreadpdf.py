""" Try module for reading text from pdf documents

https://github.com/pdfminer/pdfminer.six

Usage: 

Example: 

"""

# # Have to comment out line 131-132 in pdfpage.py in pdfminer to extract text:
#         # if check_extractable and not doc.is_extractable:
#         #     raise PDFTextExtractionNotAllowed('Text extraction is not allowed: %r' % fp)
# from pdfminer.high_level import extract_text

# pdf_text = extract_text(pdf_file = 'pdfin\\15935_22801.pdf')

# TODO: extract date string and find month + year

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def extract_protected_pdf_text(path):
    
    output = StringIO()

    resource_manager = PDFResourceManager()
    laparams = LAParams()

    device = TextConverter(resource_manager, output, codec='utf-8', laparams=laparams)

    pdf_infile = open(path, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, device)

    page_numbers = set()
    
    for page in PDFPage.get_pages(pdf_infile, page_numbers, maxpages=0, caching=True, check_extractable=False):
        interpreter.process_page(page)

    text = output.getvalue()
    pdf_infile.close()
    device.close()
    output.close()
    return text

pdf_text = extract_protected_pdf_text(path = 'pdfin\\15935_22801.pdf')