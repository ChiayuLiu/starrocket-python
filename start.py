#HW1
#讓使用者輸入五個數字，然後1.告訴人家哪一個數字最大2.算總額

#題目一
n1=input("Enter a Number:") 
n2=input("Enter a Number:")
n3=input("Enter a Number:") 
n4=input("Enter a Number:")
n5=input("Enter a Number:") 
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
nums=[n1,n2,n3,n4,n5]
max_nums=max(nums)
print(max_nums)

#題目二
n1=input("Enter a Number:") 
n2=input("Enter a Number:")
n3=input("Enter a Number:") 
n4=input("Enter a Number:")
n5=input("Enter a Number:") 
n1=int(n1)
n2=int(n2)
n3=int(n3)
n4=int(n4)
n5=int(n5)
result=n1+n2+n3+n4+n5
print(result)
