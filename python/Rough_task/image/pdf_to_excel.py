# # Import Module
# import pdftables_api

# # API KEY VERIFICATION
# conversion = pdftables_api.Client('API KEY')

# # PDf to Excel
# # (Hello.pdf, Hello)
# conversion.xlsx("address.pdf", "address.xlsx")


# # Import Module
# import tabula
# from tabula.io import read_pdf

# # Read PDF File
# # this contain a list
# df = read_pdf("/home/praveen/Learning/python/Rough_task/image/address.pdf", pages = 1)
# print(df)
# # Convert into Excel File
# df.to_excel('/home/praveen/Learning/python/Rough_task/image/saddress.xlsx')
import pandas as pd
import pdfplumber
from collections import namedtuple

lines = []
Line = namedtuple('Line', 'EmployeeCode Name Location Department Gender')


def pdf_to_excel(pdf_file_path):

    with pdfplumber.open(pdf_file_path) as pdf:
        for pages in pdf.pages:
            text = pages.extract_text()
            for line in text.split("\n"):
                if line.startswith("YT"):
                    li = line.split(" ")
                    lines.append(Line(*li))

    df = pd.DataFrame(lines)
    # print(df.head())
    df.to_csv('test.csv', index=False)


if __name__ == "__main__":
    pdf_to_excel(
        "/home/praveen/Learning/python/Rough_task/image/Employee_details.pdf")
