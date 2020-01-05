def solution(data, n):
    newlist = data
    if len(data) > max(data):
        length = len(data)
    else:
        length = max(data)
    for i in range(length+1):
        if data.count(i) > n:
            for x in range(data.count(i)):
                newlist.remove(i)
    return newlist



