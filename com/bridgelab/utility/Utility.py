import random


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

        tail = times-head

        head_percentage=((head/times)*100)
        tail_percentage=((tail / times) * 100)
        return head_percentage, tail_percentage





utility_obj = Utility()

