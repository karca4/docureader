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


def find_text_containing_index(text: str, index: int, keyword_offset):
  return text[index - keyword_offset:index + keyword_offset]
