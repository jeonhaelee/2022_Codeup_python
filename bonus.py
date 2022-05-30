class Node():
	def __init__ (self):
		self.data = None
		self.link = None

def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')

def makeLinkedList(arr):
    memory = []
    head, current, pre = None, None, None

    node = Node()			
    node.data = arr[0]
    head = node
    memory.append(node)

    for data in arr[1:]:		
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    return head

def make_3arr(input_arr):
    arr1 = []; arr2 = []; arr3 = []
    for i in range(len(input_arr)):
        get = str(input_arr[i])
        a = get[0]; b = get[1]; c = get[2]
        arr1.append(a)
        arr2.append(b)
        arr3.append(c)

    return arr1, arr2, arr3

    # 목표: 연결리스트에 넣을 데이터인 '자리수가 동일한 숫자들로 구성된 3개의 배열' 반환 (1점)
    

def makeDigits(node):
    li = node.data
    number = ""
    for i in range(len(li)-1, -1, -1):
        number += li[i]
    return int(number)
    # 목표: 거꾸로 삽입된 연결리스트가 나타내는 5자리 정수 만들기 (3점)


def makeReversedLinkedList(number):
    number = str(number)
    li = []
    for i in range(len(number)-1,-1,-1):
        li.append(int(number[i]))
    return makeLinkedList(li)
    # 목표: 숫자를 받아 거꾸로 삽입된 연결리스트 만들기 (3점)
    

def addNumber(node1, node2, node3):
    result_num = makeDigits(node1) + makeDigits(node2) + makeDigits(node3)
    # print(result_num)
    return makeReversedLinkedList(result_num)
    # 목표: 3개의 연결리스트가 나타내는 정수 3개의 합으로 거꾸로 삽입된 연결리스트의 시작 노드 반환 (3점)
    # 조건: makeDigits(), makeReveredLinkedList() 사용 (조건 어길 시, 해당 함수 구현 0점 처리)


# 결과 테스트 부분 (아래 코드를 수정하지 마시오.)

input_arr = [436, 193, 583, 267, 829]
print('## 입력:', input_arr)

arr1, arr2, arr3 = make_3arr(input_arr)                                                    # 자리수가 동일한 숫자들로 구성된 3개의 배열 생성
head1, head2, head3 = makeLinkedList(arr1), makeLinkedList(arr2), makeLinkedList(arr3)     # 기본 연결리스트 생성

print('\n## 생성한 연결 리스트')
print('# [ ', end='')
printNodes(head1)
print(']\n# [ ', end='')
printNodes(head2)
print(']\n# [ ', end='')
printNodes(head3)
print(']')

result = addNumber(head1, head2, head3) # 3개의 연결리스트가 나타내는 숫자의 합을 나타내는 '거꾸로 삽입된 연결리스트' 생성
print('\n## 출력: ', end='')
printNodes(result)





