from typing import List


class FiniteAutomata:

    def __init__(self, Q, EPS, q0, F, delta, is_dfa):
        self.Q = Q
        self.EPS = EPS 
        self.q0 = q0 
        self.F = F 
        self.delta = delta
        self.is_dfa = is_dfa


    @staticmethod    
    def parse_line(line: str)-> List[str]:
        toks = line.split(',')
        for i in range(len(toks)):
            toks[i] = toks[i].strip()
        return toks

    @staticmethod
    def parse_delta_line(line):

        toks = line.split('=')
        rhs = toks[1].split(',')
        for i in range(len(rhs)):
            rhs[i] = rhs[i].strip()
            
        lhs = toks[0].split(',')
        for i in range(len(lhs)):
            lhs[i] = lhs[i].strip()
        
        return [lhs, rhs[0]]

    @staticmethod
    def read_from_file(file_name: str):

        f = open(file_name)

        Q = FiniteAutomata.parse_line(f.readline())
        EPS = FiniteAutomata.parse_line(f.readline())
        q0 = FiniteAutomata.parse_line(f.readline())
        F = FiniteAutomata.parse_line(f.readline())
        delta = {}
        while True:
            line = f.readline()
            # print(line)
            if not line:
                break
            # delta.append(FiniteAutomata.parse_delta_line(line))
            [lhs, rhs] = FiniteAutomata.parse_delta_line(line) 
            is_dfa = True
            if (lhs[0], lhs[1]) in delta.keys():
                delta[(lhs[0], lhs[1])].append((lhs[1], rhs))
                is_dfa = False
            else:
                delta[(lhs[0], lhs[1])] = [rhs]
            # delta[(lhs[0], lhs[1])] = rhs


        return FiniteAutomata(Q, EPS, q0, F, delta, is_dfa)

    def print_menu(self):
        print("1. Show list of states(Q)")
        print("2. Show terminals (EPS)")
        print("3. Show initial state(q0)")
        print("4. Show final state(F)")
        print("5. Show transitions(delta)")
        print("6. Check for sequence")
        print("0. Exit")


    def check_sequence(self, sequence: str):

        if not self.is_dfa:
            return False 
        current  = self.q0[0] 
        for s in sequence:
            # print((current,s))
            if (current, s) in self.delta.keys():
                current = self.delta[(current, s)][0]
            else:
                return False
        
        return current in self.F
    




    def menu(self):

        while True:
            self.print_menu()
            cmd = input(">")
            if cmd == "1":
                print("The elements from Q are: ")
                print(self.Q)    
            elif cmd == "2":
                print("The terminals: ")
                print(self.EPS)     
            elif cmd == "3":
                print("The initial state: ")
                print(self.q0)       
            elif cmd == "4":
                print("The final states: ")
                print(self.F)
            elif cmd == "5":
                print("The transitions: ")
                print(self.delta)   
            elif cmd == "6":
                seq = input("Input the sequence, please\n>")
                print(self.check_sequence(seq))                        
            elif cmd == "0":
                exit()
            else:
                print("choose something from the menu, please")


def test_menu():

    fa = FiniteAutomata.read_from_file("FAINTS.in")
    fa.menu()


# test_menu()

