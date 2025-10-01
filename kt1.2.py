#КТ1.2 Перцев Александр ИТ-6
import random 
from random import *


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_first(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value
    
    def is_empty(self):
        return self.head is None
    
    def get_first(self):
        return self.head.value if self.head else None
    
    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

class QueueIterator:
    def __init__(self, queue):
        self.queue = queue
        self.forward_data = []
        self.backward_data = []
        self._collect_data()
    
    def _collect_data(self):
        current = self.queue.head
        while current:
            self.forward_data.append(current.value)
            current = current.next
        self.backward_data = self.forward_data[::-1]
    
    def display_forward(self):
        print("Очередь в прямом порядке:")
        for value in self.forward_data:
            print(value, end=" ")
        print()
    
    def display_backward(self):
        print("Очередь в обратном порядке:")
        for value in self.backward_data:
            print(value, end=" ")
        print()

def save_to_file(removed_elements, sum_removed, new_first_value, new_first_pointer):
    with open('rez.dat', 'w', encoding='utf-8') as f:
        f.write("Удаленные элементы: " + str(removed_elements) + '\n')
        f.write("Сумма удаленных элементов: " + str(sum_removed)+ '\n')
        f.write("Новый первый элемент: " + str(new_first_value)+ '\n')
        f.write("Указатель на новый первый элемент: " + str(new_first_pointer))

def process_queue(P1, K):
    removed_elements = []
    sum_removed = 0

    for i in range(K):
        if P1.head:
            value = P1.remove_first()
            removed_elements.append(value)
            sum_removed += value
        else:
            break
    
    new_first = P1.head
    new_first_value = new_first.value if new_first else None
    new_first_pointer = id(new_first) if new_first else None

    save_to_file(removed_elements, sum_removed, new_first_value, new_first_pointer)
    
    print(f"Удаленные элементы: {removed_elements}\n")
    print(f"Сумма удаленных элементов: {sum_removed}\n" )
    if new_first:
        print(f"Новый первый элемент: {new_first_value}\n")
        print(f"Указатель на новый первый элемент: {new_first_pointer}\n")
    else:
        print("Очередь пуста")
    
    return removed_elements, sum_removed, new_first_value, new_first_pointer

if __name__ == "__main__":
    queue = Queue()
    K = int(input("Введите число К: "))
    queue.add(K)
    for i in range(1,K):
        queue.add(randint(0,100))
    
    print("Исходная очередь:")
    queue.display()
    K = int(input("Сколько чисел надо удалить? "))
    print(f"Удаляем первые {K} элементов:")
    results = process_queue(queue, K)
    
    print("Очередь после удаления:")
    queue.display()
    
    print("\n" + "="*50)
    iterator = QueueIterator(queue)
    iterator.display_forward()
    iterator.display_backward()
    

    print("\n" + "="*50)
    print("Чтение из файла rez.dat:")
    with open('rez.dat', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)