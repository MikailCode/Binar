def to_binar(arg):
	return bin(arg)[2:]

def from_binar(arg):
	return int(arg, 2)

def main():
	inp = input('Из десятичного в бинарное введите 0 \nИз бинарного в десятичное введите 1\n')
	if inp == '0':
		inp1 = int(input())
		return to_binar(inp1)
	if inp == '1':
		inp1 = input()
		return from_binar(inp1)

print(main())