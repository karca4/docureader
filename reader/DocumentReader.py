import abc
from typing import Optional, List

from model.DocumentInfo import DocumentInfo
from model.Occurrence import Occurrence


class DocumentReader(abc.ABC):
  @abc.abstractmethod
  def get_filename(self) -> str:
    pass

  @abc.abstractmethod
  def get_pages_number(self) -> int:
    pass

  @abc.abstractmethod
  def get_metadata_info(self) -> Optional[DocumentInfo]:
    pass

  @abc.abstractmethod
  def find_all_occurrences(self, to_find: str, keyword_offset: int = 250) -> List[Occurrence]:
    pass
