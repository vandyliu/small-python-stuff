#! python3

# Takes a to be filled cover letter and replaces all instances of 'XXXXX' with the company name
# To run type python.exe madLibs.py <path of template cover letter > <date?> <company name 1> <company name 2> ...
# first parameter is the script
# second parameter is the docx
# third parameter is date if you want the current date or can be the first company name
# the last parameters are all company names

# Eg. python.exe C:\Users\Vandy\PycharmProjects\ATBS\coverletter.py C:\Users\Vandy\Desktop\coverletter_blank.docx date 'Apple' 'Broadcom' 'Google'
# Eg. python.exe C:\Users\Vandy\PycharmProjects\ATBS\coverletter.py C:\Users\Vandy\Desktop\coverletter_blank.docx 'Apple' 'Broadcom' 'Google'

import sys, os, docx, datetime

if len(sys.argv) <= 2:
     print("Please write a docx path location as the second argument and company name as the third")
elif len(sys.argv) >= 3:
    include_date = False
    firstCompany = 2
    if (sys.argv[2].lower() == 'date'):
        include_date = True
        firstCompany = 3
    for company_index in range(firstCompany ,len(sys.argv)):
        company = sys.argv[company_index]
        # company = 'Apple'
        path = sys.argv[1].lower()
        # path = r'C:\Users\Vandy\Desktop\CL.docx'
        if os.path.exists(path):
            doc = docx.Document(path)
            if (include_date):
                date_paragraph = doc.paragraphs[0].insert_paragraph_before(datetime.date.today().strftime("%B %d, %Y"))

            for paragraph in doc.paragraphs:
                text = paragraph.text
                paragraph.text = text.replace('XXXXX', company)

            doc.save(os.path.join(os.path.dirname(path), company + '_CL.docx'))
        else:
            print("Wrong path")

