def merge_sort(list):
    if len(list) <= 1:
        return list
        """stoping condition"""
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    """recurvise again until reach to the stoping condition"""
    return merge(left, right)


def split(list):
    """
    divide the list at the midpoint 
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]
    return left, right


def merge(left, right):
    """
    merge two lists, sort them and retur a new list
    """
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    return l


def verify(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify(list[1:])


a = [4, 3, 2, 1, 33]
l = merge_sort(a)
print(verify(l))
