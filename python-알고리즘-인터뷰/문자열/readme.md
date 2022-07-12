# 1. 문자열

## 1-1) 유효한 펠린드롬

> * [link](https://leetcode.com/problems/valid-palindrome/)
> * [폴더이동](./유효한펠린드롬/)

### a. 문제 요약

* 공백이나 , 삭제하고 해당 문자열이 팰린드롬인지 확인하는 문제
* ex) race a car
  * raceacar (X)

### b. 포인트

* 공백이랑 ,를 잘라서 문자열에 담기
  * 문자열, 숫자 판별 메서드
    * `isalnum()`
  * `re.sub('[^a-zA-Z0-9]','',strs)`

* 뒤집기
  * list(스택) 사용 -> `list.pop(0) != list.pop()`
  * deque 사용 -> `list.popleft() != list.pop()`
  * 뒤집기 사용 -> `strs == strs[::-1]`

## 1-2) 문자열 뒤집기

> * [link](https://leetcode.com/problems/reverse-string/)

### a. 문제 요약

* 배열로 된 문자열 뒤집기

### b. 포인트

`a,b = b,a`

## 1-3) 로그파일 재정렬

> * [link](https://leetcode.com/problems/reorder-data-in-log-files/)

### a. 문제 요약

* 문제 이해가 정확히 안돼서 그냥 넘어갔다.
* array가 주어졌을 때, 두번째, 그리고 첫번째 기준으로 정렬하기

### b. 문제 포인트

* `문자열.isdigit()`
* 정렬 규칙 `lambda`
  * `letters.sort(key=lambda x:(x.split[1:], x.split[0])`

## 1-4) 그룹 에너그램

> * [link](https://leetcode.com/problems/group-anagrams/)

### a. 문제 요약

* 같은 문자끼리 묶어서 반환하기

### b. 포인트

* java
  * `map.containsKey()`
* python
  * `val = defaultdict(list)`
    * `return list(val.values())`

## 1-5) 가장 흔한 단어

> * [link](https://leetcode.com/problems/most-common-word/)
> * [폴더이동](./가장흔한단어/)

### a. 문제 요약

* string값이 주어졌을 때, 가장 흔하게 등장하는 단어를 반환하기
  * 단, banned에는 없는 단어어야 한다.

### b. 포인트

* java
  * `split("  ")` -> `split(" ")`
  * word 파싱
    * `replace` 를 사용하면 딱 해당하는 문자열만 파싱된다. 정규표현식을 사용하려면 `replaceAll`을 사용해야 한다.
    * `replaceAll`
      * `replaceAll("[\\w]"," )`
* python
  * `re.sub`
  * `counter`
    * `counter.most_common(1)[0][0]`

## 1-6) 가장 긴 팰린드롬 부분 문자열

### a. 문제 요약

* 문제 그대로, appappb 와 같이 값이 주어졌을 때 `ppapp`값이 가장 긴 팰린드롬 부분 문자열이므로 해당 값을 반환하기.

### b. 포인트

* 재귀
  * 재귀써서 하면 문자 길시 터진다.
  * while 안에서 `left--`, `right ++` 해야한다
* python
  * max 구할 시 parameter에 여러 값 넘기고, key값만 주면 됨