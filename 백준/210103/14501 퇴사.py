# 다이나믹 프로그래밍으로 풀기

N = int(input())
time = list(list(map(int, input().split())) for _ in range(N))
dp = [0] * N


for i in range(N):
    if i + time[i][0] <= N:
        dp[i] = time[i][1]  # 현재 인덱스 값과 현재 인덱스의 업무 시간을 더하여 N보다 큰지 검수

        # 이전 값들을 돌면서 i에 위치한 result값과 (j에 위치한 result값 + i 업무시간) 중 최대값을 선택
        for j in range(i):
            if j + time[j][0] <= i:
                dp[i] = max(dp[i], dp[j] + time[i][1])

print(max(dp))
