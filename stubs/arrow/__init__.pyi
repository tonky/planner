import arrow


class Arrow:
	def weekday(self) -> int: ...
	day = ... # type: int

	@staticmethod
	def range(frame: str, start: arrow.Arrow, end: arrow.Arrow) -> List[arrow.Arrow]: ...


def get(date: str) -> arrow.Arrow: ...
