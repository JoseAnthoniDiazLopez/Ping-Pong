import os,random
import msvcrt
if __name__ == '__main__':
	alto = 20
	ancho = 50
	pelotax = random.randint(1,ancho)
	pelotay = 1
	reglax = 20
	velocidad = 900
	i = velocidad
	direccionx = 1
	direcciony = 1
	anchoball=0
	altoball=0
	blokdur=[]
	class objeto:
		def __init__(self):
			self.x=random.randint(2,49)
			self.y=random.randint(2,10)
	
	for i in range(50):
		blokdur.append(objeto())

	input("Jugar? enter y")
	#	time.sleep(0.09)
	while True:	
		
		if msvcrt.kbhit():
				key = msvcrt.getwch()
				key = msvcrt.getwch()
				if key == "K" and reglax>0:
					reglax-=3
				elif key == "M" and reglax+10<ancho-1:
					reglax+=3
				
				key=""
		if i>=velocidad:
			os.system("cls")
			for py in range(1,alto+1):
				for px in range(1,ancho+1):
					if px==pelotax and py==pelotay:
						pixel = "o"
					else:
						if py==1:
							pixel = "-"
						elif py==alto:
							pixel = "_"
						else:
							pixel = " "
						if px==1:
							pixel = "|"
						elif px==ancho:
							pixel = "|"
						if py==18 and px>reglax and px<reglax+10:
							pixel = "_"
					for o in blokdur:
						if o.x==px and o.y==py:
							pixel="-"
					print(pixel, end="")
				print("")
			pelotax = pelotax+direccionx
			pelotay = pelotay+direcciony
			if pelotax+anchoball>ancho or pelotax<2:
				direccionx = direccionx*(-1)
				
			if pelotay<2:
				direcciony = direcciony*(-1)
			for o in blokdur:
						if o.x==pelotax and o.y==pelotay:
							direcciony = direcciony*(-1)
								
			if pelotay+altoball>alto:
				print("Perdiste")
				break
				
			if pelotay==18 and pelotax>reglax and pelotax<reglax+10:
				direcciony = direcciony*(-1)
			i=1
				
		i=i+1
	
			
		
