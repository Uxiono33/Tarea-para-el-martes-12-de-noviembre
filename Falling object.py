Acceleration =float(9.8)
mass = float(input('Enter mass in KG:'))
while mass < 0:
    mass = float(input("A positive value for mass is required: "))
    
else :
    Heigh= float(input("Enter the initial heigh:"))
    while Heigh < 0:
         Heigh = float(input("A positive value for height is required: "))
    else : 
        Time_until_the_object_reaches_the_ground=((2*Heigh)/(Acceleration))**((2)**-1)
        Ground_touching_speed=(Time_until_the_object_reaches_the_ground*Acceleration)
        Ground_hitting_force=(Acceleration*mass)
        print('The objet will reach the ground in', Time_until_the_object_reaches_the_ground,'s','It will reach the ground at',Ground_touching_speed,'m/s','The object will hit the ground with',Ground_hitting_force,'N')