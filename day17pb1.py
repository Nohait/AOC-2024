def adv(operand) :
    global rega,regb,regc,instruction_pointer 
    if operand == 7 :
        print("Unbound value 7")
        exit()
    elif 0<=operand<=3 :
        rega = int(rega / (2**operand))
    elif operand == 4 :
        rega = int(rega / (2**rega))
    elif operand == 5 :
        rega = int(rega / (2**regb))
    elif operand == 6 :
        rega = int(rega / (2**regc))
    instruction_pointer += 2

def bxl(operand) :
    global rega,regb,regc,instruction_pointer 
    
    if 0 <= operand <= 7 :
        regb = regb ^ operand
    else :
        print(F"Invalid operand : {operand}")
        exit()
    instruction_pointer += 2

def bst(operand) :
    global rega,regb,regc,instruction_pointer 
    if operand == 7 :
        print("Unbound value 7")
        exit()
    elif 0<=operand<=3 :
        regb = operand % 8
    elif operand == 4 :
        regb = rega % 8
    elif operand == 5 :
        regb = regb % 8
    elif operand == 6 :
        regb = regc % 8
    instruction_pointer += 2

def jnz(operand) :
    global rega,regb,regc,instruction_pointer 
    if rega == 0:
        instruction_pointer += 2
    elif 0<=operand<=7 :
        instruction_pointer = operand
    else :
        print(f"Invalid Operand : {operand}")
        exit()

def bxc(operand = None) :
    global rega,regb,regc,instruction_pointer 
    regb = regb ^ regc
    instruction_pointer += 2

def out(operand) :
    global rega,regb,regc,instruction_pointer,output
    if operand == 7 :
        print("Unbound value 7")
        exit()
    elif 0<=operand<=3 :
        output.append(operand % 8)
    elif operand == 4 :
        output.append(rega % 8)
    elif operand == 5 :
        output.append(regb % 8)
    elif operand == 6 :
        output.append(regc % 8)
    instruction_pointer += 2

def bdv(operand) :
    global rega,regb,regc,instruction_pointer 
    if operand == 7 :
        print("Unbound value 7")
        exit()
    elif 0<=operand<=3 :
        regb = int(rega / (2**operand))
    elif operand == 4 :
        regb = int(rega / (2**rega))
    elif operand == 5 :
        regb = int(rega / (2**regb))
    elif operand == 6 :
        regb = int(rega / (2**regc))
    instruction_pointer += 2

def cdv(operand) :
    global rega,regb,regc,instruction_pointer 
    if operand == 7 :
        print("Unbound value 7")
        exit()
    elif 0<=operand<=3 :
        regc = int(rega / (2**operand))
    elif operand == 4 :
        regc = int(rega / (2**rega))
    elif operand == 5 :
        regc = int(rega / (2**regb))
    elif operand == 6 :
        regc = int(rega / (2**regc))
    instruction_pointer += 2
    
global rega,regb,regc,output,instruction_pointer

instructions = {
    0 : adv, # divise la valeur dans le registre A par 2^combo operand
    1 : bxl, # xor bit a bit sur la valeur dans le registre B avec litteral operand
    2 : bst, # ecrit la valeur de son combo operand mod 8 dans le registre B
    3 : jnz, # ne fait rien si A = 0, sinon saute a l'instruction de son litteral operand
    4 : bxc, # ecrit B^C dans B
    5 : out, # calcule son combo operand mod 8 et renvoie sa valeur
    6 : bdv, # comme adv mais écrit dans B (lit dans A)
    7 : cdv # comme bdv mais dans C
}

# 0,1,2,3,4,5

rega = 0
regb = 8
regc = 0
output = []
program = [2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0]
program = [
    2,4,
    1,3,
    7,5,
    4,0,
    1,3,
    0,3,
    5,5,
    3,0
]
instruction_pointer = 0

"""
bst(4) ;
bxl(3) ;
cdv(5) ;
bxc() ;
bxl(3) ;
adv(3)
out(5) ;
jnz(0) ;

while A != 0
    B = A % 8
    B = B ^ 3
    C = A // 2^B
    B = B ^ C
    B = B ^3
    A = A // 2 ^ 3
    out (B % 8)

"""
def test_a(a,program) :
    a = a
    b = 0
    c = 0
    output = []
    while a != 0 :
        b = a % 8
        b ^= 3
        c = a >> b
        b ^= c
        b ^= 3
        a >>= 3
        output.add(b%8)




while instruction_pointer < len(program) :
    # print(instruction_pointer)
    instruction = instructions[program[instruction_pointer]]
    operand = program[instruction_pointer + 1]
    instruction(operand)
    
    

print(output)
print(f"A : {rega}    B : {regb}    C : {regc}")
print(",".join([str(x) for x in output]))