
# lesson_06, homework_06 task 6.1
# proposed_string: str = input("Provide ur string here please: ")
# unique_counter: int = sum([1 for char in proposed_string if proposed_string.count(char) == 1])
#
# if unique_counter > 10:
#     print(True)
# else:
#     print(False)

def has_more_than_10_unique_chars(proposed_string: str) -> bool:
    unique_counter = sum([1 for char in proposed_string if proposed_string.count(char) == 1])
    return unique_counter > 10


