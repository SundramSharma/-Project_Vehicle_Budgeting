import tkinter as tk
from tkinter import Button, Label, PhotoImage
from tkinter.constants import DISABLED, INSERT
from tkinter.font import Font
from PIL import ImageTk
from PIL import Image



root = tk.Tk()
#root.geometry("1366x768")

#this creates the UI box
canvas = tk.Canvas(height=400, width=700 )
canvas.grid(columnspan=20, rowspan=20)

#showing the logo
logo = Image.open('D:\Things To Do\Programming\logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)  
               
#taking input
instructions = tk.Label(root,text="Select Your Budget ", font="Raleway")
instructions.grid(columnspan=3, column=0, row=3,)

#main program
value = 1
def change_value():
       global value
       value -= 1
       if value == 0:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 BTunder10HB.grid(column=1 ,row=2) 
                 BTunder10SUV.grid(column=1 ,row=3)
                 BTunder10Sedan.grid(column=1, row=4)
                 budget_btn1.grid(column=1, row=21)
                 budget_btn3.grid(column=1 , row=22)
                 BTLuxury.grid(column=1,row=23)
                 
                 value = 1
       else:
                pass

value1 = 2
def selecting_10hatchback():
       global value1
       value1 -= 1
       if value1 == 1:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 L = ('''                  Top Hatchback style cars under Rs. 10 Lakh
1. Maruti Suzuki
         Specifications-->  Price: 5.85 - 8.67 Lakh
                          ARAI Mileage is 23.76 kmpl
                          Engine Displacement 1197cc
                          Max Power(bhp@rpm) 88.50bhp@6000rpm
                          Seating Capacity  5 people
                          Boot Space  268L
                          Fuel Type: Petrol
                          Fuel Tank Capacity is 37.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years) is Rs.4,703
                          
 *******************************************************************************  
                         
2. Maruti Baleno
        Specifications-->Price: Rs.5.98 - 9.44 Lakh
                         ARAI Mileage: 19.56 kmpl
                         Engine Displacement: 1197cc
                         Max Power(bhp@rpm): 81.80bhp@6000rpm
                         Seating Capacity: 5
                         Boot Space: 339L
                         Fuel Type: Petrol
                         Fuel Tank Capacity 37.0L
                         Transmission Type: Automatic
                         Service Cost (Avg. of 5 years) Rs.3,656
                         
 *******************************************************************************
                         
3. Hyundai i20
        Specifications--->Price: Rs.6.91 - 11.40 Lakh
                          ARAI Mileage: 20.28 kmpl
                          Engine Displacement: 998cc
                          Max Power(bhp@rpm): 118.36bhp@6000rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 311 
                          Fuel Type: Petrol 
                          Fuel Tank Capacity: 37.0 
                          Transmission Type: Automatic 
                          Service Cost (Avg. of 5 years) Rs.2,882
                          
 *******************************************************************************
 
4. Tata Altroz
        Specifications--->Price: Rs.5.89 - 9.64 Lakh
                          ARAI Mileage: 25.11 kmpl
                          Engine Displacement: 1497cc
                          Max Power(bhp@rpm): 88.77bhp@4000rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 345
                          Fuel Type: Diesel 
                          Fuel Tank Capacity: 37.0 
                          Transmission Type: Automatic 
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************
              
5. Maruti Celerio 
        Specifications--->Price: Rs.5.89 - 9.64 Lakh
                          ARAI Mileage: 26.68 kmpl
                          Engine Displacement: 998 cc
                          Max Power(bhp@rpm): 65.71bhp@5500rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 313
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 32.0 
                          Transmission Type: Automatic 
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************
 
 6.Renault KWID
         Specifications--->Price: Rs.4.24 - 5.80 Lakh
                          ARAI Mileage: 22.0 kmpl
                          Engine Displacement: 999cc
                          Max Power(bhp@rpm): 67bhp@5500rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 279
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 28 L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.2,125

 *******************************************************************************

7.Mahindra KUV100 NXT
        Specifications--->Price: Rs.6.15 - 7.81 Lakh
                          ARAI Mileage: 18.15 kmpl
                          Engine Displacement: 1198
                          Max Power(bhp@rpm): 82bhp@5500rpm
                          Seating Capacity: 6
                          Boot Space (Litres): 243
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 35 L
                          Transmission Type: Manual
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************

8.Hyundai Grand i10 Nios
        Specifications--->Price: Rs.5.29 - 8.51 Lakh
                          ARAI Mileage: 26.2 kmpl 
                          Engine Displacement: 1186cc
                          Max Power(bhp@rpm):73.97bhp@4000rpm
                          Seating Capacity:5
                          Boot Space (Litres): 260 
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 37 L
                          Transmission Type: Manual
                          Service Cost (Avg. of 5 years): Rs.3,625
   
 *******************************************************************************

9.TATA Tiago NRG
        Specifications--->Price: Rs.6.62 - 7.17 Lakh
                          ARAI Mileage: 15.0 kmpl
                          Engine Displacement: 1199cc
                          Max Power(bhp@rpm): 84.48bhp@6000rpm
                          Seating Capacity:5
                          Boot Space (Litres): 242 
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 35 L 
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown  
   
 *******************************************************************************

10.Datsun GO
        Specifications--->Price:Rs.4.02 - 6.51 Lakh*
                          ARAI Mileage: 19.59 kmpl
                          Engine Displacement: 1198cc
                          Max Power(bhp@rpm): 76.43bhp@6000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 265
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 35.0 L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.6,240
                                                                       

                          
 ''')
                 print(L)
                 BTunder10HB.grid(column=1, row=20)
                 BTunder10Sedan.grid(column=1, row=21)
                 BTunder10SUV.grid(column=1, row=22)
                 budget_btn.grid(column=1 , row=2)
                 budget_btn1.grid(column=1, row=3)
                 budget_btn3.grid(column=1, row=4)
                 BTLuxury.grid(column=1,row=5)
                 
                 global text_box
                 text_box = tk.Text(root, height=45, width=80, padx=15, pady=15)
                 text_box.insert(1.0,L) 
                 text_box.grid(column=4 ,row=0, columnspan=10, rowspan=7,)
                 text_box.config(state=DISABLED)
                 value1 = 2
       else:
               pass

value3 = 3
def selecting_10SUV():
       global value3
       value3 -= 1
       if value3 == 2:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 R = ('''                  Top 10 SUV Cars Under Rs.10 Lakh

1.TATA Punch 
        Specifications--->Price:Rs.5.64 - 8.98 Lakh
                          ARAI Mileage: 18.82kmpl 
                          Engine Displacement:1199cc
                          Max Power(bhp@rpm):84.48bhp@6000rpm
                          Seating Capacity:5
                          Boot Space (Litres): 366 L
                          Fuel Type:Petrol
                          Fuel Tank Capacity: 37.0 L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years):Unknown

 *******************************************************************************

2.TATA Nexon
        Specifications--->Price:Rs.7.39 - 13.34 Lakh
                          ARAI Mileage: 21.5kmpl
                          Engine Displacement:1499cc
                          Max Power(bhp@rpm): 108.5bhp@4000rpm
                          Seating Capacity:5
                          Boot Space (Litres): 350L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 44.0 L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years):Rs.4,447
                          
 *******************************************************************************
 
3.Maruti Vitara Brezza
        Specifications--->Price:Rs.7.69 - 11.34 Lakh
                          ARAI Mileage: 18.76 kmpl
                          Engine Displacement: 1462
                          Max Power(bhp@rpm): 103.26bhp@6000rpm
                          Seating Capacity:5
                          Boot Space (Litres): 328 L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 48.0 L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.6,619
                          
 *******************************************************************************

4.Hyundai Venue
        Specifications--->Price:Rs.6.99 - 11.87 Lakh
                          ARAI Mileage: 18.15 kmpl
                          Engine Displacement: 998cc
                          Max Power(bhp@rpm):118.35bhp@6000rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 350 L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 45.0 L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.2,837 
                          
 *******************************************************************************

5.Mahindra XUV 300
        Specifications--->Price: Rs.8.16 - 13.67 Lakh
                          ARAI Mileage: 20.0 kmpl  
                          Engine Displacement: 1497cc
                          Max Power(bhp@rpm):115bhp@3750rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 259 L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 42.0 L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years):Unknown
                          
 *******************************************************************************

6.Kia Sonet 
        Specifications--->Price: Rs.6.95 - 13.69 Lakh
                          ARAI Mileage: 19.0 kmpl
                          Engine Displacement: 1493cc
                          Max Power(bhp@rpm): 113.42bhp@4000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 392 L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 45.0 L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.3,980

                          
 *******************************************************************************
 
7. Nissan Magnite
        Specifications--->Price: Rs.5.76 - 10.15 Lakh
                          ARAI Mileage: 17.7kmpl
                          Engine Displacement: 999cc
                          Max Power(bhp@rpm):98.63bhp@5000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 336L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 40.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown

 *******************************************************************************

8.Renault Kiger
        Specifications--->Price:Rs.5.79 - 10.22 Lakh
                          ARAI Mileage: 20.53 kmpl
                          Engine Displacement:999 cc
                          Max Power(bhp@rpm): 98.63bhp@5000rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 405 L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 40.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************

9.Maruti S-Cross
        Specifications--->Price: Rs.8.80 - 12.77 Lakh
                          ARAI Mileage: 18.55 kmpl
                          Engine Displacement: 1462cc
                          Max Power(bhp@rpm):103.26bhp@6000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 375L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 48.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************

10.Honda WR-V
        Specifications--->Price: Rs.8.82 - 11.86 Lakh
                          ARAI Mileage: 23.7 kmpl
                          Engine Displacement: 1498 cc
                          Max Power(bhp@rpm): 97.89bhp@3600rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 363L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 40.0L
                          Transmission Type: Manual
                          Service Cost (Avg. of 5 years): Unknown
 *******************************************************************************
''')
                 print(R)
                 
                 BTunder10HB.grid(column=1, row=20)
                 BTunder10Sedan.grid(column=1, row=21)
                 BTunder10SUV.grid(column=1, row=22)
                 budget_btn.grid(column=1 , row=2)
                 budget_btn1.grid(column=1, row=3)
                 budget_btn3.grid(column=1, row=4) 
                 BTLuxury.grid(column=1,row=5)
                   
                 global text_box
                 text_box = tk.Text(root, height=45, width=80, padx=15, pady=15)
                 text_box.insert(1.0,R) 
                 text_box.grid(column=4 ,row=0, columnspan=10, rowspan=7,)
                 text_box.config(state=DISABLED)
                 
                 value3 = 3
       else:
               pass

value4 = 4
def selecting_10Sedan():
       global value4
       value4 -= 1
       if value4 == 3:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 
                 _10Sedan = ('''                  Top 10 Sedan Cars Under Rs.10 Lakh

1. Maruti Dzire
        Specifications--->Price: Rs.6.09 - 9.13 Lakh
                          ARAI Mileage: 24.12 kmpl 
                          Engine Displacement: 1197 cc
                          Max Power(bhp@rpm): 88.50bhp@6000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 378L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 37.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.3,546/yr

 *******************************************************************************

2.Honda City 4th Generation
        Specifications--->Price: Rs.9.29 - 9.99 Lakh
                          ARAI Mileage: 17.4 kmpl
                          Engine Displacement: 1497 cc
                          Max Power(bhp@rpm): 117.60bhp@6600rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 510L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 40.0:L
                          Transmission Type: Manual
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************
 
3.Tata Tigor
        Specifications--->Price:Rs.5.79 - 8.41 Lakh
                          ARAI Mileage: 20.3 kmpl
                          Engine Displacement: 1199cc
                          Max Power(bhp@rpm): 72.40bhp@6000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 419L
                          Fuel Type: CNG
                          Fuel Tank Capacity: 60.0L
                          Transmission Type: Manual
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************

4.Honda Amaze
        Specifications--->Price: Rs.6.38 - 11.21 Lakh
                          ARAI Mileage: 24.7 kmpl
                          Engine Displacement: 1498 cc
                          Max Power(bhp@rpm): 79.12bhp@3600rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 420L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 35.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************

5.Hyundai Aura
        Specifications--->Price: Rs.5.99 - 9.37 Lakh
                          ARAI Mileage: 25.4kmpl
                          Engine Displacement: 1197cc
                          Max Power(bhp@rpm): 73.97bhp@4000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 402L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 37.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.3,582/yr
                          
 *******************************************************************************

6. Maruti Ciaz
        Specifications--->Price: Rs.8.87 - 11.86 Lakh
                          ARAI Mileage: 20.65 kmpl
                          Engine Displacement: 1462 cc
                          Max Power(bhp@rpm): 103.25bhp@6000rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 510L
                          Fuel Type: Petrol 
                          Fuel Tank Capacity: 13.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.3,689/y
                          
 *******************************************************************************
 
7. Hyundai Xcent Prime
        Specifications--->Price: Rs.6.40 - 7.25 Lakh
                          ARAI Mileage: 15.38 kmpl
                          Engine Displacement: 1197 cc
                          Max Power(bhp@rpm): 65.39bhp@5600rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 407L
                          Fuel Type: CNG
                          Fuel Tank Capacity: 65.0L
                          Transmission Type: Manual
                          Service Cost (Avg. of 5 years): Unknown

 *******************************************************************************

8.Hyundai Verna
        Specifications--->Price: Rs.9.32 - 15.36 Lakh
                          ARAI Mileage: 25.0 kmpl
                          Engine Displacement: 1497cc
                          Max Power(bhp@rpm): 113.42bhp@4000rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 480L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 45.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.3,967

                          
 *******************************************************************************

9.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

10.
        Specifications--->Price: 
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
 *******************************************************************************
                       
 ''')
                 print(_10Sedan)
                 
                 BTunder10HB.grid(column=1, row=20)
                 BTunder10Sedan.grid(column=1, row=21)
                 BTunder10SUV.grid(column=1, row=22)
                 budget_btn.grid(column=1 , row=2)
                 budget_btn1.grid(column=1, row=3)
                 budget_btn3.grid(column=1, row=4)  
                 BTLuxury.grid(column=1,row=5)
                 
                 global text_box
                 text_box = tk.Text(root, height=45, width=80, padx=15, pady=15)
                 text_box.insert(1.0,_10Sedan) 
                 text_box.grid(column=4 ,row=0, columnspan=10, rowspan=7,)
                 text_box.config(state=DISABLED)
                 
                 value4 = 4
       else:
               pass
               
#20lakh
value = 1
def change_value1():
       global value
       value -= 1
       if value == 0:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1,)
                 budget_btn3.grid(column=1 , row=40)
                 budget_btn.grid(column=1,row=40)
                 BTunder20SUV.grid(column=1, row=3)
                 BTunder20Sedan.grid(column=1, row=4)
                 BTLuxury.grid(column=1,row=23)
                 
                 value = 1
       else:
                pass 


#UNDER 20 SUV
value6 = 6        
def selecting_20SUV():
        global value6
        value6 -= 1
        if value6 == 5:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 _20Suv = ('''                  Top 10 SUV Cars Under Rs.20 Lakh

1.Mahindra Thar 
        Specifications--->Price: Rs.13.17 - 15.53 Lakh
                          ARAI Mileage: 15.2 kmpl
                          Engine Displacement: 2184 cc
                          Max Power(bhp@rpm): 130bhp@3750rpm
                          Seating Capacity: 4 
                          Boot Space (Litres): 600L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 57.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown

 *******************************************************************************

2.Tata Harrier
        Specifications--->Price: Rs.14.49 - 21.34 Lakh
                          ARAI Mileage: 17.0 kmpl
                          Engine Displacement: 1956 cc
                          Max Power(bhp@rpm): 167.63bhp@3750rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 425L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 50.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************
 
3.Mahindra XUV700
        Specifications--->Price: Rs.12.95 - 23.79 Lakh
                          ARAI Mileage: 17.0kmpl
                          Engine Displacement: 2198 cc
                          Max Power(bhp@rpm): 182.38bhp@3500rpm
                          Seating Capacity: 5-7
                          Boot Space (Litres):  425L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 60.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************

4.Mahindra Scorpio
        Specifications--->Price: Rs.13.18 - 18.14 Lakh
                          ARAI Mileage: 15.0kmpl
                          Engine Displacement: 2179 cc
                          Max Power(bhp@rpm): 140bhp@3750rpm
                          Seating Capacity: 7-9
                          Boot Space (Litres): 460L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 60.0L
                          Transmission Type: Manual
                          Service Cost (Avg. of 5 years): Rs.3,794/yr
                          
 *******************************************************************************

5.Hyundai Creta
        Specifications--->Price: Rs.10.23 - 17.94 Lakh
                          ARAI Mileage: 21.4 kmpl
                          Engine Displacement: 1497 cc
                          Max Power(bhp@rpm): 138.08bhp@6000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 433L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 50.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.3,225/yr
                          
 *******************************************************************************

6.Kia Seltos
        Specifications--->Price:Rs.9.95 - 18.19 Lakh
                          ARAI Mileage: 20.8 kmpl
                          Engine Displacement:1497 cc
                          Max Power(bhp@rpm): 113.43bhp@4000rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 433L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 50.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.4,628/yr
                          
 *******************************************************************************
 
7.MG Hector 
        Specifications--->Price:Rs.13.94 - 19.90 Lakh
                          ARAI Mileage: 13.5kmpl
                          Engine Displacement: 1956 cc
                          Max Power(bhp@rpm): 167.68bhp@3750rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 587L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 60.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.6,019/yr

 *******************************************************************************

8.Hyundai Alcazar
        Specifications--->Price: Rs.16.34 - 20.14 Lakh
                          ARAI Mileage: 18.4 kmpl
                          Engine Displacement: 1999 cc
                          Max Power(bhp@rpm): 113.45bhp@4000rpm
                          Seating Capacity: 6-7
                          Boot Space (Litres): 180L
                          Fuel Type: Diesel
                          Fuel Tank Capacity: 50.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Rs.3,731/yr
                          
 *******************************************************************************

9.Skoda Kushaq
        Specifications--->Price:Rs.10.99 - 18.19 Lakh
                          ARAI Mileage: 17.95 kmpl 
                          Engine Displacement: 1498cc
                          Max Power(bhp@rpm):147.51bhp@5000-6000rpm
                          Seating Capacity: 5
                          Boot Space (Litres): 385L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 50.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown
                          
 *******************************************************************************

10.MG Astor
        Specifications--->Price: Rs.9.98 - 17.72 Lakh
                          ARAI Mileage: 11.5kmpl
                          Engine Displacement: 1498 cc
                          Max Power(bhp@rpm): 138.08bhp@5600rpm
                          Seating Capacity: 5 
                          Boot Space (Litres): 448L
                          Fuel Type: Petrol
                          Fuel Tank Capacity: 45.0L
                          Transmission Type: Automatic
                          Service Cost (Avg. of 5 years): Unknown
 *******************************************************************************
                       
 ''')           
                 print(_20Suv)
                 
                
                 BTunder20SUV.grid(column=1, row=21)
                 BTunder20Sedan.grid(column=1, row=22)
                 budget_btn.grid(column=1 , row=2)
                 budget_btn1.grid(column=1, row=3)
                 budget_btn3.grid(column=1, row=4)
                 BTLuxury.grid(column=1, row=5)
                 
                 global text_box
                 text_box = tk.Text(root, height=45, width=80, padx=15, pady=15)
                 text_box.insert(1.0,_20Suv) 
                 text_box.grid(column=4 ,row=0, columnspan=10, rowspan=7,)
                 text_box.config(state=DISABLED)
                 value6=6     
        else:
                pass

#UNDER 20 SEDAN
value7 = 7
def selecting_20Sedan():
        global value7
        value7 -= 1
        if value7 == 6:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 _20Sedan = ('''                  Top 10 Sedan Cars Under Rs.20 Lakh

1. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

2.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
3.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

4.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
                          
 *******************************************************************************

5.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

6. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
7. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

8.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

9.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

10.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
 *******************************************************************************
                       
 ''')           

                 print(_20Sedan)
                 
                
                 BTunder20SUV.grid(column=1, row=21)
                 BTunder20Sedan.grid(column=1, row=22)
                 budget_btn.grid(column=1 , row=2)
                 budget_btn1.grid(column=1, row=3)
                 budget_btn3.grid(column=1, row=4)
                 BTLuxury.grid(column=1,row=5)
                 
                 
                 global text_box
                 text_box = tk.Text(root, height=45, width=80, padx=15, pady=15)
                 text_box.insert(1.0,_20Sedan) 
                 text_box.grid(column=4 ,row=0, columnspan=10, rowspan=7,)
                 text_box.config(state=DISABLED) 
                 
                 value7=7    
        else:
                pass                
                
                
                

##SELECTING BUDGET 30 LAKH
value = 1
def change_value2():
       global value
       value -= 1
       if value == 0:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 budget_btn.grid(column=1, row=21)
                 budget_btn1.grid(column=1, row=22)
                 budget_btn3.grid(column=1, row=23)
                 BTLuxury.grid(column=1,row=24)
                 BTunder30SUV.grid(column=1 ,row=3)
                 BTunder30Sedan.grid(column=1, row=4)
                 
                 
                 value = 1
       else:
                pass 

#UNDER 30 SUv
value = 1
def selecting_30SUV():
        global value
        value -= 1
        if value == 0:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 _30Suv = ('''                  Top 10 SUV Cars Under Rs.30 Lakh

1. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

2.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
3.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

4.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
                          
 *******************************************************************************

5.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

6. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
7. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

8.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

9.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

10.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
 *******************************************************************************
                       
 ''')           

                 print(_30Suv)
                 
                 BTunder30SUV.grid(column=1, row=21)
                 BTunder30Sedan.grid(column=1, row=22)
                 budget_btn.grid(column=1 , row=2)
                 budget_btn1.grid(column=1, row=3)
                 budget_btn3.grid(column=1, row=4)
                 BTLuxury.grid(column=1,row=5)
                 
                 global text_box
                 text_box = tk.Text(root, height=45, width=80, padx=15, pady=15)
                 text_box.insert(1.0,_30Suv) 
                 text_box.grid(column=4 ,row=0, columnspan=10, rowspan=7,)
                 text_box.config(state=DISABLED)
                 
                 value = 1
                 
        else:
                pass 

#UNDER 30 Sedan
value = 1
def selecting_30Sedan():
        global value
        value -= 1
        if value == 0:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 _30Sedan = ('''                  Top 10 Sedan Cars Under Rs.30 Lakh

1. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

2.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
3.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

4.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
                          
 *******************************************************************************

5.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

6. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
7. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

8.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

9.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

10.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
 *******************************************************************************
                       
 ''')           

                 print(_30Sedan)
                 
                 BTunder30SUV.grid(column=1, row=21)
                 BTunder30Sedan.grid(column=1, row=22)
                 budget_btn.grid(column=1 , row=2)
                 budget_btn1.grid(column=1, row=3)
                 budget_btn3.grid(column=1, row=4)
                 BTLuxury.grid(colum=1,row=5)
                 
                 global text_box
                 text_box = tk.Text(root, height=45, width=80, padx=15, pady=15)
                 text_box.insert(1.0,_30Sedan) 
                 text_box.grid(column=4 ,row=0, columnspan=10, rowspan=7,)
                 text_box.config(state=DISABLED)
                 
                 value = 1
                 
        else:
                pass
      
value = 1
def selecting_Luxury():
        global value
        value -= 1
        if value == 0:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 Luxury = ('''                  Top 10 Luxury Cars To Buy After Selling Your Kidney

1. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

2.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
3.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

4.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
                          
 *******************************************************************************

5.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

6. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
7. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

8.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

9.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

10.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
 *******************************************************************************
                       
 ''')           

                 print(Luxury)
                 
                 BTunder30SUV.grid(column=1, row=21)
                 BTunder30Sedan.grid(column=1, row=22)
                 budget_btn.grid(column=1 , row=2)
                 budget_btn1.grid(column=1, row=3)
                 budget_btn3.grid(column=1, row=4)
                 BTLuxury.grid(column=1,row=5)
                 
                 
                 global text_box
                 text_box = tk.Text(root, height=45, width=80, padx=15, pady=15)
                 text_box.insert(1.0,Luxury) 
                 text_box.grid(column=4 ,row=0, columnspan=10, rowspan=7,)
                 text_box.config(state=DISABLED)
                 
                 value = 1
                 
        else:
                pass 

#UNDER 30 Sedan
value = 1
def selecting_30Sedan():
        global value
        value -= 1
        if value == 0:
                 logo_label.grid(column=1, row=0)
                 instructions.grid(columnspan=3, column=0, row=1)
                 Luxury = ('''                  Top 10 Sedan Cars Under Rs.30 Lakh

1. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

2.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
3.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

4.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
                          
 *******************************************************************************

5.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

6. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************
 
7. 
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):

 *******************************************************************************

8.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

9.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years):
                          
 *******************************************************************************

10.
        Specifications--->Price:
                          ARAI Mileage: 
                          Engine Displacement:
                          Max Power(bhp@rpm):
                          Seating Capacity:
                          Boot Space (Litres):
                          Fuel Type:
                          Fuel Tank Capacity:
                          Transmission Type:
                          Service Cost (Avg. of 5 years): 
 *******************************************************************************
                       
 ''')           

                 print(Luxury)
                 
                 
                 
                 value = 1
        else:
                pass                                         
#BUDGET Rs.10 LAKH
budget_text = tk.StringVar()
budget_btn = tk.Button(root, textvariable=budget_text, command=lambda:change_value(), font = 'Algerian', bg='black', fg='White', height=2, width=30)
budget_text.set("Cars Under Rs.10 Lakh")
budget_btn.grid(column=1 , row=2)


#selecting Category
#Under 10 Lakh Hatchback 
BTunder10HBtext = tk.StringVar()
BTunder10HB = tk.Button(root, textvariable=BTunder10HBtext, command=lambda:selecting_10hatchback(), font = 'Algerian', bg='black', fg='White', height=2, width=30)
BTunder10HBtext.set("Hatchback")

#UNDER 10 LAKh SUV
BTunder10SUVtext = tk.StringVar()
BTunder10SUV = tk.Button(root, textvariable=BTunder10SUVtext, command=lambda:selecting_10SUV(), font = 'Algerian', bg='black', fg='White', height=2, width=30)
BTunder10SUVtext.set("SUV")

#Under 10 Lakh Sedan
BTunder10Sedantext = tk.StringVar()
BTunder10Sedan = tk.Button(root, textvariable=BTunder10Sedantext, command=lambda:selecting_10Sedan(), font = 'Algerian', bg='black', fg='White', height=2, width=30)
BTunder10Sedantext.set("Sedan")
####################################################################################################################################################################



#BUDGET Rs.20 LAKH
budget_text1 = tk.StringVar()
budget_btn1 = tk.Button(root, textvariable=budget_text1, command=lambda:change_value1(), font = 'Algerian', bg='black', fg='White', height=2, width=30)
budget_text1.set("Cars Under Rs.20 Lakh")
budget_btn1.grid(column=1 , row=3)

#Under 20 Lakh SUV 
BTunder20SUVtext = tk.StringVar()
BTunder20SUV = tk.Button(root, textvariable=BTunder20SUVtext, command=lambda:selecting_20SUV(), font = 'Algerian', bg='Orange', fg='Black', height=2, width=30)
BTunder20SUVtext.set("SUV")

#UNDER 20 Lakh Sedan
BTunder20Sedantext = tk.StringVar()
BTunder20Sedan = tk.Button(root, textvariable=BTunder20Sedantext, command=lambda:selecting_20Sedan(), font = 'Algerian', bg='Orange', fg='Black', height=2, width=30)
BTunder20Sedantext.set("Sedan")
#####################################################################################################################################################################



#BUDGET Under 30 Lakh
budget_text3 = tk.StringVar()
budget_btn3 = tk.Button(root, textvariable=budget_text3, command=lambda:change_value2(), font = 'Algerian', bg='black', fg='White', height=2, width=30)
budget_text3.set("Cars Under Rs.30 Lakh")
budget_btn3.grid(column=1 , row=4)

#Under 30 SUV
BTunder30SUVtext = tk.StringVar()
BTunder30SUV = tk.Button(root, textvariable=BTunder30SUVtext, command=lambda:selecting_30SUV(), font = 'Algerian', bg='#3776ab', fg='Black', height=2, width=30)
BTunder30SUVtext.set("SUV")

#Under 30 Sedan
BTunder30Sedantext = tk.StringVar()
BTunder30Sedan = tk.Button(root, textvariable=BTunder30Sedantext, command=lambda:selecting_30Sedan(), font = 'Algerian', bg='#3776ab', fg='Black', height=2, width=30)
BTunder30Sedantext.set("Sedan")

#BUDGET Under 30 - ~
BTLuxurytext = tk.StringVar()
BTLuxury = tk.Button(root, textvariable=BTLuxurytext, command=lambda:selecting_Luxury(), font = 'Algerian', bg='Black', fg='White', height=2, width=30)
BTLuxurytext.set("Luxury Cars")
BTLuxury.grid(column=1,row=5)


canvas = tk.Canvas(height=400, width=250)
canvas.grid(columnspan=3)


root.mainloop()