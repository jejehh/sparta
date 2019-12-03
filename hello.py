def oddeven(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
	if num % 2 == 0: # num을 2로 나눈 나머지가 0이면
		 return True   # True (참)을 반환한다.
	else:            # 아니면,
		 return False  # False (거짓)을 반환한다.

def checkbob(name):
	if name == 'bob': # name이 'bob'이면 True를, 아니면 False를 반환해라
		return True
	else:
		return False


print (oddeven(11))