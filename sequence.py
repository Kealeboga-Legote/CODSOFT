
def is_sequence(subMain,m):

    sCounter = 0
    mCounter = 0
    
    while sCounter < len(subMain) and mCounter < len(m):
        if subMain[sCounter] == m[mCounter]:
            sCounter += 1
        mCounter += 1
    
    # returns "True" if subMain is a subsequence of m 
    return sCounter == len(subMain) 

if __name__ == "__main__":
    m = input("Enter the full string: \n")
    subMain = input("Enter the sequence to check for: \n")

    if is_sequence(subMain, m):
        print("The given substring is a subsequence of the full string.")
    else :
        print("The given substring is not a subsequence of the full string.")