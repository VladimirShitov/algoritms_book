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

        for i in range(index):
            element = element.next

        return element

    def _add_element(self, index: int, element: _ListElement) -> None:
        if index == 0:
            element.next = self._root
            self._root = element

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
        if not 0 < index <= self._length:
            raise self.WrongIndexException

        element = _ListElement(data)
        self._add_element(index, element)

    def delete_element(self, index: int):
        if not 0 < index < self._length:
            raise self.WrongIndexException

        if index == 0:
            element = self._root.next  # It is an existing element or None if length of the list equals 0
            del self._root
            self._root = element
        elif index == len(self)-1:
            element = self._find_element(index)
            del element
        else:
            prev_element = self._find_element(index-1)
            element = prev_element.next
            prev_element.next = element.next
            del element

        self._length -= 1

    def get_element_data(self, index: int):
        if not 0 < index < self._length:
            raise self.WrongIndexException

        element = self._find_element(index)
        return element.data

    def to_list(self):
        data_list = []

        element = self._root
        while element is not None:
            data_list.append(element.data)
            element = element.next

        return data_list
