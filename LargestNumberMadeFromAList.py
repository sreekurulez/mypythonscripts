def create_largest_number(number_list):
        
        number_list.sort()
        number_list.reverse()
        print(number_list)
        temp =''
        for i in number_list:
            temp += str(i)
    
        largest_number =int(temp)
        return largest_number
    #remove pass and write your logic here

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)
