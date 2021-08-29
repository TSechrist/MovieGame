
while True:

    # string1 = "Hello"
    # string2 = "oellH"

    string1 = input("String 1: ")
    string2 = input("Reverse of string 1: ")

    if len(string1) != len(string2):
        print("Not equal")
    else:
        rev = string2[::-1]
        for i in range(0, len(string1)):
            if(string1[i] != rev[i]):
                print("Not equal")
                break
    print("Equal")

