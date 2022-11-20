import dataclasses
from typing import Optional, List


@dataclasses.dataclass
class DocumentInfo:
  subject: Optional[str]
  title: Optional[str]
  keywords: Optional[str]
  pages: Optional[int]
  author: Optional[str]
  year: Optional[int]
  producer: Optional[str]


@dataclasses.dataclass
class Occurrence:
  page: int
  phrase: str
  text: str
