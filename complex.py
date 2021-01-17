import math
class compleX:
	def __init__(self,r, i):
		self.real = r
		self.imaginary = i

	def __repr__(self):
		return '(%f, %f)'%(self.real, self.imaginary)   	

	def __add__(num1, num2):
		real_sum = num1.real + num2.real
		img_sum = num1.imaginary + num2.imaginary
		return compleX(real_sum,img_sum)	
	
	def __iadd__(num1,num2):
		num1.real=num1.real + num2.real
		num1.imaginary=num1.imaginary + num2.imaginary
		return num1

	def __sub__(num1, num2):
		real_dif = num1.real - num2.real
		img_dif = num1.imaginary - num2.imaginary
		return compleX(real_dif,img_dif)

	def __mul__(num1, num2):
		real_pro = num1.real*num2.real - num1.imaginary*num2.imaginary
		img_pro = num1.real*num2.imaginary + num2.real*num1.imaginary
		return compleX(real_pro,img_pro)

	def __truediv__(num1, num2):
		real_quo = (num1.real*num2.real+num1.imaginary*num2.imaginary)/(num2.real**2 + num2.imaginary**2)
		img_quo = (num2.real*num1.imaginary-num1.real*num2.imaginary)/(num2.real**2 + num2.imaginary**2)
		return compleX(real_quo,img_quo)

	
class polar(compleX):	
	def __init__(self,r,i):
		num=compleX(r,i)
		self.rho = math.sqrt(num.real**2+num.imaginary**2)
		self.theta = math.atan(num.imaginary/num.real)

	def __repr__(self):
		return '%f, %f'%(self.rho, self.theta)

	def __add__(num1,num2):
		rho = num1.rho+num2.rho
		theta = num1.theta+num2.theta
		return (rho*math.cos(theta),rho*math.sin(theta))
	
	def __sub__(num1,num2):
		rho = num1.rho-num2.rho
		theta = num1.theta-num2.theta
		return (rho*math.cos(theta),rho*math.sin(theta))		

	def __mul__(num1, num2):
		rho = num1.rho*num2.rho
		theta = num1.theta+num2.theta
		return (rho, theta)

	def __truediv__(num1, num2):
		rho = num1.rho/num2.rho
		theta = num1.theta-num2.theta
		return (rho, theta)

	def __pow__(num,power):
		real=num.rho**power
		img=num.theta*power
		return (real, img)


def conjugate(num):
	num.imaginary=num.imaginary*-1
	return compleX(num.real,num.imaginary)						


def root(num,root):
	img=[]
	real=num.rho**(1/float(root))
	for i in range(root):
		ans=1/root*(num.theta+2*math.pi*i)
		img.append((real,ans))
	return img			
			

def plot(num):
	import matplotlib.pyplot as plt 
	plt.ylabel("imaginary")
	plt.xlabel("real")
	plt.title("Argand plane")
	plt.scatter(num.real, num.imaginary)
	plt.show()

def nthrootunity(n):
	import matplotlib.pyplot as plt
	li=root(polar(1,0),n)
	ax = plt.subplot(111, projection='polar')
	ax.plot([x[1] for x in li],[x[0] for x in li])
	plt.ylabel("imaginary")
	plt.xlabel("real")
	plt.title("Argand plane")
	plt.show()

print("------------------------------Complex numbers------------------------------")
print("Enter two complex numbers:")
r1=float(input("Real part:"))
i1=float(input("Imaginary part:"))
r2=float(input("Real part:"))
i2=float(input("Imaginary part:"))
num1=compleX(r1,i1)
num2=compleX(r2,i2)
print("Addition =",num1+num2)
print("Subtraction =",num1-num2)
print("Multiplication =",num1*num2)
print("Division =",num1/num2)
print("Polar representation:")
num3=polar(r1,i1)
num4=polar(r2,i2)
print("Addition=",num1+num2)
print("Subtraction=",num1-num2)
print("Multiplication=",num1*num2)
print("Division=",num1/num2)
print("9th power of",num1,":",num3**9)
print("5th root of",num2,":",root(num4,5))
print("Multiplication by (-1,0) changes the sign of real & imaginary part:",num1*compleX(-1,0))
print("Plotting ",num1,"on argand plane...")
plot(num1)
print("Plotting 5th root of unity....")
nthrootunity(5)	