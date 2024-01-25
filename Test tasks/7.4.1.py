# link to task https://stepik.org/lesson/891577/step/2?unit=896427

some_list = [7, 14, 28, 32, 32, 56]

def custom_filter(list) -> bool:
    summ = 0
    for element in list:
        if type(element) is int and element % 7 == 0:
            summ += element
    if summ >= 83:
        return False
    else:
        return True

print(custom_filter(some_list))


# Alternative solve
# def custom_filter(some_list):
#    return sum(filter(lambda x: type(x) == int and x % 7 == 0, some_list)) <= 83
