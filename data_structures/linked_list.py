class _ListElement:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    class WrongIndexException(Exception):
        pass

    class InvalidElementException(Exception):
        pass

    def __init__(self) -> None:
        self._root = None
        self._length = 0

    def __len__(self):
        return self._length

    def _find_element(self, index: int) -> _ListElement:
        element = self._root
        if element is None:
            raise self.InvalidElementException

        if index > self._length:
            raise self.WrongIndexException

        for i in range(index):
            element = element.next

        return element

    def _add_element(self, index: int, element: _ListElement) -> None:
        if index == 0:
            element.next = self.root
            self.root = element

        elif index == len(self):
            prev_element = self._find_element(len(self)-1)
            prev_element.next = element
            element.next = None

        else:
            prev_element = self._find_element(index-1)
            next_element = prev_element.next

            element.next = next_element
            prev_element.next = element

        self._length += 1

    def add_element(self, index: int, data) -> None:
        element = _ListElement(data)
        self._add_element(index, element)
