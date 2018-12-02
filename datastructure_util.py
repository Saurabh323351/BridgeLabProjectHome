from com.bridgelab.util.utility import Utility


class Node:
    """
    This class is used to create Node
    """

    def __init__(self, data, next=None):
        """
        This is the constructor of Node class .

        :param data:user given value will be stored in this variable
        :param next: this variable keeps the address of next node
        """
        self.data = data
        self.next = next


class LinkedList:
    """
    This class is used to create LinkedList
    """
    head = None

    def __init__(self):
        """
        This is constructor of LinkedList class
        """
        pass

    def append(self, data):
        """
        This method is used to append data given by user at the end of the LinkedList

        :param data:this value will be provided by user to append at the end of list

        :return: this method won't return anything
        """

        node = Node(data)

        if self.head == None:

            self.head = node

        else:

            traverse = self.head

            while traverse.next != None:
                traverse = traverse.next

            traverse.next = node

    def show(self):
        """
        This method is used to display content of each node in the LinkedList

        :return:nothing
        """

        traverse = self.head

        if self.head == None:
            print("Linked List  is empty")
            return

        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next

        print(traverse.data)

    def is_empty(self):
        """
        This is ued to know whether LinkedList is empty or not

        :return:this will return True if LinkedList is empty else return False
        """

        if self.head == None:
            return True
        else:
            return False

    def search_item(self, data):
        """
        This method is used to search data given by user.

        :param data:this is the data that user want to search in the list
        :return: this will return true if data is found else return False
        """

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
        """
        This method is used to calculate size of LinkedList.

        :return:this will return the size of L;inkedList
        """
        traverse = self.head
        count = 0
        while traverse.next != None:
            traverse = traverse.next
            count += 1
        return count + 1

    def index(self, data):
        """
        This method is used to find index of paricular data entered by user

        :param data:data given by user
        :return:this will return  index of data
        """

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
        """
        This method is used to insert data at specific position given by user.

        :param position:position will be given by user.
                    at which position user weants to insert data
        :param data:which data user wants to insert
        :return:nothing
        """

        node = Node(data)
        traverse = self.head

        for i in range(0, position - 1):
            traverse = traverse.next
        temp = traverse.next
        traverse.next = node
        node.next = temp

    def pop(self):
        """
        This method is used to delete last data from the Linked .

        :return:this will return the data that will be deleted
        """

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
        """
        This method is used to delete data at particular position.

        position will be specified by user

        :param position:given by user
        :return: this will return the data that will be popped
        """

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
        """
        This method is used to remove data from the Linked list specified by the user.

        :param data:specified by user which data to be removed
        :return:this will return None ,if LinkedList is Empty
        """

        traverse = self.head
        temp = self.head
        if self.head == None:
            return None

        if traverse.data == data:
            self.head = traverse.next
            return

        while traverse.next != None:

            temp = traverse.next
            if temp.data == data:
                traverse.next = temp.next
                return

            traverse = traverse.next

    def display_content(self):
        """
        This method is used to display content of Linked list.

        this method return each data in each node in LinkedList
         and this method i created so that i can use in HashTable to display
         each data stored in HashTable data structure

        :return:this will return each data in LinkedList
        """
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


class OrderedList:
    """
    This is used to create OrderedList.
    """
    head = None

    def __init__(self):
        """
        This is the constructor of OrderedList class
        """
        pass

    def add(self, data):
        """
        This method is used to put data in OrderedList in increasing order.

        :param data: dat will be provided by user
        :return: nothing
        """
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

    def remove(self, data):
        """
        This method is used to remove data from the OrderedList specified by the user.

        :param data:specified by user which data to be removed
        :return:nothing
        """

        traverse = self.head
        temp = self.head
        if traverse.data == data:
            self.head = traverse.next
            return

        while traverse.next != None:

            temp = traverse.next
            if temp.data == data:
                traverse.next = temp.next
                return

            traverse = traverse.next

    def search_item(self, data):
        """
        This method is used to search data given by user.

        :param data:this is the data that user want to search in the list
        :return: this will return true if data is found else return False
        """

        traverse = self.head
        while traverse.next != None:

            if traverse.data == data:
                return True
            traverse = traverse.next
        if traverse.data == data:
            return True
        else:
            return False

    def is_empty(self):
        """
        This is used to know whether OrderedList is empty or not

        :return:this will return True if OrderedList is empty else return False
        """

        if self.head == None:
            return True
        else:
            return False

    def size(self):
        """
        This method is used to calculate size of OrderedList.

        :return:this will return the size of L;inkedList
        """
        traverse = self.head
        count = 1
        while traverse.next != None:
            traverse = traverse.next
            count += 1
        return count

    def index(self, data):
        """
       This method is used to insert data at specific position given by user.

       :param position:position will be given by user.
                   at which position user weants to insert data
       :param data:which data user wants to insert
       :return:nothing
       """

        traverse = self.head
        count = 0
        while traverse.next != None:

            if traverse.data == data:
                return count
            traverse = traverse.next
            count += 1

        if traverse.data == data:
            return count

    def pop(self):
        """
        This method is used to delete last data from the Linked .

         :return:this will return the data that will be deleted
        """

        traverse = self.head

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:
                traverse.next = None
                return t1.data
            traverse = traverse.next

    def pop_position(self, position):
        """
        This method is used to delete data at particular position.

        position will be specified by user

        :param position:given by user
        :return: this will return the data that will be popped
        """

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

    def show(self):
        """
        This method is used to display content of each node in OrderedList.

        :return: nothing
        """
        traverse = self.head
        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next
        print(traverse.data)


ordered_list = OrderedList()


class Stack:
    """
    This is the Stack class to create Stack.
    """
    top = 0
    head = None

    def __init__(self):
        """
        This is the constructor of Stack class.
        """
        pass

    def push(self, data):
        """
        This method is used to insert data in stack.

        :param data:data will given by user
        :return: nothing
        """

        node = Node(data)

        if self.head == None:

            self.head = node
        else:

            traverse = self.head

            while traverse.next != None:
                traverse = traverse.next

            traverse.next = node

    def size(self):
        """
        This method is used to find the size of Stack.

        :return:this will return the size of stack
        """
        traverse = self.head

        if self.head == None:
            return 0
        size = 1
        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size

    def show(self):
        """
        This method is used to display content of stack.

        :return: nothing
        """
        traverse = self.head

        if self.top <= -1:
            print(" Stack Underflow")
            return
        if traverse == None:
            print("Stack is empty")
            return

        while traverse.next != None:
            print(traverse.data)
            traverse = traverse.next
        print(traverse.data)

    def pop(self):
        """
        This method is used to delete last data which is inserted into the stack.

        actually stack follow the Last in First Out order Principle to pop the data fromthe stack
        :return: this will return the data that will be removed
        """

        traverse = self.head

        if self.head == None:
            return -1

        if self.head.next == None:
            self.head = None

            return traverse.data

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:
                traverse.next = None

                return t1.data
            traverse = traverse.next

    def peek(self):
        """
        This method is used to return the last inserted item in the stack.

        :return: return the last item inserted in the stacck
        """
        traverse = self.head

        if self.head == None:
            return "empty stack"
        self.top = self.size() - 1
        for i in range(0, self.top):
            traverse = traverse.next

        return traverse.data

    def is_empty(self):
        """
        This method is used to know wheter stack is empty or not.

        :return:this will return true if stack is empty else return False
        """

        if self.size() == 0:
            return True
        else:
            return False


stack = Stack()
stack1=Stack()
string = "{(([{}]))}"

for i in string:
    # print(i)
    if i == '(' or i == '[' or i == '{':
        stack.push(i)

    if ((stack.peek() == '(' and i == ')') or (stack.peek() == '[' and i == ']') or (
            stack.peek() == '{' and i == '}')) and stack.size() > 0:
        stack.pop()
        continue

    if i == ')' or i == ']' or i == '}':
        stack.push(i)


#
# if stack.size()==0:
#     print("Balanced Parenthesis ")
# else:
#     print("Parenthesis is not Balanced ")
# print(stack.size())
# stack.show()


class Queue:
    """
    This Queue class is used to create Queue.
    """
    front = None
    rear = None

    def __init__(self):
        """
        This is the constructor of Queue class .
        """
        pass

    def enqueue(self, data):
        """
        This method is used to insert data in the Queue .

        data will be given by user which data to be inserted ,
        queue follows First in First Out Principle.

        :param data: data wiill be given by user
        :return: nothing
        """

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = self.rear.next

    def show(self):
        """
        This method is used to display content of queue .

        :return: nothing
        """

        if self.front == None:
            print("Linked List  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):
        """
        This method is used to delete data from the Queue.

        data will deleted according to FIFO principle

        :return: this will return the data that will be removed from the Queue
        """

        temp = self.front
        self.front = self.front.next
        return temp.data

    def is_empty(self):
        """
       This method is used to know whether Queue is empty or not.

       :return:this will return true if Queue is empty else return False
       """
        if self.front == None:
            return True
        else:
            return False

    def size(self):
        """
        This method is used to display content of queue.

        :return: nothing
        """

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size


queue = Queue()


class Deque:
    # front = None
    # rear = None

    def __init__(self, front=None, rear=None):
        """
        This is the constructor of Deque class.

        :param front: this will always point to first node in the deque
        :param rear: this will always point to last node in the Deque
        """
        self.front = front
        self.rear = rear

    def add_front(self, data):
        """
        This method is used to insert data at front in Deque.

        :param data: data will be given by user that which data to be inserted in Deque
        :return: nothing
        """
        node = Node(data)
        if self.front == None and self.rear == None:
            self.front = node
            self.rear = node

        else:
            node.next = self.front
            self.front = node

    def add_rear(self, data):
        """
        This method is used to insert data at last in Deque.

        :param data:data will be given by user
        :return: nothing
        """

        node = Node(data)

        if self.front == None and self.rear == None:

            self.front = node
            self.rear = node

        else:

            self.rear.next = node
            self.rear = node

    def show(self):
        """
        This method is used to display content of deque.

        :return:nothing
        """

        if self.front == None:
            print("Queue  is empty")
            return

        while self.front.next != None:
            print(self.front.data)
            self.front = self.front.next

        print(self.front.data)

    def remove_front(self):
        """
        This is used to remove data which is at front in deque.

        :return:this will return the data which will be removed from the deque
        """

        if self.front.next is None:
            temp = self.front
            self.front = None
            return temp.data

        temp = self.front
        self.front = self.front.next
        return temp.data

    def remove_rear(self):
        """
       This is used to remove data which is at rear position in deque.

       :return:this will return the data which will be removed from the deque
       """

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
        """
        This method is used to know whether Deque is empty or not.

        :return:this will return True if Deque is empty or else  return False.
        """

        if self.front == None:
            return True
        else:
            return False

    def size(self):
        """
        This method is used to calculate size of Deque
        :return: this will return size of Deque
        """

        size = 1
        traverse = self.front
        if self.front == None:
            return 0

        while traverse.next != None:
            traverse = traverse.next
            size += 1
        return size


deque = Deque()


class BinaryTreeNode:

    def __init__(self):
        pass

    def count_binary_search_tree(self, test_cases):
        """
        This method is used to calculate possible number of binary search tree in given number of node.

        :param test_cases:No of node given by user
        :return: this will return the number of binary search tree possible
        """

        for i in test_cases:
            fact1 = 1
            for j in range(1, (i * 2) + 1):
                fact1 = fact1 * j

            fact2 = 1
            num = i + 1
            for l in range(1, num + 1):
                fact2 = fact2 * l

            nfact = 1

            for k in range(1, i + 1):
                nfact = nfact * k

            number_of_bst = (fact1 // (fact2 * nfact)) % 100000007
            return number_of_bst


utility_obj = Utility()


class Logic:
    """
    This class Logic is used to write logics of various programs.
    """

    def __init__(self):
        pass

    def anagram_stack(self):
        """
        This method is used to print prime anagram in reverse order.
        :return: nothing
        """
        for i in utility_obj.get_anagram_prime():
            stack.push(i)

        for i in range(0, stack.size()):
            print(stack.pop())

    def anagram_queue(self):
        """
        This method is used to print prime anagram using queue.
        :return:
        """

        for i in utility_obj.get_anagram_prime():
            queue.enqueue(i)

        for i in range(0, queue.size()):
            print(queue.dequeue())

    def prime_number_2d_array(self):
        """
        This method is used to store prime number in matrix or 2d array
        and print in proper order.
        :return: nothing
        """

        prime_list = utility_obj.get_prime()
        row = 10
        column = 25
        limit = 100

        two_d_array = [[0 for j in range(column)] for i in range(row)]

        k = 0
        for i in range(row):

            for j in range(column):

                if k < len(prime_list):
                    if prime_list[k] <= limit:
                        two_d_array[i][j] = prime_list[k]
                        k += 1

            limit += 100

        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")

            print()

    def anagram_2d_array(self):
        """
        This method is used to store prime anagram and prime number which are not anagram in matrix or 2d array.
        and print them accordingly

        :return:nothing
        """
        prime_list = utility_obj.get_prime()
        anagram_list = utility_obj.get_anagram_prime()
        not_anagram = []
        row = 10
        column = 25

        two_d_array = [[0 for j in range(column)] for i in range(row)]
        k = 0
        index = 0
        for i in prime_list:
            if anagram_list.__contains__(i) is not True:
                not_anagram.append(i)

        for i in range(row):

            for j in range(column):

                if k < len(anagram_list):
                    two_d_array[i][j] = anagram_list[k]
                    k += 1

                if k >= len(anagram_list) and index < len(not_anagram):
                    two_d_array[i][j] = not_anagram[index]
                    k += 1
                    index += 1
        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")

            print()

    def calender(self, month, year):
        """
        This method is used to print Calender of given month and year.

        :param month: month given by user
        :param year: year given by user
        :return: nothing
        """

        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility_obj.isleap_year(str(year)):
            days[1] = 29
        row = 6
        column = 7
        two_d_array = [[0 for j in range(column)] for i in range(row)]

        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:
                        two_d_array[i][j] = ' '
                        continue

                    two_d_array[i][j] = values
                    values += 1

        for i in range(row):

            for j in range(column):
                if two_d_array[i][j] != 0:
                    x = two_d_array[i][j]
                    x1 = str(x).ljust(2)
                    print(x1, end=" ")

            print()

    def calender_queue(self, month, year):

        """
               This method is used to print calender of given month and year.

               In this method calender is created using queue
               :param month:month given ser
               :param year: year given by year
               :return: nothing
               """
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility_obj.isleap_year(str(year)):
            days[1] = 29
        row = 6
        column = 7

        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:
                        queue.enqueue(' ')
                        continue

                    queue.enqueue(values)
                    values += 1

        for i in range(row):

            for j in range(column):
                if queue.size() > 0:
                    x = queue.dequeue()
                    x1 = str(x).ljust(2)
                    print(x1, end=" ")

            print()

    def calender_stack(self, month, year):
        """
       This method is used to print calender of given month and year.

       In this method calender is created using stack
       :param month:month given ser
       :param year: year given by year
       :return: nothing
       """
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility_obj.isleap_year(str(year)):
            days[1] = 29
        row = 6
        column = 7

        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:
                        stack.push(' ')
                        continue

                    stack.push(values)
                    values += 1

        for i in range(stack.size()):
            stack_element = stack.pop()
            stack1.push(stack_element)

        for i in range(row):

            for j in range(column):
                if stack1.size() > 0:
                    x = stack1.pop()
                    x1 = str(x).ljust(2)
                    print(x1, end=" ")

            print()


width = 4
t1 = (width,) * 5
t2 = (4, 4, 4, 4, 4)


# print(t1)

# node1=LinkedList()
#
# node2=LinkedList()
# node3=LinkedList()
#
# node4=LinkedList()
#
# node5=LinkedList()
#
# node6=LinkedList()
#
# node7=LinkedList()
#
# node8=LinkedList()
#
# node9=LinkedList()
#
# node10=LinkedList()
#
# node11=LinkedList()

#
# for i in range(11):
#     objects_list.append(LinkedList())
#


#
# objects_list[0].append(10)

# objects_list[1].append(20)
# objects_list[10].append(30)
# objects_list[4].append(40)
# objects_list[4].append(50)
# objects_list[1].show()
# print(objects_list[1].index(20))
#
# objects_list[0].append(10)
# objects_list[0].show()
# objects_list[1].append(20)
# objects_list[1].show()
#
# objects_list[6].append(5555)
# objects_list[6].append(6666)
# objects_list[6].append("hi bro")
# print(objects_list[5].show())
# logic_obj = Logic()
# print(len(objects_list))
#


class HashTable:
    """
    This HashTable class is used to create hashtable data structure.
    """

    def __init__(self):
        pass

    # creating list to store 11 objects of LinkedList class
    objects_list = list()
    for i in range(11):
        """
        creating 11 objects of LinkedList class and storing it in list 
        that is in objects_list to make HashTable data structure
        """
        objects_list.append(LinkedList())

    def hash_function(self, key):
        """
        This method is used to convert users key or data into index.

        this index is used to store user data in hashtable on index which is obtained  by that particular
        data from hash_function

        :param key:data given by user as a key
        :return: this will return index for that data to store in hashtable
        """
        index = key % len(self.objects_list)
        return index

    def insert(self):
        """
        This method is used to read data from file and convert each data into
        integer format from string format.
        :return: nothing
        """

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


    def search(self, data):
        """
        This method is used to search data which is given by user in hashtable data structure.

        :param data:data will be given bu user
        :return: this will return true if data is found else return false
        """
        index = self.hash_function(data)
        return self.objects_list[index].search_item(data)

    def file_update(self, data):
        """
        This method is used to update file after any operation happened in hashtable
        data strucure.

        :param data:this is the data that is to be removed or added to the file according to search result
        :return: nothing
        """
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
        """
        This method is used to display content of HashTable data structure.
        :return:nothing
        """

        file = open("../util/HashTable File", "r+")
        file.truncate(0)
        file.close()
        for i in range(0, len(self.objects_list)):

            if self.objects_list[i].display_content() != None:
                lines = []
                lines = self.objects_list[i].display_content()
                file = open("../util/HashTable File", "a+")
                for j in lines:
                    file.write(str(j) + ' ')

        file.close()

        file = open("../util/HashTable File", "r")
        for i in file:
            print(i)

#
h = HashTable()
h.insert()
print(h.search(26))
h.file_update(26)
