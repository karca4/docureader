import os
from typing import Generator, List

from model import Occurrence, DocumentInfo


def get_filenames_from_path(path: str) -> Generator[str, None, None]:
  for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
      yield file


def write_file_result(result_file_path: str, analyzed_filename: str, info: DocumentInfo, occurrences: List[Occurrence]):
  with open(result_file_path, "a") as f:
    f.write(f"Filename: {analyzed_filename}\n")
    f.write(f"Title: {info.title}\n")
    f.write(f"Subject: {info.subject}\n")
    f.write(f"Keywords: {info.keywords}\n")
    f.write(f"Author: {info.author}\n")
    f.write(f"Year: {info.year}\n")
    f.write(f"Pages: {info.pages}\n")
    f.write(f"Found {len(occurrences)} occurrences\n")
    for occ in occurrences:
      f.write(f"Page: {occ.page}\n")
      f.write(f"Phrase: {occ.phrase}\n")
      f.write(f"Text: {occ.text}\n\n")
    f.write("===========================================================================\n\n")
