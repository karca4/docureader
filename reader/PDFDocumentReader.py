import logging
import re
import traceback
from pathlib import Path
from typing import Optional, List

from PyPDF2 import PdfReader

from model.DocumentInfo import DocumentInfo
from model.Occurrence import Occurrence
from reader.DocumentReader import DocumentReader
from reader.search import find_phrase_containing_index, find_text_containing_index

logger = logging.getLogger()


class PDFDocumentReader(DocumentReader):
  __file: PdfReader
  __filename: str
  __info: Optional[DocumentInfo] = None

  def __init__(self, filepath: str):
    self.__file = PdfReader(filepath)
    self.filename = Path(filepath).name
    self.__metadata_info()

  def get_filename(self):
    return self.filename

  def get_pages_number(self) -> int:
    return len(self.__file.pages)

  def __metadata_info(self):
    meta = self.__file.metadata
    subject, title, keywords, author, year, producer = None, None, None, None, None, None

    try:
      year = meta.creation_date.year
    except Exception as e:
      traceback.print_exc()
      logger.error(e)
      pass

    if meta is not None:
      subject = meta.subject
      title = meta.title
      keywords = meta.getText('/Keywords')
      author = meta.author
      producer = meta.producer

    self.__info = DocumentInfo(subject, title, keywords, self.get_pages_number(), author, year, producer)

  def get_metadata_info(self):
    return self.__info

  def find_all_occurrences(self, to_find: str, keyword_offset: int = 250) -> List[Occurrence]:
    occurrences: List[Occurrence] = []

    for page_number in range(self.__info.pages):
      occurrences_idx: List[int] = list()
      page = self.__file.pages[page_number]
      text = page.extract_text()

      occurrences_idx.extend([m.start() for m in re.finditer(to_find, text)])
      if len(occurrences_idx):
        logger.debug(f"Occurrences found in page {page_number}: {occurrences_idx}")
        for index in occurrences_idx:
          phrase = find_phrase_containing_index(text, index)
          text_block = find_text_containing_index(text, index, keyword_offset)

          logger.debug(f"Phrase: {phrase}")
          logger.debug(f"Text: {text_block}")

          occurrences.append(Occurrence(page_number + 1, phrase, text[index - keyword_offset:index + keyword_offset]))
      else:
        logger.debug(f"No occurrences found in page {page_number}")
        pass
    return occurrences
