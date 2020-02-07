
# Закодируйте любую строку по алгоритму Хаффмана.

import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left","right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(namedtuple("Leaf",["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def hufmann_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, count1, left = heapq.heappop(h)
        freq2, count2, right = heapq.heappop(h)

        heapq.heappush(h, (freq1 + freq2,  count, Node(left, right)))
        count +=1
    code = {}

    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def main():
    s = input('Введите строку для кодирования: ')
    code = hufmann_encode(s)
    encoded = "".join(code[ch] for ch in s)

    #print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))

    print(encoded)

main()
