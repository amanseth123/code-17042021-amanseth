import json
fileName='data.json' # or we could use input() to directly ask the user to input the file 
f = open(fileName, "r")  # opening then file in read mode  
#f = open("data2.json","r")
if f.closed==False: # if file is open, then perform the task
    data = f.read() # reading the file and storing the data in data variable
    try:
        jsonObj = json.loads(data) # loading the data
        length=len(jsonObj) # calculating the length of the file 
        def BMI(height,weight): # BMI function to calculate and return BMI given weight and height as parameters
            if type(height) not in [int,float] or type(weight) not in [int,float]: # avoiding string type input
                raise TypeError("Height and weight must be non-negative real number ")
            if height==0 or weight==0: # avoiding zero division and infinite values 
                raise ZeroDivisionError("Height or weight cannot be Zero")
            if height<0: # checking for negative values
                raise ValueError("Height cannot be negative")
            return weight/(height**2) # finally return the answer 
        def BMICategory(bmi,totalOverweight): # function to calculare BMI category given the bmi as input parameter
            # as per the bmi formula bmi category is being calculated below 
            if bmi<=18.4:
                return 'Underweight'
            elif 18.5<=bmi<=24.9:
                return 'Normal weight'
            elif 25<=bmi<=29.9:
                totalOverweight+=1
                return 'Overweight'
            elif 30<=bmi<=34.9:
                return 'Moderately Obese'
            elif 35<=bmi<=39.9:
                return 'Severely Obese'
            elif bmi>=40:
                return 'Very Severely Obese'
            return 'Not Found' # return not found catgeory when the input doesn't matches with any category

        def Healthrisk(bmiCategory): # calculating the health risk using the bmi category
            # using the data calculating the health risk 
            if bmiCategory=='Underweight':
                return 'Malnutrition'
            elif bmiCategory=='Normal weight':
                return 'Low risk'
            elif bmiCategory=='Overweight':
                return 'Enhanced Risk'
            elif bmiCategory=='Moderately Obese':
                return 'Medium Risk'
            elif bmiCategory=='Severely Obese':
                return 'High Risk'
            elif bmiCategory=='Very Severely Obese':
                return 'Very High Risk'
            else:
                return 'Invalid' # returning invalid when invalid data is feed
        totalOverweight=0 # variable to store total number of overweight people from the data
        for row in range(length): # going through each row in the data file, time complexity O(length) 
            #gender=jsonObj[row]['Gender'] # storing the gender(if required)
            height=jsonObj[row]['HeightCm']/100 # storing the height in m(from cm) in variable height
            weight=jsonObj[row]['WeightKg']# storing the weight in kg in variable weight 
            bmi=BMI(height,weight) # storing the bmi value returned from the BMI()
            bmi=round(bmi,2)
            bmiCategory=BMICategory(bmi,totalOverweight)# storing the BMI category value returned from the BMICategory function
            healthRisk=Healthrisk(bmiCategory)# storing the Health risk value from the Healthrisk function
            # feeding the above values into the data(temporary copy) below
            jsonObj[row]['BMI']=bmi 
            jsonObj[row]['BMI Category']=bmiCategory
            jsonObj[row]['Health Risk']=healthRisk
        try:
            with open(fileName ,'w') as jsonfile: # updating the data file with the new data 
                json.dump(jsonObj, jsonfile, indent=4)
            f.close()# closing the file as all the operations are performed 
        except:
            print("Unable to update the data !") # except block to throw error 
    except :
        print("File could be empty")
else:
    raise FileExistsError





