from PyPDF2 import *

file_path = "C:\\Users\\002CL0744\Documents\\NLP-NaturalLanguageProcessing\\Working With PDF\\US_Declaration.pdf"
myfile = open(file_path, mode="rb") #reading in binary method
pdf_reader = PdfReader(myfile) #convert in PDF file object
print(f"Number of pages in file {len(pdf_reader.pages)}")
page_one = pdf_reader.pages[0]
print(f"Text from first page of the file:\n{page_one.extract_text()}")
myfile.close()

#Add a page to PDF
f = open(file_path, mode="rb") #reading in binary method
pdf_reader = PdfReader(f)
first_page = pdf_reader.pages[0]
#create writer object
pdf_writer = PdfWriter()
pdf_writer.add_page(first_page)
pdf_output = open('MY_BRAND_NEW_PDF',"wb")
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()

#read new file
brand_new = open("MY_BRAND_NEW_PDF","rb")
pdf_reader = PdfReader(brand_new)
print(f"Number of pages in new file {len(pdf_reader.pages)}")
first_page = pdf_reader.pages[0]
print(f"Text from first page of the new file:\n{page_one.extract_text()}")
brand_new.close()

#get all the text from a PDF file
f = open(file_path,'rb')
pdf_text = [] #creating empty list for storing page's text
pdf_reader = PdfReader(f)
for p in range (len(pdf_reader.pages)):
    page = pdf_reader.pages[p]
    pdf_text.append(page.extract_text())
f.close()

print(f"Text of the entire PDF: {pdf_text}")
print(len(pdf_text))

for page in pdf_text:
    print(f"Text of page {pdf_text.index(page)+1}\n{page}")
    print("\n\n\n")
