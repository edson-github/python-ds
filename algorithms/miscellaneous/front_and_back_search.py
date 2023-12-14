def front_and_back_search(lst, item):
    '''
    args:
    lst: an unsorted array of integers
    item: data to be found

    return:
    item which is found else False
    '''
    rear=0
    front=len(lst)-1
    u=None
    if rear>front:
        return False
    while rear<=front:
        if item in [lst[rear], lst[front]]:
            u=''
            return True ##item found
        else:
            if item > lst[rear]:
                rear += 1
            elif item < lst[front]:
                front=front-1
    if u is None:
        return False
