# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
from typing import List


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier

        if result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_numbers(a, b):
    return a + b


result = sum_numbers(3, 5)
print(result)

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count


numbers = [1, 2, 3, 4, 5, 6, 8, 9]
result = average(numbers)
print(result)

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(s):
    return s[::-1]


input_string = "Hillel python course"
reversed_string = reverse_string(input_string)
print(reversed_string)

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def find_longest_word(words):
    if not words:
        return None
    longest_word = max(words, key=len)
    return longest_word


words_total = ["Max", "Andrey", "Vasiliy", "Nikita", "Sasha"]
longest_word = find_longest_word(words_total)
print(longest_word)

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    index = str1.find(str2)
    return index


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 10
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# LESSON 4, HOMEWORK 4, TASK 2 (Замініть .... на пробіл)
def replace_and_normalize(text):
    text = text.replace('....', ' ')
    normalized_text = ' '.join(text.split())
    return normalized_text

adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash
"""

normalized_text = replace_and_normalize(adventures_of_tom_sawyer)
print(normalized_text)

# LESSON 4, HOMEWORK 4, TASK 4 (Виведіть, скількі разів у тексті зустрічається літера "h")

def count_letter_h(text):
    count = text.count('h')
    return count

adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
"""

h_count = count_letter_h(adventures_of_tom_sawyer)
print(f"The letter 'h' appears {h_count} times in the text.")

# LESSON 4, HOMEWORK 4, TASK 5 (Виведіть, скільки слів у тексті починається з Великої літери?)

def count_uppercase_words(text):
    words = text.split()
    count = sum(1 for word in words if word[0].isupper())
    return count

adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
"""

uppercase_words_count = count_uppercase_words(adventures_of_tom_sawyer)
print(f"The number of words starting with an uppercase letter is {uppercase_words_count}.")

# LESSON 4, HOMEWORK 4, TASK 6 (Виведіть позицію, на якій слово Tom зустрічається вдруге)

def find_second_occurrence(text, word):
    first_occurrence = text.find(word)
    if first_occurrence == -1:
        return -1
    second_occurrence = text.find(word, first_occurrence + len(word))
    return second_occurrence

adventures_of_tom_sawyer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""


second_tom_position = find_second_occurrence(adventures_of_tom_sawyer, "Tom")
print(f"The position of the second occurrence of the word 'Tom' is {second_tom_position}.")







