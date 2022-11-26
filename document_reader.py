import abc
import logging
import re
import traceback
from pathlib import Path
from typing import Optional, List

from PyPDF2 import PdfReader

from model import DocumentInfo, Occurrence

logger = logging.getLogger()


class DocumentReader(abc.ABC):
  @abc.abstractmethod
  def get_filename(self) -> str:
    pass

  @abc.abstractmethod
  def get_metadata_info(self) -> Optional[DocumentInfo]:
    pass

  @abc.abstractmethod
  def find_all_occurrences(self, to_find: str, keyword_offset: int = 250) -> List[Occurrence]:
    pass


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

  def __metadata_info(self):
    meta = self.__file.metadata
    subject, title, keywords, pages, author, year, producer = None, None, None, None, None, None, None

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

    self.__info = DocumentInfo(subject, title, keywords, self.__file.getNumPages(), author, year, producer)

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

          logger.debug(f"Phrase: {phrase}")
          logger.debug(f"Text: {text[index - keyword_offset:index + keyword_offset]}")

          occurrences.append(Occurrence(page_number + 1, phrase, text[index - keyword_offset:index + keyword_offset]))
      else:
        logger.debug(f"No occurrences found in page {page_number}")
        pass
    return occurrences


def find_phrase_containing_index(text: str, index: int):
  start_index = index
  end_index = index

  while True:
    start_index = start_index - 1
    if text[start_index] == "." or start_index == 0:
      break
  while True:
    end_index = end_index + 1
    if text[end_index] == "." or end_index == len(text) - 1:
      break

  # +1 in start index to remove '.' character. +1 in end index to add '.' character
  return text[start_index + 1:end_index + 1]
