# program that takes two integers and displays the result of their addition,subtraction,multiplication and division
n1,n2=map(int,input("Enter two integers:").split())
print("{}+{}={}".format(n1,n2,n1+n2)) 
print("{}-{}={}".format(n1,n2,n1-n2)) 
print("{}*{}={}".format(n1,n2,n1*n2)) 
print("{}/{}={}".format(n1,n2,n1/n2))
