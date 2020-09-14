import sys
import os
import random 

banner = """
     _____        _______   _______ _______ _______ _______ 
    |     \ _____|   |   | |   |   |   _   |_     _|   |   |
    |  --  |_____|       | |       |       | |   | |       |
    |_____/      |___|___| |__|_|__|___|___| |___| |___|___|

            Script that aim to teach how DH math works
"""

print_red       = lambda *args, **kwargs : print("\u001b[31;1m", *args, "\u001b[0m", **kwargs)
print_green     = lambda *args, **kwargs : print("\u001b[32;1m", *args, "\u001b[0m\n", **kwargs)
print_yellow    = lambda *args, **kwargs : print("\u001b[33;1m", *args, "\u001b[0m", **kwargs)
print_blue      = lambda *args, **kwargs : print("\u001b[34;1m", *args, "\u001b[0m", **kwargs)
print_magenta   = lambda *args, **kwargs : print("\u001b[35;1m", *args, "\u001b[0m", **kwargs)
print_cyan      = lambda *args, **kwargs : print("\u001b[36;1m", *args, "\u001b[0m", **kwargs)

class Helper:
    @staticmethod
    def print_banner():
        print_green(banner)

    @staticmethod
    def clear():
        if os.name == "nt" : os.system("cls")
        else: os.system("clear")

    @classmethod
    def go_on(cls):
        print_yellow("\nContinue...", end="")
        input()
        cls.clear()
        print("", end="\n\n")

class Algorithms:

    @staticmethod
    def get_prime_numbers(start = 1000, end = 9999):
        prime_list = []
        for i in range(start, end):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
        return random.choices(prime_list, k=20)

    @staticmethod
    def dh_mod(g, k, p):
        return g ** k % p

class DhMath:
    def __init__(self):
        self.a = ""
        self.b = ""
        self.g = ""
        self.p = ""

    def print_information(self, first_keys = False, shared_secrets = False):
        width = 20
        empty = ' ' * width
        line  = '-' * width
        a = ("a = " + str(self.a)).center(width) if self.a else " " * width
        b = ("b = " + str(self.b)).center(width) if self.b else " " * width
        g = ("g = " + str(self.g)).center(width) if self.g else " " * width
        p = ("p = " + str(self.p)).center(width) if self.p else " " * width

        information = f""" 
        |{'ALICE'.center(width)}|{'PUBLIC'.center(width)}|{'BOB'.center(width)}|
        |{line}|{line}|{line}|
        |{a}|{p}|{b}|
        |{empty}|{g}|{empty}|"""

        if first_keys:
            x1 = Algorithms.dh_mod(self.g, self.a, self.p)
            x2 = Algorithms.dh_mod(self.g, self.b, self.p)

            ex_a_0 = "g ^ a % p".center(width)
            ex_a_1 = (str(self.g)+" ^ "+str(self.a)+" % "+str(self.p)).center(width)
            ex_a_2 = ("x1 = " + str(x1)).center(width)
            ex_b_0 = "g ^ b % p".center(width)
            ex_b_1 = (str(self.g)+" ^ "+str(self.b)+" % "+str(self.p)).center(width)
            ex_b_2 = ("x2 = " + str(x2)).center(width)

            information += f"""
        |{ex_a_0}|{empty}|{ex_b_0}|
        |{ex_a_1}|{empty}|{ex_b_1}|
        |{empty}|{empty}|{empty}|
        |{ex_a_2}|{'<< ------- >>'.center(width)}|{ex_b_2}|"""

        if shared_secrets:
            sh_a_0 = "x2 ^ a % p".center(width)
            sh_a_1 = (str(x2)+" ^ "+str(self.a)+" % "+str(self.p)).center(width)
            sh_a_2 = ("x1 = " + str(Algorithms.dh_mod(x2, self.a, self.p))).center(width)
            sh_b_0 = "x1 ^ a % p".center(width)
            sh_b_1 = (str(x1)+" ^ "+str(self.b)+" % "+str(self.p)).center(width)
            sh_b_2 = ("x2 = " + str(Algorithms.dh_mod(x1, self.b, self.p))).center(width)

            information += f"""
        |{empty}|{empty}|{empty}|
        |{sh_a_0}|{empty}|{sh_b_0}|
        |{sh_a_1}|{empty}|{sh_b_1}|
        |{empty}|{empty}|{empty}|
        |{sh_a_2}|{empty}|{sh_b_2}|"""

        print_cyan(information, end="\n\n")

    def set_a(self):
        while True:
            try:
                print_blue("\n--- Define 'a' number. It can be any number, but let's choose less than 1000 : ", end="")
                a = int(input())
                if a > 1000:
                    print_red("!!! Choose less than 1000!")
                else:
                    self.a = a
                    break
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! 'a' must be number!")

    def set_b(self):
        while True:
            try:
                print_blue("\n--- Define 'b' number. It can be any number, but let's choose less than 1000 : ", end="")
                b = int(input())
                if b > 1000:
                    print_red("!!! Choose less than 1000!")
                else:
                    self.b = b
                    break
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! 'b' must be number!")
    
    def set_p(self, prime_list):
        while True:
            try:
                print_blue("\n--- Select a 'p' number from list above : ", end="")
                p = int(input())
                if p in prime_list:
                    self.p = p
                    break
                else:
                    print_red("!!! Choose a number from list above!")
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! 'p' must be number!")
    
    def set_g(self):
        while True:
            try:
                print_blue("\n--- Select a 'g' number : ", end="")
                g = int(input())
                if g < 500 and g > 100:
                    self.g = g
                    break
                else:
                    print_red("!!! 'g' must be between 100 and 500!")
            except KeyboardInterrupt:
                sys.exit()
            except ValueError:
                print_red("!!! 'g' must be number!")

if __name__ == "__main__":
    d = DhMath()
    Helper.clear()

    # Banner
    Helper.print_banner()
    Helper.go_on()

    # Introduction
    print_red("INTRODUCTION", end="\n\n")
    print_green(">>> Diffie Hellman algorithm allows two parties who HAVE NOT PREVIOUSLY MET to securely establish a key which they can use to secure their communications.")
    print_green(">>> Because of the connection between two parties are public, the data sent to each other must be irreversible.")
    print_green(">>> Diffie Hellman algorithm allows two parties aggree on same key even if the connection is not secure.")
    Helper.go_on()
    
    # Secret Numbers
    print_red("USER SECRET NUMBERS")
    d.print_information()
    print_green(">>> Let's say Alice and Bob want to define a secret key, but they have public connection which they don't trust.")
    print_green(">>> Also note that, Alice and Bob cannot change a key physically, public connection is all they have.")
    print_green(">>> First thing they should do is define their private numbers, let's name them 'a' and 'b'.")
    d.set_a()
    d.set_b()
    d.print_information()
    Helper.go_on()

    # Modulus (p) number
    print_red("PRIME MODULES (p) NUMBER", end="\n\n")
    print_green(">>> The prime modules (p) number is one of the public number which will be used for mod in DH algorithm.")
    print_green(">>> In practical use, 'p' number is very large PRIME number, about 2048 bits long.")
    print_green(">>> The length of 'p' number defines how hard to brute force to crack the keys.")
    print_green(">>> Let's choose a 'p' number, but because of this is example, not 2048 bits long, just 4 bits long (1000-9999)")
    
    print_magenta("Random 20 prime numbers between 1000 and 9999")
    prime_list = Algorithms.get_prime_numbers()
    print_magenta(prime_list)
    d.set_p(prime_list)
    d.print_information()
    Helper.go_on()

    # Base (g) number
    print_red("BASE GENERATOR (g) NUMBER", end="\n\n")
    print_green(">>> Base generator (g) number is another public number.")
    print_green(">>> Both 'g' and 'p' called 'public key pair' and shown as (g,p)")
    print_green(">>> Although 'p' is very long number, 'g' is shorter to calculate easly.")

    print_magenta("Let's choose a 'g' number between 100 and 500")
    d.set_g()
    d.print_information()
    Helper.go_on()

    # Exchange Keys
    print_red("KEY EXCHANGE", end="\n\n")
    print_green(">>> As we've defined all keys, we can found the first keys for exchange.")
    print_green(">>> DH algorithm's main function is :", "\u001b[31;1m" ,"g ^ k % p")
    print_green(">>> The 'k' is 'a' or 'b', depends on which side wants to calculate their exchange key.")
    print_green(">>> Let's look at Alice and Bob exchange keys...")
    d.print_information(first_keys=True)
    print_green(">>> After calculation their keys, Alice and Bob will send the keys (x1 and x2) each other.")
    print_green(">>> Although they use insecure connection to exchange, by the neture of modular arithmetic, 'a' or 'b' cannot found from 'x1' or 'x2'.")
    Helper.go_on()

    # Shared Secrets
    print_red("SHARED SECRETS")
    print_green(">>> After they exchange their exchange keys (x1 and x2), both side can calculate secret keys.")
    print_green(">>> For that, they both use same fuction but this time instead of using 'a' or 'b', they will use the other's 'x1' or 'x2' numbers.")
    d.print_information(first_keys=True, shared_secrets=True)
    print_green(">>> As you can see above, both Alice and Bob reach the same number securely.")
    print_green(">>> After establish same secret key, Alice and Bob can create symmetric encrypted connection.")
    Helper.go_on()

    # Bye
    print_magenta(">>> That was all.")
    print_magenta(">>> Bye.", end = "\n")