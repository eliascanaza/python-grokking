class FastSlowPointer:
    def happyNumber(_self, number):
        sum = number
        numList = set()
        numList.add(number)

        while sum != 1:
            sum = 0
            
            while number > 0:
                digit = number % 10
                number //= 10
                sum += digit * digit
            
            if sum in numList: 
                return False
            
            numList.add(sum)
            number = sum

        return True
    
fastSlowPointer = FastSlowPointer()

print(fastSlowPointer.happyNumber(40))