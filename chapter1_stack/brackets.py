from data_structures.stack import Stack


def is_bracket_sequence_valid(sequence: str) -> bool:
    brackets_map: dict = {
        "[": "]",
        "{": "}",
        "(": ")",
    }
    opening_brackets = {"[", "(", "{"}
    closing_brackets = {"]", ")", "}"}

    stack = Stack()
    for symbol in sequence:
        if symbol in opening_brackets:
            stack.push(symbol)
        elif symbol in closing_brackets:
            if stack.is_empty():
                return False
            stack_top = stack.pop()
            if brackets_map[stack_top] != symbol:
                return False
        else:
            raise ValueError(f"Symbol {symbol} is not allowed")

    return stack.is_empty()
