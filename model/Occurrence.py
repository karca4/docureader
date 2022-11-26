import dataclasses


@dataclasses.dataclass
class Occurrence:
  page: int
  phrase: str
  text: str
