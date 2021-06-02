import codecs


def print_Code(x):
    output = ''
    output = output.join(x)
    print()

    print(" The Result is : " + output)

    main()


def encode(x):
    for i in range(len(x)):
        a = ord(x[i])
        a = a + 4
        x[i] = chr(a)

    print_Code(x)


def decode(x):
    for i in range(len(x)):
        a = ord(x[i])
        a = a - 4
        x[i] = chr(a)

    print_Code(x)


def main():
    x = list(input(" enter  the Value: "))
    options = input("Chose any one (1: encode  or 2: decode) : ")

    if options == '1':

        encode(x)

    elif options == '2':

        decode(x)
    else:
        exit()


if __name__ == "__main__":
    main()
