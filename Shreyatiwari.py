import PyPDF2

pdf_file = open('one.pdf', 'rb')


pdf_reader = PyPDF2.PdfReader(pdf_file)


num_pages = len(pdf_reader.pages)


for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    page_text = page.extract_text()
    print(f'Page {page_num + 1}:\n{page_text}')


pdf_file.close()
