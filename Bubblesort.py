#Python program
def bubblesort(List):

    for i in range(len(List)):
        for j in range(len(List) - 1, i, -1):
            if List[j] < List[j - 1]:
                List[j], List[j - 1] = List[j -1], List[j]
    return List

if __name__ == '__main__':
    List = [2, 4, 3, 12, 10]
    print('Sorted List:', bubblesort(List))
