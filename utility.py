import random
import string
from array import array

import color as color


class Utility:

    def __init__(self):
        pass

    def get_int(self):
        return int(input(""))

    def get_string(self):
        return input("")

    def replace_str(self, string, replace, user_string):

        return string.replace(replace, user_string)

    def get_probability(self, times):
        head = 0

        for i in range(0, times):
            r = random.randint(0, 1)
            if r == 1:
                head += 1

        tail = times - head

        head_percentage = ((head / times) * 100)
        tail_percentage = ((tail / times) * 100)
        return head_percentage, tail_percentage

    def isleap_year(self, year):
        if len(year) < 4:
            print("enter year having 4 digit ")
            year = utility_obj.get_string()
            utility_obj.isleap_year(year)

        else:
            year = int(year)
            if year % 100 == 0 and year % 400 == 0:
                print(str(year) + " is a Leap year")

            else:
                print(str(year) + " is not a leap year")

    def power(self, limit):
        # store_value=[]
        # count=0
        if 0 > limit or limit > 30:
            print("Enter value greater than equal to zero but less than 31")
            limit = utility_obj.get_int()
            utility_obj.power(limit)

        else:

            for i in range(0, limit + 1):
                value = pow(2, i)
                print(value)

    def get_nth_harmonic_value(self, harmonic_value):
        sum = 0
        for i in range(1, harmonic_value + 1):
            sum += 1 / i
        print(sum)

    def get_prime_factors(self):
        list = []
        count = 0
        print("Enter Number to find Prime Factors =>")
        num = utility_obj.get_int()
        Range = num
        is_prime = True
        for i in range(Range):
            if i == 0 or i == 1:
                continue
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:

                while num % i == 0:
                    # print(i)
                    list.insert(count, i)
                    count += 1
                    num = num / i

        return list

    def get_gambling_result(self, stake, goal, times):
        cash = stake
        win_count = 0
        lose_count = 0
        i = 0
        while (cash != 0 or cash == goal) and i < times:
            random_number = random.randint(0, 1)
            i += 1
            if random_number == 1:
                cash += 1
                win_count += 1

            elif random_number == 0:
                cash -= 1
                lose_count += 1

            if cash == goal:
                break

        win_percent = (win_count / (win_count + lose_count)) * 100
        lose_percent = (lose_count / (win_count + lose_count)) * 100
        return win_count, win_percent, lose_percent

    def coupan_generator(self, no_of_coupans):
        store_coupans = []
        random_number_count = 0
        while len(store_coupans) <= no_of_coupans:
            random_number = random.randint(1, 50)
            random_number_count += 1

            if store_coupans.__contains__(random_number) == False:
                store_coupans.append(random_number)

        return random_number_count, store_coupans

    def get_2d__input(self, row, column):

        two_d_array = [[0 for j in range(column)] for i in range(row)]

        for i in range(0, row):
            for j in range(0, column):
                two_d_array[i][j] = Utility().get_int()

        return two_d_array

    def find_triplet(self, store_values):
        size = len(store_values)

        for i in range(0, size - 2):

            for j in range(i + 1, size - 1):

                for k in range(j + 1, size):

                    if (store_values[i] + store_values[j] + store_values[k]) == 0:
                        print(store_values[i], end=" ")
                        print(store_values[j], end=" ")
                        print(store_values[k], end=" ")
                        print("")

    def get_prime(self):
        list = []
        is_prime = True
        for i in range(1001):
            if i == 0 or i == 1:
                continue
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
            if is_prime:
                list.append(i)
        return list

    def get_palindrome_prime(self):
        store_prime = Utility().get_prime()
        s = ''
        store_palindrome_prime = []
        for i in store_prime:
            string = ''
            string = str(i)
            string1 = string
            count = -1
            reverse_string1 = ''

            for j in range(0, len(string1)):
                reverse_string1 += string1[count]
                count = count - 1

            string1 = ''
            if reverse_string1 == string:
                store_palindrome_prime.append(string)

        return store_palindrome_prime

    def anagram_detection(self, first_string, second_string):
        first_string
        second_string = second_string
        first_string_list = []
        second_string_list = []

        lower_string = first_string.lower()
        first_string = lower_string

        lower_string = ''
        lower_string = second_string.lower()
        second_string = lower_string

        remove_space = ''
        for i in range(0, len(first_string)):
            if first_string[i] == ' ':
                continue

            remove_space += first_string[i]

        first_string = remove_space

        remove_space = ''
        for i in range(0, len(second_string)):
            if second_string[i] == ' ':
                continue
            remove_space += second_string[i]

        second_string = remove_space

        for i in first_string:
            first_string_list.append(i)

        for i in range(0, len(first_string_list) - 1):

            for j in range(i + 1, len(first_string_list)):
                temp = ''
                if first_string_list[i] > first_string_list[j]:
                    temp = first_string_list[i]
                    first_string_list[i] = first_string_list[j]
                    first_string_list[j] = temp

        first_string = ''
        for i in range(0, len(first_string_list)):
            first_string = first_string + first_string_list[i]

        for i in second_string:
            second_string_list.append(i)

        for i in range(0, len(second_string_list) - 1):

            for j in range(i + 1, len(second_string_list)):
                temp = ''
                if second_string_list[i] > second_string_list[j]:
                    temp = second_string_list[i]
                    second_string_list[i] = second_string_list[j]
                    second_string_list[j] = temp

        second_string = ''
        for i in range(0, len(second_string_list)):
            second_string = second_string + second_string_list[i]

        s3 = ''
        if first_string == second_string:
            print("Both Strings are Anagram of each other")


        else:
            print('Both Strings are not Anagram of each other')

    def get_anagram_prime(self):
        store_prime = Utility().get_prime()
        first_string_list = []
        second_string_list = []
        count = 0
        for each_index in range(0, len(store_prime) - 1):
            first_string_list = []
            s1 = str(store_prime[each_index])
            first_string = s1
            count = 0
            for i in first_string:
                first_string_list.append(i)

            for i in range(0, len(first_string_list) - 1):

                for j in range(i + 1, len(first_string_list)):
                    temp = ''
                    if first_string_list[i] > first_string_list[j]:
                        temp = first_string_list[i]
                        first_string_list[i] = first_string_list[j]
                        first_string_list[j] = temp

            first_string = ''
            for i in range(0, len(first_string_list)):
                first_string = first_string + first_string_list[i]

            for next_index in range(each_index + 1, len(store_prime)):

                second_string = str(store_prime[next_index])

                for i in second_string:
                    second_string_list.append(i)

                for i in range(0, len(second_string_list) - 1):

                    for j in range(i + 1, len(second_string_list)):
                        temp = ''
                        if second_string_list[i] > second_string_list[j]:
                            temp = second_string_list[i]
                            second_string_list[i] = second_string_list[j]
                            second_string_list[j] = temp

                second_string = ''
                for i in range(0, len(second_string_list)):
                    second_string = second_string + second_string_list[i]

                if first_string == second_string:
                    print(store_prime[next_index])
                    count += 1

                second_string_list = []

            if count >= 1:
                print(store_prime[each_index])

    def number_guess_game(self, lowerlimit, upperlimit):

        while lowerlimit <= upperlimit:
            if lowerlimit == upperlimit:
                print('Your Number is => ' + str(lowerlimit))
                print("Intermediary numbers is " + str(lowerlimit - 1) + " and " + str(lowerlimit + 1))
                return

            mid_value = (lowerlimit + upperlimit) // 2
            print('1. ' + str(lowerlimit) + ' - ' + str(mid_value))
            print('2. ' + str(mid_value + 1) + ' - ' + str(upperlimit))
            choice = Utility().get_int()
            if choice == 1:
                upperlimit = mid_value

            if choice == 2:
                lowerlimit = mid_value + 1


utility_obj = Utility()


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class OrderedList:
    head = None
    list = [10, 1, 2, 7, 5, 3]

    def __init__(self):
        pass

    def add(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node

        else:
            traverse = self.head
            if self.head.data > node.data:
                self.head = node
                node.next = traverse

            if self.head.data < node.data:
                temp = self.head
                while traverse.next != None:
                    if traverse.data < node.data:
                        temp = traverse
                    traverse = traverse.next

                if traverse.data < node.data:
                    temp = traverse

                temp1 = temp.next
                temp.next = node
                node.next = temp1

    def show(self):
        traverse = self.head
        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next
        print(traverse.data)


# ordered_list = OrderedList()
# ordered_list.add(10)
# ordered_list.add(1)
# ordered_list.add(2)
# ordered_list.add(3)
# ordered_list.add(4)
# ordered_list.add(11)
# ordered_list.add(5)
# ordered_list.add(-1)
# ordered_list.add(-2)
# ordered_list.add(6)
# ordered_list.show()
#

class Queue:
    front = None
    rear = None

    def __init__(self):
        pass

    def enqueue(self, data):

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = self.rear.next

    def show(self):

        if self.front == None:
            print("Queue  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):

        temp = self.front
        self.front = self.front.next
        return temp.data

    def is_empty(self):

        if self.front == None:
            return True
        else:
            return False

    def size(self):

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size


queue = Queue()


# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)
#
# queue.dequeue()
# queue.dequeue()
#
# queue.show()
# print(queue.is_empty())
# print(queue.size())

class Deque:
    front = None
    rear = None

    def __init__(self):
        pass

    def add_front(self, data):
        node = Node(data)
        if self.front == None and self.rear == None:
            self.front = node
            self.rear = node

        else:
            node.next = self.front
            self.front = node

    def add_rear(self, data):

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = node

    def show(self):

        if self.front == None:
            print("Queue  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def remove_front(self):

        temp = self.front
        self.front = self.front.next
        return temp.data

    def remove_rear(self):

        traverse = self.front
        if self.rear == self.front:
            self.rear = None
            self.front = None
            return traverse.data

        while traverse.next != self.rear:
            traverse = traverse.next

        rear_value = self.rear
        self.rear = traverse
        traverse.next = None
        return rear_value.data

    def is_empty(self):

        if self.front == None:
            return True
        else:
            return False

    def size(self):

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size


deque = Deque()


# deque.add_rear(40)

# deque.add_rear(60)
# deque.add_rear(70)

# deque.remove_front()
# deque.remove_front()

# print( deque.remove_rear())
# print( deque.remove_rear())


# deque.remove_rear()
# deque.remove_rear()

# print(deque.is_empty())
# print(deque.size())

# deque.show()

def palindrome_checker():
    print("Enter String to Check for Palindrome")
    string = Utility().get_string()

    for i in string:
        deque.add_rear(i)
    reverse_string = ''
    for i in range(0, deque.size()):
        reverse_string += str(deque.remove_rear())

    if string == reverse_string:
        return True
    else:
        return False


# print(palindrome_checker())

def prime_number_2d_array():

    prime_list = utility_obj.get_prime()
    row=8
    column=21
    # list_2d=[[].insert(0,22),[].append(23),[].append(24),[].append(25),[].append(26)]
    list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    two_d_array = [[0 for j in range(column)] for i in range(row)]

    # list_2d.insert([0][1],22)

    k=0
    for i in range(row):


        for j in range(column):

            if k<len(prime_list):
                two_d_array[i][j] =prime_list[k]
                k+=1


    for i in range(row):

        for j in range(column):
            print(two_d_array[i][j],end=" ")

        print()
# prime_number_2d_array()

#
# class HashTable:
#     def __init__(self):
#         self.size = 11
#         self.slots = [None] * self.size
#         self.data = [None] * self.size
#
#     def put(self,key,data):
#       hashvalue = self.hashfunction(key,len(self.slots))
#
#       if self.slots[hashvalue] == None:
#         self.slots[hashvalue] = key
#         self.data[hashvalue] = data
#       else:
#         if self.slots[hashvalue] == key:
#           self.data[hashvalue] = data  #replace
#         else:
#           nextslot = self.rehash(hashvalue,len(self.slots))
#           while self.slots[nextslot] != None and \
#                           self.slots[nextslot] != key:
#             nextslot = self.rehash(nextslot,len(self.slots))
#
#           if self.slots[nextslot] == None:
#             self.slots[nextslot]=key
#             self.data[nextslot]=data
#           else:
#             self.data[nextslot] = data #replace
#
#     def hashfunction(self,key,size):
#          return key%size
#
#     def rehash(self,oldhash,size):
#         return (oldhash+1)%size
#
#     def get(self,key):
#       startslot = self.hashfunction(key,len(self.slots))
#
#       data = None
#       stop = False
#       found = False
#       position = startslot
#       while self.slots[position] != None and  \
#                            not found and not stop:
#          if self.slots[position] == key:
#            found = True
#            data = self.data[position]
#          else:
#            position=self.rehash(position,len(self.slots))
#            if position == startslot:
#                stop = True
#       return data
#
#     def __getitem__(self,key):
#         return self.get(key)
#
#     def __setitem__(self,key,data):
#         self.put(key,data)
#
# H=HashTable()
# H[54]="cat"
# H[26]="dog"
# H[93]="lion"
# H[17]="tiger"
# H[77]="bird"
# H[31]="cow"
# H[44]="goat"
# H[55]="pig"
# H[20]="chicken"
# print(H.slots)
# print(H.data)
#
# print(H[20])
#
# print(H[17])
# H[20]='duck'
# print(H[20])
# print(H[99])
#
# # 2nd hashmap implementation---------------
#
#
# # Hash Map
#
# class HashMap:
#     def __init__(self):
#         self.size = 6
#         self.map = [None] * self.size
#
#     def _get_hash(self, key):
#         hash = 0
#         for char in str(key):
#             hash += ord(char)
#         return hash % self.size
#
#     def add(self, key, value):
#         key_hash = self._get_hash(key)
#         key_value = [key, value]
#
#         if self.map[key_hash] is None:
#             self.map[key_hash] = list([key_value])
#             return True
#         else:
#             for pair in self.map[key_hash]:
#                 if pair[0] == key:
#                     pair[1] = value
#                     return True
#             self.map[key_hash].append(key_value)
#             return True
#
#     def get(self, key):
#         key_hash = self._get_hash(key)
#         if self.map[key_hash] is not None:
#             for pair in self.map[key_hash]:
#                 if pair[0] == key:
#                     return pair[1]
#         return None
#
#     def delete(self, key):
#         key_hash = self._get_hash(key)
#
#         if self.map[key_hash] is None:
#             return False
#         for i in range(0, len(self.map[key_hash])):
#             if self.map[key_hash][i][0] == key:
#                 self.map[key_hash].pop(i)
#                 return True
#         return False
#
#     def print(self):
#         print('---PHONEBOOK----')
#         for item in self.map:
#             if item is not None:
#                 print(str(item))
#
#
# h = HashMap()
# h.add('Bob', '567-8888')
# h.add('Ming', '293-6753')
# h.add('Ming', '333-8233')
# h.add('Ankit', '293-8625')
# h.add('Aditya', '852-6551')
# h.add('Alicia', '632-4123')
# h.add('Mike', '567-2188')
# h.add('Aditya', '777-8888')
# h.print()
# h.delete('Bob')
# h.print()
# print('Ming: ' + h.get('Ming'))


class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    head = None

    def __init__(self):
        pass

    def append(self, data):

        node = Node(data)

        if self.head == None:

            self.head = node

        else:

            traverse = self.head

            while traverse.next != None:
                traverse = traverse.next

            traverse.next = node

    def show(self):

        traverse = self.head

        if self.head == None:
            # print("Linked List  is empty")
            return

        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next

        print(traverse.data)

    def is_empty(self):

        if self.head == None:
            return True
        else:
            return False

    def search_item(self, data):

        traverse = self.head
        if self.head == None:
            return False

        while traverse.next != None:

            if traverse.data == data:
                return True
            traverse = traverse.next
        if traverse.data == data:
            return True
        else:
            return False

    def size(self):
        traverse = self.head
        count = 0
        while traverse.next != None:
            traverse = traverse.next
            count += 1
        return count + 1

    def index(self, data):

        traverse = self.head
        count = 0
        while traverse.next != None:

            if traverse.data == data:
                return count
            traverse = traverse.next
            count += 1

        if traverse.data == data:
            return count

    def insert(self, position, data):

        node = Node(data)
        traverse = self.head

        for i in range(0, position - 1):
            traverse = traverse.next
        temp = traverse.next
        traverse.next = node
        node.next = temp

    def pop(self):

        traverse = self.head

        if self.head == None:
            return -1

        if self.head.next == None:
            self.head = None
            print(traverse.data)

        while traverse.next is not None:

            t1 = traverse.next

            if t1.next is None:
                traverse.next = None
                return t1.data
            traverse = traverse.next

    def pop_position(self, position):

        traverse = self.head
        temp = self.head

        if position == 0:
            self.head = traverse.next
            return traverse.data

        for i in range(0, position - 1):
            traverse = traverse.next

        temp = traverse
        traverse = traverse.next
        temp.next = traverse.next
        return traverse.data

    def remove(self, data):

        traverse = self.head
        temp = self.head
        if self.head==None:
            return None

        if traverse.data == data:
            self.head = traverse.next
            return traverse.data

        while traverse.next != None:

            temp = traverse.next
            if temp.data == data:
                traverse.next = temp.next
                return temp.data

            traverse = traverse.next

    def display_content(self):
        list=[]
        traverse = self.head

        if self.head == None:
            # print("Linked List  is empty")
            return

        while traverse.next != None:
            list.append(traverse.data)
            traverse = traverse.next

        list.append(traverse.data)
        return list




class HashTable:

    def __init__(self):
        pass

    objects_list = list()
    for i in range(11):
        objects_list.append(LinkedList())

    def hash_function(self, key):
        index = key % len(self.objects_list)
        return index

    def insert(self):

        # elements = [77, 26, 22, 33, 37,38,39,44]
        # file = open("HashTable File", "w+")
        # for i in elements:
        #     file.writelines(str(i) + ' ')
        # file.close()

        file = open("../util/HashTable File", "r")
        elements = file.readlines()
        string = elements[0]

        string_list = string.split()
        # print(string_list)
        elements = []
        for i in range(0, len(string_list)):
            to_integer = int(string_list[i])
            elements.append(to_integer)
        print(elements)
        for i in range(len(elements)):
            index = self.hash_function(elements[i])
            self.objects_list[index].append(elements[i])
            # self.objects_list[index].show()

    def search(self, data):
        index = self.hash_function(data)
        return self.objects_list[index].search_item(data)

    def file_update(self, data):
        result = self.search(data)

        if result == True:
            index = self.hash_function(data)
            self.objects_list[index].remove(data)
            self.dispaly_content_hashtable()

        if result == False:
            index = self.hash_function(data)
            self.objects_list[index].append(data)
            self.dispaly_content_hashtable()



    def dispaly_content_hashtable(self):


        file = open("../util/HashTable File", "r+")
        file.truncate(0)
        file.close()
        for i in range(0,len(self.objects_list)):

            if self.objects_list[i].display_content()!=None:
                lines=[]
                lines=self.objects_list[i].display_content()
                file = open("../util/HashTable File", "a+")
                for j in lines:
                    file.write(str(j)+' ')


        file.close()

        file=open("../util/HashTable File","r")
        for i in file:
            print(i)

#
h = HashTable()
h.insert()
print(h.search(26))
h.file_update(26)
# # h.dispaly_content_hashtable()