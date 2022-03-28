

n = int(input()) # 데이터의 개수 입력 받기
d = list(map(int,input().split())) # 데이터 정수로 입력받아 리스트 d에 담아주기

m = sorted(d) # 오름차순으로 정렬한 리스트 d를 새로운 리스트 m에 넣어주기

count = 0 # 몇단계인지 알기 위한 count 변수 만들어주기
for j in range(n): # 거품 정렬 (버블 정렬)
    for i in range(n-1):
        if d[i] > d[i+1]: 
            temp = d[i]
            d[i] = d[i+1]
            d[i+1] = temp
    count += 1 # 한 단계 마칠 때마다 count에 1씩 더해주기
    if m == d: # 한 단계 마칠 때마다 if문으로 d가 정렬한 m과 같은지 확인하여, 만약 같다면 for문 탈출해주기
        break

print(count) # count 변수 출력해주기
