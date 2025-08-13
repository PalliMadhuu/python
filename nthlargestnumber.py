def findNthLargestOrPrintLeast():
    userInput=int(input("Enter the number : "))
    userStringInput=str(userInput)
    nthLargest=int(input("Enter the nth largest value you want : "))
    inputAfterRemovingDuplicates=[]
    for originalValue in range(len(userStringInput)):
            isDuplicate=False
            for j in range(len(inputAfterRemovingDuplicates)):
             if(userStringInput[originalValue]==inputAfterRemovingDuplicates[j]):
                isDuplicate=True
                break
            else:
                inputAfterRemovingDuplicates.append(str(userStringInput[originalValue]))
    for index in range(len(inputAfterRemovingDuplicates)):
        for j in range(index+1,len(inputAfterRemovingDuplicates)):
            if(int(inputAfterRemovingDuplicates[index]) < int(inputAfterRemovingDuplicates[j])):
                    existingUpperValue=inputAfterRemovingDuplicates[j]
                    existingLowerValue=inputAfterRemovingDuplicates[index]
                    inputAfterRemovingDuplicates[index]=existingUpperValue
                    inputAfterRemovingDuplicates[j]=existingLowerValue
    if(nthLargest<=inputAfterRemovingDuplicates.__len__()):
        print(inputAfterRemovingDuplicates[nthLargest-1])
    
    else:
        print(inputAfterRemovingDuplicates[inputAfterRemovingDuplicates.__len__()-1])
findNthLargestOrPrintLeast()