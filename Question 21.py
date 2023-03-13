def hostpital_speciality(cases_list):
    speciality =[]
    temp_list = cases_list
    
    for item in cases_list:
    
        try:
            cases_list.remove(int(item))
        except ValueError:
            pass
    P=0
    O=0
    E=0        
    for item in cases_list:
        # print(item)
        if item == 'P':
            P=P+1
        elif item == 'O':
            O=O+1
        elif item == 'E':
            E=E+1

    Dict={'P':'Pediatrics','O':'Orthopedics','E':'ENT'}
    
    if P>O and P>E:
        print(Dict['P'])
    elif O>P and O>E:
        print(Dict['O'])
    elif E>P and E>O:
        print(Dict['E'])

    

no_of_cases=int(input("Enter the number of cases:- "))
cases_list = []

for i in range(no_of_cases):
    
    no_of_patients = int(input("Enter the number of patients: "))
    cases_list.append(no_of_patients)
    medical_speciality=input("Enter the speciality:- ")
    cases_list.append(medical_speciality)

# print(max(cases_list))
hostpital_speciality(cases_list)

