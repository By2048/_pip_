import re
import string
from xml.etree.ElementTree import parse

UP = list(string.ascii_uppercase)
DOWN = list(string.ascii_lowercase)
NUM = list(string.digits)


def split_word(item):
    item = list(item)
    result = []
    tmp = ""
    for index in range(len(item)):
        if item[index] in UP + NUM:
            if tmp:
                result.append(tmp)
                tmp = ""
        tmp += item[index]
        if index == len(item) - 1:
            result.append(tmp)
    return " ".join(result)


def test_1():
    with open("_pycharm_keymap_.xml", 'r', encoding='utf-8') as file:
        data = parse(file).getroot()
    for action in data.findall('action'):
        item = action.attrib['id']
        item = item.lstrip('$')
        item = item.replace('.', '')
        item = item.replace(' ', '')
        item = item.replace("ANSI", "Ansi")
        item = split_word(item)
        print(item)


def test_2():
    with open("_pycharm_keymap_.xml", 'r', encoding='utf-8') as file:
        data = parse(file).getroot()
    for action in data.findall('action'):
        item = action.attrib['id']
        item = item.lstrip('$')
        item = item.replace('.', '')
        item = item.replace(' ', '')
        item = re.split('(?=[A-Z])', item)
        print(" ".join(item).strip())


if __name__ == '__main__':
    test_2()
