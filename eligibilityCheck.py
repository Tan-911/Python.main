#24/12/2025
#This program is used to determine a student whether eligible to join competition based on age, GPA and attendance percentage.

#Main space
#Process & validate input
try:
    age = int(input('Enter your age: ')) #Input
    
    if age <= 0 or age >= 100: #Validate age
        print ('Please enter a valid age.')

    else:
        if age >= 18 and age <= 25: #Determine eligible age

            try:
                GPA = float(input('Enter your GPA: ')) #Input
                
                if GPA < 0.00 or GPA > 4.00:  
                    print ('Please enter a valid GPA.')
                
                else:

                    if GPA >= 3.5: #Determine eligible GPA

                        try:
                            attendance = float(input('Enter your attendance percentage: ')) #Input

                            if attendance < 0.00 or attendance > 100.00:
                                print ('Please enter a valid attendance.')

                            else:
                                if attendance >= 95.0: #Determine eligible attendance
                                    print('You are eligible to join this competition.')
                
                                else: 
                                    print('You are not eligible to join this competition.') 

                        except ValueError:
                            print ('Please enter a numeric value.')      

                    else: 
                        print('You are not eligible to join this competition.')

            except ValueError:
                print ('Please enter a numeric value.')           

        else: 
            print('You are not eligible to join this competition.')    

except ValueError:
    print('Please enter a numeric value.')
                      