import argparse
import json
#Task1 - "Parsowanie(...)" 
parser = argparse.ArgumentParser(description='Parsowanie')
parser.add_argument('input_file', type=str, help='Nazwa pliku wejściowego')
parser.add_argument('output_file', type=str, help='Nazwa pliku wyjściowego')
parser.add_argument('format', type=str, help='Format pliku')

args = parser.parse_args()
print("Wartość wejściowa: ", args.input_file)
print("Wartość wyjściowa: ", args.output_file)

def verify_json(json_example.json):
  try:
    with open(json_example.json) as dj_json:
     data = json.load(dj_json):
      print ("Plik z rozszerzeniem .json jest poprawny składniowo.")
      return data
  except json.JSONDecodeError as eRR:
      print("Błąd składni pliku JSON:", str(eRR))
      return None
  except FileNotFoundError:
      print("Podany plik nie istnieje.")
      return None
