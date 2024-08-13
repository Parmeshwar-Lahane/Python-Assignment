# Write a program which accept N numbers from user and store it into list. Return addition of all elements from that list.

def main():
    print("\nThe perpose of this application, Addition of list element : ")

    # Creating list
    list1 = [11,22,33,44,55,66,77,88,99]
    print(f"List elements : {list1}")
    Ans = 0
    for i in (list1):       # Passing list1 element by i
        Ans += i        # Adding liste element with Ans one by one
        
    print(f"Addition of list elements : {Ans}\n\n")


if __name__=="__main__":
    main()