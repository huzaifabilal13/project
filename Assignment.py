x=0
while True:
	try:
		print("Enter no. corresponding to beam type.")
		x= int(input("1)Simply supported beam. 2) Cantilever beam. 3) Overhanging beam :"))
	except ValueError:
			print("Incorrect Input!")
			continue
	else:
		if x==1:
			wx=0
			while True:
				try:
					wx= float(input("Enter UDL on beam :"))
				except ValueError:
					print("Incorrect Input!")
					continue
				else:
					lx=0
					while True:
						try:
							lx= float(input("Enter length of beam :"))
						except ValueError:
							print("Incorrect Input!")
							continue
						else:
							r1x= (wx*lx/2)
							r2x= (wx*lx/2)
							print("Reaction at left support :")
							print(r1x)
							print("Reaction at right support :")
							print(r2x)
							print("Calculation complete. Back to beginning.")
							break
					break
		if x==2:
			wy=0
			while True:
				try:
					wy= float(input("Enter UDL on beam :"))
				except ValueError:
					print("Incorrect Input!")
					continue
				else:
					ly=0
					while True:
						try:
							ly= float(input("Enter length of beam :"))
						except ValueError:
							print("Incorrect Input!")
							continue
						else:
							ry= (wy*ly)
							my= (wy*ly*ly/2)
							print("Reaction at fix support: ")
							print(ry)
							print("Moment at fix support: ")
							print(my)
							print("Calculation complete. Back to beginning.")
							break
					break	
		if x==3:
			wz=0
			while True:
				try:
					wz= float(input("Enter UDL on beam :"))
				except ValueError:
					print("Incorrect Input!")
					continue
				else:
					l1z=0
					while True:
						try:
							l1z= float(input("Enter length of beam(A to B) :"))
						except ValueError:
							print("Incorrect Input!")
							continue
						else:
							l2z=0
							while True:
								try:
									l2z= float(input("Enter length of beam(B to C) :"))
								except ValueError:
									continue
								else:
									L=(l1z+l2z)
									r1z= (((wz*l1z**2/2)-(wz*l2z**2/2))/2)
									r2z= ((wz*(l1z+l2z)**2)/(2*(l1z+l2z)))
									print("Reaction at left support :")
									print(r1z)
									print("Reaction at right support :")
									print(r2z)
									print("Calculation complete. Back to beginning.")
									break
							break
					break
	
	
	
