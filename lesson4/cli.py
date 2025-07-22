# command line test
import argparse

def test(message):
    print('\nTest Message = ', message)

parser = argparse.ArgumentParser(prog='cli.py', description='This is a command line test', epilog='End of help file')
parser.add_argument('filename')
parser.add_argument('-m', '--message')
parser.add_argument('-n', '--name')
parser.add_argument('-a', '--age', type=int)
#parser.add_argument('-h', '--help', action='help')
args = parser.parse_args()
print('filename = ',args.filename)
print('message = ',args.message)
print('name = ',args.name)
print('age = ',args.age)

test(args.message)

