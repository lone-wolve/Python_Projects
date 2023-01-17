import PyPDF2

with open('recipe-book.pdf', 'r+b') as f:
    reader = PyPDF2.PdfFileReader(f)
    # print(reader.numPages)
    # print(reader.getDocumentInfo())page
    for page in range(0, reader.numPages):

        pageObj = reader.getPage(page)
        print("\n", pageObj.extract_text())
    
    