#!/usr/bin/env python3
""" Test shit

Usage: 

Example: 
"""

import pikepdf

ONEDRIVE_FOLDER = 'C:\\\\Users\\dhjensen\\OneDrive\\salarytest\\'

pdf = pikepdf.open('pdf\\15935_22801.pdf')

if pdf.is_encrypted:
    print('Encrypted')
    pdf.open('pdf\\15935_22801.pdf')

#pdf.save('pdf\\15935_22801.pdf')





#print(pdf.Pdf)