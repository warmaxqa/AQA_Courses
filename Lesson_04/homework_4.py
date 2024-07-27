adwentures_of_tom_sawer = """\
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

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
text = ' '.join(adwentures_of_tom_sawer.split())
print(text)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
letter_h_count = adwentures_of_tom_sawer.count("h")
print(letter_h_count)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
capitalize_words = 0

for word in words:
    if word[0].isupper():
        capitalize_words +=1

print(capitalize_words)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
words = adwentures_of_tom_sawer.split()
first_position = words.index("Tom")
second_position = words.index("Tom", first_position + 1)
print(second_position)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
fourth_sentence_lower = adwentures_of_tom_sawer_sentences[3].strip().lower()
print(fourth_sentence_lower)

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in adwentures_of_tom_sawer_sentences]
found_place = any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print(found_place)

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
adwentures_of_tom_sawer_sentences = [sentence.strip() for sentence in adwentures_of_tom_sawer_sentences if sentence.strip()]
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print(word_count)
