# Given a five-digit or six-digit natural number. Write a program to reverse the order of its last five digits.
# To test: 65000, 206578


def reverse_digits(number):
    initial_list = list(str(number))
    initial_list.reverse()
    list1 = initial_list[5:]
    list1.reverse()
    list2 = initial_list[:5]
    list3 = list1+list2
    resulting_string = ''.join(list3)
    return int(resulting_string.lstrip('0'))


if __name__ == '__main__':
    number = input('Enter five-digit or six-digit natural number: ')
    result = reverse_digits(number)
    print(result)
