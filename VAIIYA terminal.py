from ctypes import wintypes
import time
import os
from prompt_toolkit.shortcuts import ProgressBar
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import message_dialog
from prompt_toolkit.shortcuts import yes_no_dialog
from prompt_toolkit.shortcuts import input_dialog
import time
import bcrypt
from datetime import datetime
from prompt_toolkit import print_formatted_text, HTML

#changes the size of the Command promp so it is easyer to read (and that the ASCII doesnt soft wrap)

def window_resize_startup():
#put the CMD reisze code here, this is disabled for the tiem being 
    CMD = "mode 1000,1000"
    os.system(CMD)




#NOTE: THERE MAY BE MINOR LINE WRAP IN THE ASCII

# Loading screen with VAIIYA SECURITY ASCII Art
def startup_screen_ASCII():
    print(r"""

 
                                             __________   __________
                                             \|||||||||\ \::::::::::\
                                              \|||||||||\ \::::::::::\
                                               \|||||||||\ \::::::::::\
                                                \|||||||||\ \::::::::::\
\-------\             /--------/  /-------\  \--------\  \--------\  \--------\           /---------/  /-------\
 \.......\           /......../  /.........\  \........\  \........\  \........\         /........./  /.........\
  \.......\         /......../  /...........\  \........\  \........\  \........\       /........./  /...........\
   \.......\       /......../  /.............\  \........\  \........\  \........\     /........./  /.............\
    \.......\     /......../  /......__.......\  \........\  \........\  \........\   /........./  /...............\
     \.......\   /......../  /....../  \.......\  \........\  \........\  \........\_/........./  /......./  \......\
      \.......\ /......../  /....../    \.......\  \........\  \........\  \................../  /......./    \......\
       \................/  /....../      \.......\  \........\  \........\  \................/  /......./      \......\
        \............../  /....../        \.......\  \........\  \........\  \............../  /......./        \......\
         \............/  /....../          \.......\  \........\  \........\  \............/  /......./          \......\
          \........../  /....../            \.......\  \........\  \........\  \........../  /......./            \......\
                                                                               /........./
                                                                              /........./
                                                                             /........./
                                                                            /........./
                                                                           /---------/
                                                    VAIIYA technologies LLC
                                            Empowering security, one byte at a time.

                                            
                                    please wait while the program does mandatory checks.
    """)
#title stuff for new loadin screen 

def loading_bars_intro_1():

    title = HTML('Connecting to the VAIIYA Defender framework....')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(300), label=label):
            time.sleep(.01)
    time.sleep(1)
    
    print("connection: approved")
    time.sleep(0.3)

def loading_bars_intro_2():

    title = HTML('Checking root for verification codes....')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(215), label=label):
            time.sleep(.01)
    time.sleep(1)
    
    print("codes found! checking with system.... approved!")
    time.sleep(0.2)

def loading_bars_intro_3():

    title = HTML('Sending system logs and debug info for system approval')
    label = HTML('')

    # loading screen system with prompTK
    with ProgressBar(title=title) as pb:
        for i in pb(range(175), label=label):
            time.sleep(.01)
    time.sleep(1)
    
    print("sending logs.... approved! sending debug... approved! ")
    time.sleep(0.3)
    
    
    print("All connections approved! opening VAIIYA terminal....")
    time.sleep(0.7)

# Display main menu
def main_menu():
    print(r"""
                                             __________   __________
                                             \|||||||||\ \::::::::::\
                                              \|||||||||\ \::::::::::\
                                               \|||||||||\ \::::::::::\
                                                \|||||||||\ \::::::::::\
\-------\             /--------/  /-------\  \--------\  \--------\  \--------\           /---------/  /-------\
 \.......\           /......../  /.........\  \........\  \........\  \........\         /........./  /.........\
  \.......\         /......../  /...........\  \........\  \........\  \........\       /........./  /...........\
   \.......\       /......../  /.............\  \........\  \........\  \........\     /........./  /.............\
    \.......\     /......../  /......__.......\  \........\  \........\  \........\   /........./  /...............\
     \.......\   /......../  /....../  \.......\  \........\  \........\  \........\_/........./  /......./  \......\
      \.......\ /......../  /....../    \.......\  \........\  \........\  \................../  /......./    \......\
       \................/  /....../      \.......\  \........\  \........\  \................/  /......./      \......\
        \............../  /....../        \.......\  \........\  \........\  \............../  /......./        \......\
         \............/  /....../          \.......\  \........\  \........\  \............/  /......./          \......\
          \........../  /....../            \.......\  \........\  \........\  \........../  /......./            \......\
                                                                               /........./
                                                                              /........./
                                                                             /........./
                                                                            /........./
                                                                           /---------/
                                                    VAIIYA technologies LLC
                                            Empowering security, one byte at a time.

                                            
                        Welcome to the Terminal! all checks are complete. you can continue on your work.
    """)
def timefetch():
#time fetch for login
    curtime = datetime.now().strftime('%H:%M:%S') 
    curdate = datetime.now().strftime('%Y-%m-%d')
    print("""|""")
    print('Welcome VAIIYA trustee! the time is: ',curtime)
    print('and the date is: ',curdate)
    print("have a wonerful day at VAIIYA Technologies LLC!")
    print("""|""")
# Start the TERMINAL and its commands
def terminal_start_message():
    print(" for a list of commands, please type 'commands' ")
    print("""|""")


def open_terminal():

    while True:
        
        text = prompt('awaiting command(s)>>> ')
#put all the usercommands under here please! 
        


        
        
        
        
        if text == 'CNS':
            print("CNS_VAIIYA_BYPASS_V4.567.EXE EXITCUTING....")
            time.sleep(2)
            CNS_EE_HAKED()

        if text == 't342':
            print('heyy thanks for sayin somthin!')
            continue
        

        if text == 'walker':
            print("welcome walker to your login! please wait while your coffee brews.......")
            time.sleep(3)
            walker_login()

        #BUG: the error "no command" will reply when exiting the FROST EE!
        # FROST EE WIP!! 
        if text == 'frostbyte':
            print("welcome frostbyte to your login! please wait while i startup the supercomputer and freeze these bytes!....")
            time.sleep(3)
            #enters the frostbyte EE
            frostbyte_login()


#below are all the non-user commands, DO NOT REMOVE!
            #the COMMANDS directory, DO NOT REMOVE!
        if text == 'commands':
            print("""|""")
            print("""|""")
            print("Avalible commands: (all may not be listed.)")
            print("""|""")
            print("command: walker | The login for CM|walker")
            print("command: frostbyte | The login for CM|frostbyte")
            print("placeholder here | explanation here")
            print("placeholder here | explanation here")
            print("""C0MM#ND: CNS | {ERROR: UNKNOWN PROGRAM ENTITY}""")
            print("""|""")
            print("""|""")
            #the EXIT command, DO NOT REMOVE!! 
        if text == 'exit':
            print('exiting the terminal... have a nice day!')
            time.sleep(0.5)
            exit()
        
        #error response
        else:
            print("uhh, hmm, i dont think thats a command friend! type 'commands' for a list of commands!")

# PLEASE PUT ALL 2ND DEF(S) BELOW THIS NOTE! 






#PUT ALL OTHER NON SUBCOMMAND DEFs BELOW HERE!
# the CNS EE below this messange
def CNS_EE_HAKED():
    #below is the Y/N prompt for CNS, and the following `result` can be split into a bool and set as True or False
    result = yes_no_dialog(
    title='CNS.02.06.01',
    text='dO yOU wAnT ThE tRUTh?').run()
    #if the `result` has a bool of True, it will run this part of the code. 
    if result == True:
         message_dialog(
    title='CNS.02.06.01',
    text='very well then, we will see you soon enough').run()
         #then after it retuns to the main menu and exits the program.
         print("VAIIYA DEFENDER ENGINE CRITICAL FAILURE!: THE VAIIYA DEFENDER ENGINE HAS FOUND A BREACH AND WILL NOW FORCE QUIT THE PROGRAM")
         print("""|""")
         print("THE PROGRAM WILL SHUTDOWN IN:")
         time.sleep(1)
         print("3")
         time.sleep(1)
         print("2")
         time.sleep(1)
         print("1")
         time.sleep(1)
         exit()
    #if the `result` has a bool of False, then it will run this part of code. and again will return to menu and exit the program. 
    if result == False:
         message_dialog(
    title='CNS.02.06.01',
    text='how dissapointing, that you dont want tHe TrutH. we will see you soon enough').run()
         print("VAIIYA DEFENDER ENGINE CRITICAL FAILURE!: THE VAIIYA DEFENDER ENGINE HAS FOUND A BREACH AND WILL NOW FORCE QUIT THE PROGRAM")
         print("""|""")
         print("THE PROGRAM WILL SHUTDOWN IN:")
         time.sleep(1)
         print("3")
         time.sleep(1)
         print("2")
         time.sleep(1)
         print("1")
         time.sleep(1)
         exit()
#the idea above from smashel! 

#add passwords here for the logins and name the vars respectivly.
# 
#the website for reference to the password system is https://www.geeksforgeeks.org/npm-bcrypt/ 
# 
#  
#walkerpasswrd1
walkerhash = b'$2b$12$M7LXCClyfsnN9SjibtnEmuLEOlR68H2ovjCBA0zcAIBs2RHBzOnFy'
#frostEEpswrd1
frosthash = b'$2b$12$AUur7AKX1aGQurOlmM46Pu0OX9HXqx6UHH9SHiEvrCJM56JvUjYfu'


#walker login here
def walker_login():
    #when exiting the prompt with the `<cancel>`, the program will forcequit for some reason. 

    #password prompt; 
    userpassword = text = input_dialog(
    title='Walker password input',
    text='walker password:').run()
    #encodes the given password for comapare
    userpassword = userpassword.encode('utf-8')

    #comapre password hashes, if identical then "result" == True, then it will move onto walker_entered
    result = bcrypt.checkpw(userpassword, walkerhash)
    if result:
          walker_entered()
#end of walker password varifi 

def walker_entered():
    print("welcome walker! here currnently there is nothing, i have no idea what to put here for you guys.")
    print("but id assume you are familiar with github so if you have an idea i would more than glad take a look and try to implement it! ")
    text = prompt("type EXIT to exit this page; ")
    if text == 'exit':
        return
        #end of walker login

# FROST EE STUFF OVER HERE!
def frostbyte_login():
                
    #there is a bug that cuases the `no command` string to print when exiting.
    print("to exit, type EXIT in the password!")
    userpassword = text = input_dialog(
    title='frostbyte password input',
    text='frostbyte password:').run()
    
    userpassword = userpassword.encode('utf-8')
               
    #comapre password hashes
    result = bcrypt.checkpw(userpassword, frosthash)
    if result:
          frostbytes_EE_entered()
    if text == 'exit':
        return
# 2nd part to the FROST EE                     
def frostbytes_EE_entered():
    
    #the following prompts from promptTK are for frost taling about UwU more and more ¯\_(ツ)_/¯
    message_dialog(
    title='VAIIYA Warning systems',
    text='VAIIYA TERMINAL WARNING AWAITING ATTENTION!').run()
    
    message_dialog(
    title='VAIIYA Warning systems',
    text='VAIIYA employee T342 has marked you as "requires careful observation and mental medical attention." so the VAIIYA system observation drones will now observe you.').run()

    message_dialog(
    title='VAIIYA Warning systems',
    text='thank you for your attention. you may continue your tasks and have a safe day!').run()
    
    
    print(f"""welcome frostbyte! to your ee/login! dont worry, no one will find your password ^_+ """)
    text = prompt("type EXIT to exit this page;")
    
    if text == 'exit':
        return
#END OF FROST EE CODE, 



# Main system loop
def game_loop():
    #window_resize_startup()
    startup_screen_ASCII()
    loading_bars_intro_1()
    loading_bars_intro_2()
    loading_bars_intro_3()
    main_menu()
    timefetch()
    terminal_start_message()
    open_terminal()
    
    while True:
        #there is no code to run right before startup so there is a `pass` here. 
            pass

# Start the game
game_loop()


#this func is not required for the operation of the program, so it is disabled.


#if __name__ == "__main__":
#        main()

#the notes below are very old. (maybe from v0.0.2 or v0.0.3)



#IMPORTANT NOTES AND BEHAVEIORS IN CODE!!!! 
# 1. NEVER put a IF staement with a OR command!! or any other command will do the same action!! including undefined ones!! 
# the way to get arount this is use a ELIF command, than the OR statement will not reapet undefined or incorrect strings!!! - T342 the owner if you were snooping >:3 

#update above: you cannot use workaround in main menu!! i have no idea why! you will just need to make a dual command instead. 

# 2. UwU dont you say ANYTHING ABOUT THAT - NOT T342, DONT TELL FROST PLEASESSSSSSSSSSSSSSSSSSSSSS


#found new menu system that need the EXIT command:
#  
#command = input("type EXIT to go to main menu>>> ").lower()
#    while True:
        #if command == "exit":
            #break
# use that at the end of a text viewscreen or file viewer - T342 you extra snoop >:3 


