#!/usr/bin/env python3
""" Retrieve mail attachment from mail and copy them to OneDrive

Usage: 
    

Example: 
"""

import imaplib
import sys
import getopt
from email.message import EmailMessage
from email import message_from_bytes
from email import policy

# Use 'INBOX' to read inbox.  Note that whatever folder is specified, 
# after successfully running this script all emails in that folder 
# will be marked as read.
EMAIL_FOLDER = "Job/Salary"
username = ''
password = ''
helpmsg = 'test.py -u username -p password'

def main(argv):
    global username, password

    try:
      opts, args = getopt.getopt(argv,"hu:p:",["username=","password="])
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

if __name__ == "__main__":
    main(sys.argv[1:])

imap_host = 'imap.gmail.com'
imap_user = username
imap_pass = password

# connect to host using SSL
imap = imaplib.IMAP4_SSL(imap_host, 993)

## login to server
imap.login(imap_user, imap_pass)

imap.select(EMAIL_FOLDER)

rv, data = imap.search(None, 'ALL')
for num in data[0].split():
    rv, data = imap.fetch(num, '(RFC822)')
    
    if rv != 'OK':
        print("ERROR getting message", num)
        break
    
    #msg = email.message_from_string(data[0][1].decode('utf-8'))
    msg = message_from_bytes(data[0][1], policy=policy.default)

    for part in msg.walk():
        # multipart/* are just containers
        if part.get_content_maintype() == 'multipart':
            continue
            

        #  and "creation-date" in part
        if part.is_attachment():
            print(part.get_filename())
            #print(part["date"])

        # TO-DO: make sure PDF document have no password and store it in OneDrive

    # print("Raw date:", msg['Date'] )

    # print(msg)

    # if msg['X-MS-Has-Attach'] == "yes":
    #     print("Muuh:", msg['Content-Description'] )
    #     print("Disposition", msg['Content-Disposition'])

    #print('Message: {0}\n'.format(num))
    #pprint.pprint(data[0][1])
    break

imap.close()
imap.logout()