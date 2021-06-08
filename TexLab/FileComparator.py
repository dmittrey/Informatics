import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


def convert(file_name, pages=None):
    if not pages:
        page_nums = set()
    else:
        page_nums = set(pages)

    output = io.StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(file_name, 'rb')
    for page in PDFPage.get_pages(infile, page_nums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close()
    return text


def compare_files(first_pdf_file, second_pdf_file):
    return convert(first_pdf_file) == convert(second_pdf_file)
