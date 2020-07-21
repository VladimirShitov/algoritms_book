import pytest

from data_structures.linked_list import LinkedList


def test_empty_list_creation():
    l_list = LinkedList()
    assert len(l_list) == 0
    with pytest.raises(LinkedList.WrongIndexException):
        l_list.get_element_data(index=0)
    with pytest.raises(LinkedList.WrongIndexException):
        l_list.get_element_data(index=666)


def test_list_with_one_element():
    l_list = LinkedList()
    l_list.add_element(index=0, data=123)

    assert len(l_list) == 1
    assert l_list.get_element_data(0) == 123


def test_wrong_index():
    l_list = LinkedList()

    with pytest.raises(LinkedList.WrongIndexException):
        l_list.get_element_data(1)

    with pytest.raises(LinkedList.WrongIndexException):
        l_list.get_element_data(-1)

    with pytest.raises(LinkedList.WrongIndexException):
        l_list.get_element_data(0)


def test_getting_element():
    l_list = LinkedList()

    l_list.add_element(index=0, data=1)
    assert l_list.get_element_data(index=0) == 1
    assert len(l_list) == 1

    l_list.add_element(index=0, data=5)
    assert l_list.get_element_data(index=0) == 5
    assert len(l_list) == 2

    l_list.add_element(index=2, data=7)
    assert l_list.get_element_data(index=2) == 7
    assert l_list.get_element_data(index=1) == 1
    assert len(l_list) == 3


def test_to_list():
    l_list = LinkedList()
    for i in range(10):
        l_list.add_element(index=i, data=i)
    assert l_list.to_list() == list(range(10))


def test_delete_element():
    l_list = LinkedList()
    l_list.add_element(index=0, data="Hi!")

    assert len(l_list) == 1

    l_list.delete_element(index=0)
    assert len(l_list) == 0
    with pytest.raises(LinkedList.WrongIndexException):
        l_list.get_element_data(index=0)


def test_delete_many_elements():
    l_list = LinkedList()

    for i in range(10):
        l_list.add_element(index=i, data=i)

    assert len(l_list) == 10

    l_list.delete_element(len(l_list)-1)
    assert len(l_list) == 9

    l_list.delete_element(0)
    assert len(l_list) == 8

    l_list.delete_element(5)
    assert len(l_list) == 7

    l_list.add_element(index=5, data="wubbalubbadubdub")
    assert len(l_list) == 8
    assert l_list.to_list() == [1, 2, 3, 4, 5, "wubbalubbadubdub", 7, 8]

