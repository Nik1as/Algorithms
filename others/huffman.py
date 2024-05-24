import heapq
from collections import defaultdict

def huffman(text):
    h = []

    for c in set(text):
        heapq.heappush(h, (text.count(c), c))

    cipher = defaultdict(lambda : '')

    while len(h) > 1:
        p1, v1  = heapq.heappop(h)
        p2, v2 = heapq.heappop(h)

        for c in v1:
            cipher[c] = '0' + cipher[c]
        for c in v2:
            cipher[c] = '1' + cipher[c]

        p = p1 + p2
        v = v1 + v2

        heapq.heappush(h, (p, v))
    return cipher

def encrypt(cipher, text):
    return ''.join(cipher[c] for c in text)

def decrypt(cipher, text):
    pass

if __name__ == '__main__':
    cipher = huffman('Hello World')
    for k, v in cipher.items():
        print(k, v)
    print(encrypt(cipher, 'Hello World'))
    print(encrypt(cipher, 'lord WolleH'))
