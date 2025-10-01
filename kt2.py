class Node:
    def __init__(self, symbol=None, count=0):
        self.symbol = symbol
        self.count = count    
        self.left = None     
        self.right = None     

def count_letters(text):
    counter = {}
    for letter in text:
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1
    return counter

def make_tree(letter_counts):
    nodes = []
    for letter, count in letter_counts.items():
        nodes.append(Node(letter, count))
    
    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.count)
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        parent = Node(None, left.count + right.count)
        parent.left = left
        parent.right = right
        nodes.append(parent)
    
    return nodes[0] if nodes else None

def make_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    
    if node is None:
        return codes
    
    if node.symbol is not None:
        codes[node.symbol] = current_code if current_code else "0"
    else:
        make_codes(node.left, current_code + "0", codes)
        make_codes(node.right, current_code + "1", codes)
    
    return codes

def print_tree(node, level=0):
    if node is None:
        return
    
    spaces = "  " * level
    
    if node.symbol is not None:
        if node.symbol == ' ':
            print(f"{spaces}ПРОБЕЛ({node.count})")
        else:
            print(f"{spaces}{node.symbol}({node.count})")
    else:
        print(f"{spaces}*({node.count})")
        print_tree(node.left, level + 1)
        print_tree(node.right, level + 1)

def print_single_occurrence_codes(letter_counts, codes):
    single_letters = {}
    for letter, count in letter_counts.items():
        if count == 1:
            single_letters[letter] = count
    
    print("\nКОДЫ ДЛЯ БУКВ, ВСТРЕЧАЮЩИХСЯ ОДИН РАЗ:")
    if not single_letters:
        print("Нет таких букв")
        return
    
    for letter in single_letters:
        if letter == ' ':
            print(f"ПРОБЕЛ -> {codes[letter]}")
        else:
            print(f"'{letter}' -> {codes[letter]}")

def is_russian(text):
    russian_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
    for char in text:
        if char not in russian_letters:
            return False
    return True

if __name__ == "__main__":
    text = input("Введите текст: ").strip()
    
    if not text:
        print("Нужно ввести текст!")
    elif not is_russian(text):
        print("Только русские буквы и пробел!")
    else:
        letter_counts = count_letters(text)
        
        print(f"Нашли {len(letter_counts)} разных букв:")
        for letter, count in sorted(letter_counts.items()):
            if letter == ' ':
                print(f"ПРОБЕЛ: {count} раз")
            else:
                print(f"'{letter}': {count} раз")
        
        root = make_tree(letter_counts)
        codes = make_codes(root)
        
        print("\nДЕРЕВО ХАФФМАНА:")
        print_tree(root)
        
        print_single_occurrence_codes(letter_counts, codes)
        
        encoded = ""
        for letter in text:
            encoded += codes[letter]
        
        print(f"\nЗакодированный текст: {encoded}")

        print(f"Длина закодированного: {len(encoded)} бит")


"""
Введите текст: всем привет
Нашли 9 разных букв:
ПРОБЕЛ: 1 раз
'в': 2 раз
'е': 2 раз
'и': 1 раз
'м': 1 раз
'п': 1 раз
'р': 1 раз
'с': 1 раз
'т': 1 раз

ДЕРЕВО ХАФФМАНА:
*(11)
  *(4)
    *(2)
      ПРОБЕЛ(1)
      п(1)
    *(2)
      р(1)
      и(1)
  *(7)
    *(3)
      т(1)
      в(2)
    *(4)
      е(2)
      *(2)
        с(1)
        м(1)

КОДЫ ДЛЯ БУКВ, ВСТРЕЧАЮЩИХСЯ ОДИН РАЗ:
'с' -> 1110
'м' -> 1111
ПРОБЕЛ -> 000
'п' -> 001
'р' -> 010
'и' -> 011
'т' -> 100
"""
