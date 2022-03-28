

n = int(input())
d = list(map(int, input().split()))

m = sorted(d) # 리스트 d를 오름차순으로 정렬한 리스트를 리스트 m을 새로 만들어 여기에 넣어줍니다.
# sorted() 함수는 원래 리스트는 내버려 두고 정렬한 리스트를 새로 반환해주는 함수입니다.

m_dic = {} # 딕셔너리 m_dic을 만들어줍니다.

for i in range(n): # for문을 이용해 m_dic 딕셔너리에 key와 value를 각각 넣어줍니다.
    m_dic[m[i]] = i # key 값에는 오름차순으로 정렬된 리스트 d 값이 순서대로 들어가고,
                    # vales 값에는 인덱스 값처럼 숫자가 0부터 순서대로 들어가게 됩니다.

for i in range(n): # 딕셔너리 m_dic에서 d[i]와 같은 key 값의 value 값을 출력해줍니다.
    print(m_dic.get(d[i]), end = " ")



    
    
