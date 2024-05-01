def solveTallyPuzzle(N, T):
    tally_list = [0]*(T+1)
    tally_list[0] = 1
    print(tally_list)

    for num in N:

        
        for i in range(num, T + 1):
        
            
            tally_list[i] =tally_list[i] +tally_list[i - num] # tally_list[1}=tally_list[1] +tally_list[1-1] if num =1 
            print(tally_list)    
        
    print(tally_list)
    return tally_list[T]

# Sample Input
N = [1,2,5]
T = 10

# Calculate and print the result

result = solveTallyPuzzle(N, T)
print(result)

