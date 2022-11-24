# 2022/11/24 약수
def solution(number, limit, power):
  answer = 0
  # 1 ~ number까지 수행
  for knight in range(1, number + 1):
    p = 0
    # 약수 구하기(knight**0.5+1 까지만 계산)
    for num in range(1, int(knight**0.5) + 1):
      # 약수인 경우 +1
      # 4인 경우 4, 16의 경우를 포함하므로 + 2를 한다.
      if knight % num == 0:
        p += 1
        if num ** 2 != knight: # 중복되는 경우 제외
          p += 1
      # limit를 넘은 경우 p는 power
      if p > limit:
        p = power
        break
      answer += p
  # 정답 반환
  return answer