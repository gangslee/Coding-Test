# 이진트리 정의 : 이진 트리(Binary Tree)는 최대 2개의 자식 노드를 가질 수 있는 노드를 의미합니다. 즉 한개의 노드가 2개의 자식노드를 가지거나 한개를 가지거나 아예 안 가질수 있습니다.

# 문제풀이 방법 : i1이 2개이상이 아닌 경우(부모가 2개이상이 아닌 경우), i2가 3개이상이 아닌 경우 (자식이 3개 이상이 아닌 경우)

# 참고 : https://lktprogrammer.tistory.com/67

def ArrayChallenge(strArr):
    childs, parents = list(), list()

    for sa in strArr:
        current = sa.lstrip().rstrip().split(',')

        childs.append(current[0])
        parents.append(current[1])

    childSet, parentSet = set(childs), set(parents)

    for c in childSet:
        if childs.count(c) > 1:
            return False

    for p in parentSet:
        if parents.count(p) > 2:
            return False
    # code goes here
    return True


# keep this function call here
print(ArrayChallenge(input()))

'''
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
Output: true
Input: ["(1,2)", "(1,3)"]
Output: false
'''
