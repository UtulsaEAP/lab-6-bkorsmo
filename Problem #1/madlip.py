def food_input():
    
    #type you while  loop here
    while True:
        user_input = input()
        tokens = user_input.split()
        if (user_input != 'quit 0' ):
            print('Eating '+ tokens[1]+ ' ' +tokens[0]+ ' a day keeps you happy and healthy.' )
        else:
            break

            

            
    

if __name__ == "__main__":
    food_input()
