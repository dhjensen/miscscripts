""" Try module for reading text from pdf documents

https://github.com/pdfminer/pdfminer.six

Usage: 

Example: 
"""

# Have to comment out line 131-132 in pdfpage.py in pdfminer to extract text:
        # if check_extractable and not doc.is_extractable:
        #     raise PDFTextExtractionNotAllowed('Text extraction is not allowed: %r' % fp)
from pdfminer.high_level import extract_text

pdf_text = extract_text(pdf_file = 'pdfin\\15935_22801.pdf')

# TODO: extract date string and find month + year