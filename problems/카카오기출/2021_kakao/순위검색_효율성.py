def solution(infos, query):

    result =[]

    for query_one in query:

        split_query = query_one.split(" ")
        split_query_no_and = []

        for s in split_query:
            if s != "and":
                split_query_no_and.append(s)
        count = 0

        for info in infos:
            split_info = info.split(" ")

            if (split_query_no_and[0] == '-' or split_query_no_and[0] == split_info[0]) \
                    and (split_query_no_and[1] == '-' or split_query_no_and[1] == split_info[1]) \
                    and (split_query_no_and[2] == '-' or split_query_no_and[2] == split_info[2]) \
                    and (split_query_no_and[3] == '-' or split_query_no_and[3] == split_info[3]) \
                    and int(split_info[4]) >= int(split_query_no_and[4]):
                count +=1
        result.append(count)

    return result

solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"])