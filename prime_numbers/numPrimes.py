
import os
# Program to find prime numbers in a range given by the user.
# Prime numbers are numbers that are divisible by 1 and itself.
os.system('cls')
print('************************************************************************************************')
print('                                 #     #  #######  #       #         ####                       ')
print('                                 #     #  #        #       #       #      #                     ')
print('                                 #######  #######  #       #      #        #                    ')
print('                                 #     #  #        #       #       #      #                     ')
print('                                 #     #  #######  ####### #######   ####                       ')
print('************************************************************************************************')
print('')
print('')
print('')
def numPrimes(): 
    want_to_repeat = 's'
    while(want_to_repeat=='s'):
        print('****************************************************************************************')
        first_num = int(input('Enter the first number in the range to find the prime number:'))
        print('')
        second_num = int(input('Enter the second number in the range to find the prime number:'))
        counter_list=[]
        for index_one in range(first_num,second_num+1):
            if index_one>=1:          
                for ind_two in range(2,index_one):
                    if(index_one%ind_two==0):
                        break
                else:
                #    print(index_one)
                    counter_list.append(index_one)
                #    print(counter_list)
        print('')            
        print('The desired range has {} prime numbers!'.format(len(counter_list)))
            
        want_to_repeat=input('Would you like to continue? s/ Yes ou n/ Not ')
        if want_to_repeat!='s':
            print('Thanks for using our services!')

numPrimes()

