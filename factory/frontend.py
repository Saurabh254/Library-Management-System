
class TermStyles:
    '''
    Class Name: TermStyles
    comprises of different styling attributes
    '''

    homepage = '''
###########################################################
#                                                         #
#              Welcome to Saurabh's Library               #
#                                                         #
# ------------------------------------------------------- #
#  HomePage:                                              #
#                                                         #
#                 1. Login & Signup                       #
#                 2. About Library                        #
#                 3. File a complaint                     #
#                                                         #
# ------------------------------------------------------- #
#                                                         #
#       Use commands: 'q','Q','close','quit' to exit      #
#                                                         #
###########################################################  


Enter Your Choice: '''


    Login_or_Signup_accountName = input('''
##########################################################
#                                                        #
#              Login into Your Account                   #
#                                                        #
# ------------------------------------------------------ #
                                                        
   Enter Account Holder's Name (UserName): ''')
    Login_or_Signup_accountPin = input('''   Enter Account Pin: ''')



print(TermStyles.Login_or_Signup_accountName,TermStyles.Login_or_Signup_accountPin, end="")