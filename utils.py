
########################################################################################################
########    FUNCTIONS THAT CREATE THE FILES FOR THE FINITE AUTOMATA FOR INTS AND IDENTIFIERS ###########
########    THEY CAN BE SIMPLY CALLED ONCE, THEY JUST CREATE A DOCUMENT    #############################
########################################################################################################

""""Why spend 20 minutes on a task when you can spend 6 hours failing to automate it?"""

def create_FA_file_for_ints():

    f = open("FAINTS.in", "w")

    f.write("q0,q1,qf1,qf2\n")
    s="-,"
    for i in range(10):
        s+=str(i)+","
    s2 = s[:-1] + "\n"
    f.write(s2)
    f.write("q0\n")
    f.write("qf1,qf2,qf0\n")

    f.write("q0,-=q1\n")
    f.write("q0,0=qf0\n")
    for i in range(1,10):
        f.write("q0,"+str(i) +"=qf1\n")
    for i in range(0,10):
        f.write("qf1,"+str(i) +"=qf1\n")
    for i in range(1,10):
        f.write("q1,"+str(i) +"=qf2\n")

    for i in range(0,10):
        f.write("qf2,"+str(i) +"=qf2\n")    


def create_FA_file_for_identifiers():

    f = open("FAIDS.in", "w")

    f.write("q0,qf\n")
    s="_,"
    for i in range(0,9):
        s+=str(i)+","
    for i in range(26):
        s+=chr(ord("a")+i) + ","
    for i in range(26):
        s+=chr(ord("A")+i) + ","

    s2 = s[:-1] + "\n"
    f.write(s2)
    f.write("q0\n")
    f.write("qf\n")

    for i in range(26):
        f.write("q0," + chr(ord("a")+i) + "=qf\n")
    for i in range(26):
        f.write("q0," + chr(ord("A")+i) + "=qf\n")
    for i in range(0,9):
        f.write("qf," + str(i) + "=qf\n")
    for i in range(26):
        f.write("qf," + chr(ord("a")+i) + "=qf\n")
    for i in range(26):
        f.write("qf," + chr(ord("A")+i) + "=qf\n")
    f.write("qf,_=qf\n")

# create_FA_file_for_identifiers()
