
def find_leap_years(given_year):
    count=0
    list_of_leap_years=[]
    #given_year+=1    
    while(count<15):
        if(given_year%4==0):
            if(given_year%100==0):
                if(given_year%400==0):
                    list_of_leap_years.append(given_year)
                    count=count+1
            else:
                list_of_leap_years.append(given_year)
                count=count+1
                
        given_year=given_year+1        
        
    return list_of_leap_years

list_of_leap_years=find_leap_years(1000)
print(list_of_leap_years)
