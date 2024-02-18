#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Написать программу, которая будет находить самое длинное слово в файле.
# В качестве результата программа должна выводить на экран длину
# самого длинного слова и все слова такой длины. Принимайте за значимые
# буквы любые непробельные символы, включая цифры и знаки препинания.


def find_longest_words(file_content):
    words = file_content.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return max_length, longest_words


if __name__ == '__main__':
    with open("file2.txt", "r") as fileptr:
        content = fileptr.read()
        print("Исходный файл: ")
        print(content)
        length, longest_words = find_longest_words(content)
        print(f"Длина самого длинного слова: {length}")
        print(f"Самые длинные слова: {', '.join(longest_words)}")
