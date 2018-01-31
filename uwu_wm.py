#!/usr/bin/python3


import sys
import os
from subprocess import check_output as check


'''

...		         	###########		
... 		        #         #		
... 		        #         #		
... 		        #         #		
... 		        #         #		
... 		        #    0    #			
... 		        #         #		
... 		        #         #
... 		        #         #
... 		        #         #
... 		        #         #
... 		        ###########



0,0,1920,1080           T:1920,0,1080,610
			B:1920,610,1080,1310

####################	###########
#                  #  #         #
#                  #  #    2    #
#                  #	#         #
#                  #	###########
#        1         #	#         #
#                  #	#         #
#                  #	#    3    #
#                  #	#         #
#                  #	#         #
#                  #	#         #
####################	###########


L: 0,0,960,1080		T: 1920,0,1080,960
R: 0,960,960,1080	B: 1920,960,1080,960

####################	###########
#        #         #  #         #
#        #         #  #         #
#        #         #	#    6    #
#        #         #	#         #
#   4    #    5    #	###########
#        #         #	###########
#        #         #	#         #
#        #         #	#    7    #
#        #         #	#         #
#        #         #	#         #
####################	###########

T: 0,0,1920,540
B: 0,540,1920,540

####################	...
#                  # 	...
#        8         #	...
#                  #	...
#                  #	...
####################	...
####################	...
#                  #	...
#        9         #	...
#                  #	...
#                  #	...
####################	...

'''

gap_enable, gap_size = False, 12
args = sys.argv


if args[1] in [str(i) for i in range(0, 10)]: 
	p0 = [1920,0,1080,1920]
	p1 = [0,0,1920,1080]
	p2 = [1920,0,1080,607]
	p3 = [1920,607,1080,1313]
	p4 = [0,0,960,1080]
	p5 = [960,0,960,1080]
	p6 = [1920,0,1080,960]
	p7 = [1920,960,1080,960]
	p8 = [0,0,1920,540]
	p9 = [0,540,1920,540]

	positions = [p0, p1, p2, p3, p4, p5, p6, p7, p8, p9]

	p = positions[int(args[1])]

	if gap_enable:
		if args[1] == "1" or args[1] == "0":
			add = [gap_size, gap_size, - 2*gap_size, - 2*gap_size]
			p = [x + y for x, y in zip(p,add)]
		if args[1] == "4":
			add = [gap_size, gap_size, -1.5*gap_size, - 2*gap_size]
			p = [x + y for x, y in zip(p,add)]
		if args[1] == "5":
			add = [0.5*gap_size, gap_size, - 1.5*gap_size, - 2*gap_size]
			p = [x + y for x, y in zip(p,add)]
		if args[1] in ["2", "6", "8"]:
			add = [gap_size, gap_size, - 2*gap_size, - 1.5*gap_size]
			p = [x + y for x, y in zip(p,add)]
		if args[1] in ["3", "7", "9"]:
			add = [gap_size, 0.5*gap_size, - 2*gap_size, - 1.5*gap_size]
			p = [x + y for x, y in zip(p,add)]
		
		
	print(p)

	# wmctrl -i -r `xdotool getwindowfocus` -e 0,1920,610,1080,1310
	p = [int(val) for val in p]
	p = [str(val) for val in p]
	os.system("wmctrl -i -r `xdotool getwindowfocus` -e 0," + ",".join(p))

