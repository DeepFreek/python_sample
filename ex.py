def Scan_Nums(Nums):#Ввод списка
    n=int(input("enter n\n"))
    for i in range(n):
        a=int(input("enter number\n"))
        nums.append(a)
    return nums

def Find_N(n,nums,mid):#Поиск равного значения
    flag=-1
    if mid == n:
        flag = len(nums) // 2
    elif n > mid:
        for i in range(len(nums) // 2, len(nums)):
            if n == nums[i]:
                flag = i
    else:
        for i in range(0, len(nums) // 2 + 1):
            if n == nums[i]:
                flag = i
    return flag


#nums=[1,2,3,4,5,6,7]
nums=[]
Scan_Nums(nums)
n=int(input("enter number to find\n"))
flag=-1
mid=nums[len(nums)//2] #центральное значение массива, от него ищем справа или слева
flag=Find_N(n,nums,mid)
print("Искомый номер на {} месте".format(flag))


