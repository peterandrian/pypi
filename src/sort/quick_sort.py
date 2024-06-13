class quicksort:
    def quicksort(listOfNumbers):
        if len(listOfNumbers) <= 1:
            return listOfNumbers
        else:
            pivot = [listOfNumbers[0]]
        
        lessThanPivot = []
        moreThanPivot = []

        for number in listOfNumbers[1:]:
            if number > pivot[0]:
                moreThanPivot.append(number)
            else:
                lessThanPivot.append(number)
        
        return quicksort(lessThanPivot) + pivot + quicksort(moreThanPivot)

# result = quicksort([3, 12, 3, 4, 5, 61, 2, 4, 3, 8, 17, 53, 64, 3, 4, 6, 5, 8, 9])
# print(result)
