# Proyecto modulo 2

x= int (input("Enter the value of x: "))
y= int (input ("Enter the value of y: "))

# Ninguna coordenada deberà tener valor de cero

if x==0 and y ==0:
    print("The values entered must be greater than zero")

# Identificar en què nùmero de cuadrante se encuentran las coordenadas

if x>0 and y>0:
    print ("You are in the quadrant I")

if x<0 and y>0:
    print ("You are in the quadrant II")

if x<0 and y<0:
    print ("You are in the quadrant III")

if x>0 and y<0:
    print ("You are in the quadrant IV")
    
