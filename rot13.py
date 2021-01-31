alphabet = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
            'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
            'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
            ' ': ' ',
            '!': '!', '@': '@', '#': '#', '$': '$', '%': '%', '&': '&', '^': '^', '*': '*', '(': '(', ')': ')',
            '_': '_', '+': '+', '=': '=', '~': '~',
            '{': '{', '}': '}', ';': ';', ':': ':', '"': '"', '<': '<', '>': '>', '?': '?'}


def main():
    user_input = input('Please enter the string:\n').lower()
    new_list = []
    for item in user_input:
        loc = alphabet.get(item)
        new_list.append(loc)
    print("".join(new_list))


if __name__ == '__main__':
    main()
