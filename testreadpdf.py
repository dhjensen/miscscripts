""" Try module for reading text from pdf documents

https://github.com/pdfminer/pdfminer.six

Usage: 

Example: 

"""

# # Have to comment out line 131-132 in pdfpage.py in pdfminer to extract text:
#         # if check_extractable and not doc.is_extractable:
#         #     raise PDFTextExtractionNotAllowed('Text extraction is not allowed: %r' % fp)
# from pdfminer.high_level import extract_text

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from dateparser import parse
from datetime import datetime
from pikepdf import Pdf
import os

""" Gets any text in a protected pdf document provided in path argument

"""
def extract_protected_pdf_text(path: str, password: str) -> str:
    
    output = StringIO()

    resource_manager = PDFResourceManager()
    laparams = LAParams()
    
    device = TextConverter(resource_manager, output, codec='utf-8', laparams=laparams)

    pdf_infile = open(path, 'rb')
    interpreter = PDFPageInterpreter(resource_manager, device)

    page_numbers = set()
    
    if password is None:
        for page in PDFPage.get_pages(pdf_infile, page_numbers, maxpages=0, caching=True, check_extractable=False):
            interpreter.process_page(page)
    else:
        for page in PDFPage.get_pages(pdf_infile, page_numbers, maxpages=0, password=password, caching=True, check_extractable=False):
            interpreter.process_page(page)
    
    text = output.getvalue()
    pdf_infile.close()
    device.close()
    output.close()
    return text

""" Returns a filename based on extracted text from pdf file provided in text argument   

"""
def create_file_name(text_or_filename: str) -> str:
    
    index_string = 'Udskrevet '
    
    if index_string in text_or_filename:
        pdf_text = text_or_filename

        index_string_lenght = len(index_string)
        temp_date_string = pdf_text[pdf_text.index(index_string)+index_string_lenght:-1]
        date_string = temp_date_string[0:temp_date_string.index('\n')]

        printed_date = parse(date_string)

        # PDF naming standard:
        # <YEAR>-<MONTH>-<NUMBER>.pdf
        # example: 2015-november-1.pdf
        file_name_string = '{0:%Y}-{0:%B}-{1}.pdf'.format(printed_date, 1)
    else:
        file_name = text_or_filename

        temp_list = file_name.split('\\')
        temp_string = temp_list[-1]
        
        temp_date = temp_string[0:temp_string.index('_', 0, -1)]
                       
        file_name_string = temp_date + '-1.pdf'
        
    return file_name_string

""" Removes encryption from PDF and safe it to disk

"""
def remove_password_and_save(input_path: str, output_path: str):
    with Pdf.open(input_path) as pdf:
        pdf.save(filename = output_path, encryption = None)
        
""" 

"""
def get_pdf_files_list(path: str):

    files_return = []
    for root, directories, files in os.walk(path):
        for file in files:
            if '.pdf' in file:
                files_return.append(os.path.join(root, file))
                
    return files_return

def main():
    source_path = 'C:\\Users\\dhjensen\\OneDrive\\salarytest'
    
    files = get_pdf_files_list(source_path)
    
    for file in files:
        
        if 'Daniel_Jensen' in file:
            print ('Daniel_Jensen: ' + file)
            file_name = create_file_name(text_or_filename = file)
            output_file_name = 'pdfout\\' + file_name
            print (output_file_name)
        elif '22801 - Daniel - Lønspecifikation maj 2018.pdf' in file:
            print('22801 - Daniel - Lønspecifikation maj 2018.pdf')
            extracted_text = extract_protected_pdf_text(path=file, password=None)
            file_name = create_file_name(text_or_filename = extracted_text)
            output_file_name = 'pdfout\\' + file_name
            print (output_file_name)
        elif '22801' in file:
            print('22801 baby: ' + file)
            extracted_text = extract_protected_pdf_text(path=file, password='2505832461')
            file_name = create_file_name(text_or_filename = extracted_text)
            output_file_name = 'pdfout\\' + file_name
            print (output_file_name)
        else:
            print('File we do not handle: ' + file)

if __name__ == '__main__':
    main()
