import argparse
import logging
from datetime import datetime
from typing import Optional, List

from document_reader import PDFDocumentReader, DocumentReader
from model import DocumentInfo, Occurrence
from utils import get_filenames_from_path, write_file_result

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def work(key_to_search: str, path_dir: str, result_path_dir: str):
  start_datetime = datetime.now()

  reader: DocumentReader
  logger.info(f"Work in path {path_dir}")
  logger.info(f"Search for key: {key_to_search}")
  result_file_path = f"{result_path_dir}/{key_to_search}{start_datetime.strftime('%m-%d-%Y,%H:%M:%S.%f')[:-3]}.txt"

  for filename in get_filenames_from_path(path_dir):
    info: Optional[DocumentInfo]
    occurrences: List[Occurrence]

    if filename.split(".")[-1] == "pdf":
      logger.info(f"Analyzing PDF: {filename}")
      reader = PDFDocumentReader(f"{path_dir}/{filename}")
      info = reader.get_metadata_info()
      analyzed_filename = reader.get_filename()
      occurrences = reader.find_all_occurrences(key_to_search)

      write_file_result(result_file_path, analyzed_filename, info, occurrences)
    else:
      logger.info(f"Discard no PDF file: {filename}")
  logger.info(f"Results available in file: {result_file_path}")
  logger.info(f"Execution time: {datetime.now()-start_datetime}")


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-s", "--search", required=True, help="Search key into files")
  parser.add_argument("-i", "--input_path", help="Directory path containing files")
  parser.add_argument("-r", "--result_path", help="Directory path containing results")
  args = parser.parse_args()

  work(args.search, args.input_path or "input/docs", args.result_path or "output/results")
