#!/usr/bin/env python3
""" Retrieve mail attachment from mail and copy them to OneDrive following the naming standard
    Remove password protection on PDF documents.
    
    PDF naming standard:
    <YEAR>-<MONTH>-<NUMBER>.pdf
    example: 2015-november-1.pdf

Usage: 

Example: 
"""

# TODO: pdfminer: Create patch to allow pdfminer to read text from protected documents optionally


import sys
import getopt
import base64
from io import BytesIO
from imaplib import IMAP4_SSL
from pathlib import Path
from email.message import EmailMessage
from email import message_from_bytes
from email import policy

EMAIL_FOLDER = "Job/Salary"
ONEDRIVE_FOLDER = "C:\\\\Users\\dhjensen\\OneDrive\\salarytest"
helpmsg = 'mailtool.py -u username -p password -c cprnumber'
username = ''
password = ''
cpr = ''

def main(argv):
    global username, password, cpr

    try:
        opts, args = getopt.getopt(argv,"hu:p:c",["username=","password=","cpr="])
    except getopt.GetoptError:
        print(helpmsg)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpmsg)
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-c", "--cpr"):
            cpr = arg

if __name__ == "__main__":
    main(sys.argv[1:])

imap_host = 'imap.gmail.com'
imap_user = username
imap_pass = password

imap = IMAP4_SSL(imap_host, 993)
imap.login(imap_user, imap_pass)
imap.select(EMAIL_FOLDER)

rv, data = imap.search(None, 'ALL')    

for num in data[0].split():
    rv, data = imap.fetch(num, '(RFC822)')
    
    if rv != 'OK':
        print("ERROR getting message", num)
        break
    
    msg = message_from_bytes(data[0][1], policy=policy.default)

    for part in msg.walk():           
        #  Do something if the part is an 'application/pdf'
        
        if part.get_content_type() == 'application/pdf' or part.get_content_type() == 'application/octet-stram':

            AbsoluteFileName = Path(ONEDRIVE_FOLDER).joinpath(part.get_filename())         

            if AbsoluteFileName.suffix != '.pdf':                
                AbsoluteFileName = AbsoluteFileName.with_suffix('.pdf')
            
            # Write file to disk
            
            payload = part.get_payload()
            #payload_bytes = str.encode(payload)
            
            # TODO: Before writing to disk make sure to strip the password from PDF doc
            
            with open(AbsoluteFileName.resolve(), 'wb') as f:
                print('Writing: ' + AbsoluteFileName.__str__())
                f.write(base64.b64decode(payload))
                                        
            #with BytesIO(part.get_payload(decode=True)) as open_pdf_file:
                                    
                #pdf = Pdf.open(filename_or_stream = BytesIO(part.get_payload(decode=True)), password = cpr)
                #pdf.save(filename = open(AbsoluteFileName.resolve(), 'wb'))
                
                   
                        
imap.close()
imap.logout()