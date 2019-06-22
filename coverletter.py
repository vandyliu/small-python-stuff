#! python3

# Takes a to be filled cover letter and replaces all instances of 'XXXXX' with the company name
# To run type python.exe madLibs.py <path of template cover letter > <company name> <date?>
# first parameter is the script
# second parameter is the docx
# third parameter is the company name
# NOT YET IMPLEMENTED fourth parameter is date to include the current date or anything else to not include the current date
# Eg. python.exe C:\Users\Vandy\PycharmProjects\ATBS\coverletter.py C:\Users\Vandy\Desktop\coverletter_blank.docx 'apple'

# Add date later!!!

import sys, os, docx

if len(sys.argv) <= 2:
     print("Please write a docx path location as the second argument and company name as the third")
elif len(sys.argv) >= 3:
    company = sys.argv[2]
    # company = 'Apple'
    path = sys.argv[1].lower()
    # path = r'C:\Users\Vandy\Desktop\CL.docx'
    if os.path.exists(path):
        doc = docx.Document(path)
        for paragraph in doc.paragraphs:
            text = paragraph.text
            paragraph.text = text.replace('XXXXX', company)
        for paragraph in doc.paragraphs:
            print(paragraph.text)

        doc.save(os.path.join(os.path.dirname(path), company + '_CL.docx'))
    else:
        print("Wrong path")

