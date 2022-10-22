from math import *

def C(n,r):
    p = 1
    for i in range(r):
        p *= n-i
    return p/gamma(r+1)

def differentiate(a: list):
    diff = []
    for i in range(len(a)-1):
        diff.append(a[i+1] - a[i])
    return diff

def main():
    original = []
    diff_seq = []
    
    print('Generate formulas for sequences using Gregory-Newton method.')
    inp = input("Original sequence: ")
    limit = int(input("First n terms to print: "))
    spl = inp.split()

    try:
        original = [float(i) for i in spl]
    except:
        print("Sequences can only contain numbers!")
        return

    diff_seq.append(original.copy())
    for i in range(len(original)-1):
        diff_seq.append(differentiate(diff_seq[i]))

    output = []

    for i in range(len(diff_seq)):
        s = diff_seq[i]
        if s[0] != 0:
            output.append(f"{s[0]}*C(x,{i})")

    output = ' + '.join(output)
    print("Formula:", output, end='')
    print(" [C(n, r) stands for n choose r]")
    print("-"*30)
    print("First {} terms:".format(limit))

    for x in range(limit):
        print(f"f({x}) =", eval(output))

if __name__ == '__main__':
    main()

