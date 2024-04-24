# PROGRAM TO MAKE A SIMPLE GAME .
print('Hello, welcome to trival')

ans=input('Are you ready to play (YES/NO):')
score=0
total_q=4


if ans.lower() == 'yes':
    ans=input('1. What is the best programmming language?')
    if ans.lower() == 'python':
        score+=1
        print('correct')

    else:
        print('Incorrect')
        
    ans=input('2. what is 2+8+9-1?')
    if ans=='18':
        score+=1
        print('correct')

    else:
        print('Incorrect')

    
    ans=input('3. What is  better a 1050ti or 1060 (graphics card)?')
    if ans.lower() == '1050ti':
        score+=1
        print('correct')

    else:
        print('Incorrect')

        
    ans=input('4. Who came second in the stanely cup finals?')
    if ans.lower() == 'nights' or  ans.lower() == 'vegas':
        score+=1
        print('correct')

    else:
        print('Incorrect')

print('Thank you for playing, you got', score, "question correct.")
mark = (score/total_q) * 100

print("Mark: " , mark)
print("GOODBYE")

        
        
        
