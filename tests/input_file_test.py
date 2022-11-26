from model.DocumentInfo import DocumentInfo
from reader.PDFDocumentReader import PDFDocumentReader


def test_filename():
  reader = PDFDocumentReader(filepath="./tests/res/harvard-research-paper-sample.pdf")
  assert reader.get_filename() == "harvard-research-paper-sample.pdf"


def test_file_pages():
  reader = PDFDocumentReader(filepath="./tests/res/harvard-research-paper-sample.pdf")
  assert reader.get_pages_number() == 7


def test_file_metadata():
  info: DocumentInfo

  reader = PDFDocumentReader(filepath="./tests/res/harvard-research-paper-sample.pdf")
  info = reader.get_metadata_info()
  assert info.__dict__ == {
    'subject': 'Research Paper Example - Free Samples for Students',
    'title': 'Research Paper Example - Free Samples for Students',
    'keywords': '',
    'pages': 7,
    'author': '',
    'year': 2013,
    'producer': 'LibreOffice 3.5',
  }

