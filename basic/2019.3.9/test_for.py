
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]


def list_find(list1, list2):
    for a in list1:
        if a in list2:
            print(str(a), '在列表1和2中')
        else:
            print(str(a), '只在列表1中')


if __name__ == '__main__':
    for a in list1:
        if a in list2:
            print(str(a), '在列表1和2中')
        else:
            print(str(a), '只在列表1中')

