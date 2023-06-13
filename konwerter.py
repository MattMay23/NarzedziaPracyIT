import argparse
#Task1 - "Parsowanie(...)" 
parser = argparse.ArgumentParser(description='Parsowanie')
parser.add_argument('input_file', type=str, help='Nazwa pliku wejściowego')
parser.add_argument('output_file', type=str, help='Nazwa pliku wyjściowego')
parser.add_argument('format', type=str, help='Format pliku')

args = parser.parse_args()
print("Wartość wejściowa: ", args.input_file)
print("Wartość wyjściowa: ", args.output_file)
