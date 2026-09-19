secret_word = "apple"

attempt = 0
while attempt < 6:
    guess  =input("Guess the word:").lower()
    
    if len(guess) != len(secret_word):
       print ("Please enter 5 letters word.")
       continue                       #continue loop k curent iteration ko rok k next iteration start kr deta haiapp
    
    if guess == secret_word:
        print("This is your answer.")
        break
    else:
        print("Your guess is wrong!")
        
    for letter in guess:
        if letter in secret_word:
            print(letter,"is present!")
        else:
            print(letter, "is not present")
            
    for index,letter in enumerate(guess):
        if letter == secret_word[index]:                 #same position
            print(letter, "Correct Position")
        elif letter in secret_word:                      #letter present in word but not same postion
            print(letter, "Wrong Position")
        else:                                           #letter is not presnet
            print (letter, "is not present")
        
    attempt = attempt +1
    print ("Attempts Left:", 6 - attempt)
    if attempt == 6: 
        print ("Game Over!", "Coorect Word was : ", secret_word)
    
    
#print(guess)