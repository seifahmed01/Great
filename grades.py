#the list of grades
print('the Grades: (A+ ≥ 90, 90 > A ≥ 85, 85 > B+ ≥ 80, 80 > B ≥ 75, 75 > C+ ≥ 70, 70> C ≥ 65, 65 > D+ ≥ 60, 60 > D ≥ 50)')

#to know the grade 
def grades(grade):
    if grade>=90 :
        print('\nyour grade is: A+')
    elif 90>grade>=85 :
        print('\nyour grade is: A')
    elif 85>grade>=80 :
        print('\nyour grade is: B+')
    elif 80>grade>=75 :
        print('\nyour grade is: B')
    elif 75>grade>=70 :
        print('\nyour grade is: C+')
    elif 70>grade>=65  :
        print('\nyour grade is: C')
    elif 65>grade>=60 :
        print('\nyour grade is: D+')
    elif 60>grade>=50 :
        print('\nyour grade is: D')
    else :
        print('\nyour grade is: F')

#this list if you want to know another grade
list=['yes','no']

while True :
    grade=float(input('\nenter your grade: '))
    if 0<=grade<=100 :
        grades(grade)

        #to know another grade
        New_grade=str(input('\ndo you want to add another grade ? '))
        if New_grade==list[0] :
            continue

        elif New_grade==list[1] :
            print('\nBest All Wishes...')
            break

    #if the grade is invalid
    else :
        print('the grade is invalid please enter a correct grade..!')
        continue


    




    


   