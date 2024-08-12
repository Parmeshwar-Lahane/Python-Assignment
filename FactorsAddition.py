# Write a program which accept one number from user and return addition of factors.

print("\nProgram is to find Factors and its addition ")
def main():
    Temp1 = 0
    No = int(input("\nEnter number : "))
    for i in range(1,int(No/2)+1,1):
        if (No%i) == 0:
            print(i,end=",")
            Temp1 = Temp1 + i
    print(f"\nAddition of Factors : {Temp1}\n")

if __name__=="__main__":
    main()