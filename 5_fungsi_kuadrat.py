from math import *
def solution(a,b,c):
	solution = 0
	if (b**2) - (4*a*c) > 0:
		solution = 2
	if  (b**2) - (4*a*c) == 0:
		solution = 1
	if (b**2) - (4*a*c) < 0:
		solution = 0
	print(solution,"solution")
	if solution >= 0:
		x1=int((-b+ sqrt((b**2) - (4*a*c)))//2)
		x2=int((-b- sqrt((b**2) - (4*a*c)))//2)               
		print("x1:",x1,"x2:",x2)
		
solution(2,5,2)
		