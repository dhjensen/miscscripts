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

# TODO: Test extracting dates for filenames from a broather list of PDF documents
# Alternative description: pdfminer: Use https://github.com/pdfminer/pdfminer.six to get month / year from salary documents for naming purposes

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from dateparser import parse
from datetime import datetime

""" Gets any text in a protected pdf document provided in path argument

"""
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

""" Returns a filename based on extracted text from pdf file provided in text argument   

"""
def create_file_name(text: str) -> str:
    
    pdf_text = text

    index_string = 'Udskrevet '
    index_string_lenght = len(index_string)
    temp_date_string = pdf_text[pdf_text.index(index_string)+index_string_lenght:-1]
    date_string = temp_date_string[0:temp_date_string.index('\n')]

    printed_date = parse(date_string)

    # PDF naming standard:
    # <YEAR>-<MONTH>-<NUMBER>.pdf
    # example: 2015-november-1.pdf
    file_name_string = '{0:%Y}-{0:%B}-{1}.pdf'.format(printed_date, 1)
    
    return file_name_string

def main():
    extracted_text = extract_protected_pdf_text(path = 'pdfin\\15935_22801.pdf')
    file_name = create_file_name(text = extracted_text)
    print(file_name)

if __name__ == '__main__':
    main()
