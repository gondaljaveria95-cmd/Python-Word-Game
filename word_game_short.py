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
        
    attempt = attempt +1
    print ("Attempts Left:", 6 - attempt)
    if attempt == 6: 
        print ("Game Over!")
        