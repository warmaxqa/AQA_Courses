# task 6.1
proposed_string: str = input("Provide ur string here please: ")
unique_counter: int = sum([1 for char in proposed_string if proposed_string.count(char) == 1])

if unique_counter > 10:
    print(True)
else:
    print(False)

#rask 6.2

is_correct_string: bool = False

while not is_correct_string:
    provided_string = str (input("Provide ur word pls")).lower()

    if provided_string.find("h") == -1:
        is_correct_string = True

# task 6.3
 lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

desired_list: list[str] = [item for item in lst1 if isinstance(item,str)]

print(desired_list)

# task 6.4

provided_list_1: list[int] = [1,2,3,4,5,6,7,8,9,10] #30

sum_result = int
for integer in provided_list_1:
    if integer % 2 == 0:
        sum_result+= integer

print(sum_result)

