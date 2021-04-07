def remove_duplicate(duplicate):
    new_list = []
    for num in duplicate:
        if num not in new_list:
            new_list.append(num)
    return new_list


MyList = [10, 10, 30, 30, 20, 60, 70, 70, 40, 55, 45, 45]
print(remove_duplicate(MyList))
