print("Select operation.")
print("1. Under Rs.10 Lakh ")
print("2. Under Rs.15 Lakh ")
print("3. Under Rs.20 Lakh" )
print("4. Under Rs.25 Lakh" )

budget = int(input("Choose Your Budget: "))
category = int(input(''' Select your car category
                    1.SUV
                    2.Sedan
                    3.Hatchack
            Enter: ''', ))
if budget in (1,2,3,4):
    
    if budget == 1:
        if category ==1:
            
                        print('''1.Maruti Suzuki
        Specifications--> Price: 5.85 - 8.67 Lakh
                          ARAI Mileage is 23.76 kmpl
                          Engine Displacement 1197cc
                          Max Power(bhp@rpm) 88.50bhp@6000rpm
                          Seating Capacity  5 people
                          Boot Space  268L
                          Service Cost (Avg. of 5 years) is Rs.4,703
                          Fuel Tank Capacity is 37.0L
                          Transmission Type is Automatic
                          Fuel Type: Petrol
********************************************************************************************
                          
                          2. Maruti Baleno
                          Specifications-->''')  
    else:
        print("User has lost his mind")    