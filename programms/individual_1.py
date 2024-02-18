#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант №5. Написать программу, которая считывает текст из файла
# и выводит его на экран, меняя местами каждые два соседних слова.


def swap(text):
    words = text.split()
    for i in range(0, len(words)-1, 2):
        words[i], words[i+1] = words[i+1], words[i]
    return ' '.join(words)


if __name__ == '__main__':
    with open("file2.txt", "r") as fileptr:
        content = fileptr.read()
        print("Исходный файл: ")
        print(content)

        swapped_text = swap(content)
        print("\nТекст с поменяными соседними словами:")
        print(swapped_text)
