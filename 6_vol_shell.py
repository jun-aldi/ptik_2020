from math import *
def vol_shell(r1,r2):
	vol=round(abs(((4/3) *pi)*((r1**3)-(r2**3))),3)
	return vol
print(vol_shell(7,2))