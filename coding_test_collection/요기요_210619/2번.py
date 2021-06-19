# admin -wx 29 Sep 1983    833 source.h
# admin r-x 15 Sep 1999  23322 lol.exe
# admin --x 02 Sep 1983   4343 log.zip
# ...
# 이름이 admin 이고, 권한이 x 이고, 파일용량이 14*2^20 을 넘지 않는 파일 중에 가장 오래된 날짜를 반환하라
# 0 admin
# 1 --x
# 2 월
# 3 년
# 4 용량
# 5 이름 ( 상관x )

# \n 을 기준으로 문자열 자르고
# split(" ") 으로 공백을 기준으로 array 만들고
# 각 split 된 값들 중 "" 을 지우고
# 그 중 위의 조건에 따라 년월일을 가져오고
# sorting 하고
# 월에 따라 문자열로 바꿔준다 ( 월이 문자이기 때문에 문자 -> 숫자 비교 -> 다시 문자 )

import math


def solution(s_input):
    arr = []
    value_arr = []
    pointer = 0
    for i in range(len(s_input)):
        if s_input[i] == '\n':
            arr.append(s_input[pointer:i])
            pointer=i+1
    for s in arr:
        split = s.split(" ")
        temp= []
        for attribute in split:
            if attribute != '':
                temp.append(attribute)
        value_arr.append(temp)
    # ----
    result_reserve = []
    for individual_arr in value_arr:
        owner = individual_arr[0]
        perm = individual_arr[1]
        day = individual_arr[2]
        month = individual_arr[3]
        year = individual_arr[4]
        size = individual_arr[5]

        if month == 'Jan':
            month = 1
        if month == 'Feb':
            month = 2
        if month == 'Mar':
            month = 3
        if month == 'Apr':
            month = 4
        if month == 'May':
            month = 5
        if month == 'Jun':
            month = 6
        if month == 'Jul':
            month = 7
        if month == 'Aug':
            month = 8
        if month == 'Sep':
            month = 9
        if month == 'Oct':
            month = 10
        if month == 'Nov':
            month = 11
        if month == 'Dec':
            month = 12

        if owner=='admin' and perm[2]=='x' and int(size) < int(math.pow(2,20) * 14):
            result_reserve.append([year,month,day])
    result_reserve.sort()

    month_result =""
    if result_reserve[0][1] == 1:
        month_result="Jan"
    if result_reserve[0][1] == 2:
        month_result="Feb"
    if result_reserve[0][1] == 3:
        month_result="Mar"
    if result_reserve[0][1] == 4:
        month_result="Apr"
    if result_reserve[0][1] == 5:
        month_result="May"
    if result_reserve[0][1] == 6:
        month_result="Jun"
    if result_reserve[0][1] == 7:
        month_result="Jul"
    if result_reserve[0][1] == 8:
        month_result="Aug"
    if result_reserve[0][1] == 9:
        month_result="Sep"
    if result_reserve[0][1] == 10:
        month_result="Oct"
    if result_reserve[0][1] == 11:
        month_result="Nov"
    if result_reserve[0][1] == 12:
        month_result="Dec"

    str_result = str(result_reserve[0][2]) + " " + str(month_result) + " " + str(result_reserve[0][0])
    return str_result


s = solution(
    'admin  -wx 29 Sep 1983        833 source.h\nadmin  r-x 23 Jun 2003     854016 blockbuster.mpeg\nadmin  --x 02 Jul 1997        821 delete-this.py\nadmin  -w- 15 Feb 1971      23552 library.dll\nadmin  --x 15 May 1979  645922816 logs.zip\njane   --x 04 Dec 2010      93184 old-photos.rar\njane   -w- 08 Feb 1982  681574400 important.java\nadmin  rwx 26 Dec 1952   14680064 to-do-list.txt')

print(s)