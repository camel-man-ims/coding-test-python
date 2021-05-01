def solution(citations):
    citations.sort(reverse=True)
    h = 0

    for pointer in range(len(citations)):
        count = pointer + 1
        count_desc = len(citations) - pointer - 1

        if count_desc < citations[pointer] <= count:
            h = max(h, citations[pointer])

    return h