class FastSlowPointer:
    def happyNumber(_self, number):
        sumNumbers = set()
        sumNumbers.add(number)
        
        while len(sumNumbers) > 0:
            sum = 0 
            while number > 0:
                rest = (int) (number % 10)
                number = number // 10
                sum += rest * rest
                
            number = sum

            if sum == 1:
                return True
            elif number not in sumNumbers:
                sumNumbers.add(sum)
            else:
                break
            
        print(sumNumbers)
        return False
    
fastSlowPointer = FastSlowPointer()

print(fastSlowPointer.happyNumber(26))