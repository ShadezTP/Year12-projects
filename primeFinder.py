def primeFinder(top):
    # i am truly sorry for what you are about to witness
    #cycles through each potential prime in the range given by user
    for i in range(top):
        #cycles through each potential factor under a half of the range of the potential prime
        for j in range(int(i / 2)):
            #Checks if a number is an integer in a weird way, as it will always be stored as a float
            if i / (j + 2) == int(i/(j + 2)):
                #If it has 1 factor we know it cant be a prime, so we skip checking its other potential factors
                break
            elif j == int((i / 2)) - 1:
                #if this is the last potential factor and it isnt a factor, then we know the number is prime
                #as it passed through without breaking
                print(i)

primeFinder(int(input("Please enter an integer for the range in which you will check for prime numbers: ")))
