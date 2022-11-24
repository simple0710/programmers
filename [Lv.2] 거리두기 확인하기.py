# 2022/11/24 BFS
# 입력값 : [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
from collections import deque

def bfs(stx, sty, place):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  visited = [[False] * 5 for _ in range(5)]
  q = deque()
  q.append((stx, sty))
  visited[stx][sty] = 1
  while q:
    x, y = q.popleft()
    if visited[x][y] >= 3:
      continue
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and place[nx][ny] != 'X':
        q.append((nx, ny))
        visited[nx][ny] = visited[x][y] + 1
        # 사람이고 거리가 2 이하인 경우 0 반환
        if place[nx][ny] == 'P' and visited[nx][ny] <= 3:
          return 0
  # 아무 이상 없는 경우 1 반환
  return 1

def solution(places):
  ans = []
  # n번 대기실
  for place in places:
    flag = 1
    # 전 지역 탐색
    for i in range(5):
      for j in range(5):
        # 한 사람에 대한 거리 계산
        if place[i][j] == "P":
          flag = bfs(i, j, place)
          # 만약 거리가 2 이하인 사람이 있는 경우 끝내기
          if flag == 0:
            break
      if flag == 0:
          break
    # flag 추가
    ans.append(flag)
  # 정답 반환
  return ans