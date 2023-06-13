import argparse
import json
import xmltodict as xml
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

class Citizen:
  def __init__(self, name, age):
    self.name = name
    self.age = age

citizen = Citizen("Jan Kowalski", 33)
citizen_dict = {
  "name": citizen.name,
  "age": citizen.age,
}
filename = "citizens.json"
with open(filename, "w") as citizens:
  json.dump(citizen_dict, file)
  
class Dog_Shelter(self, breed, age):
  self.breed = breed
  self.age = age
 filename = "shelter.yml"
try:
  with open(filename, "r") as file:
    data = yaml.safe_load(file)
except FileNotFoundError:
  print("Plik nie istnieje")
  exit()
#Weryfikacja poprawności składni pliku
if not isinstance(data, dict):
  print("Błąd składni pliku.")
  exit()
required_fields = ["name", "age"]
for field in required_fields:
  if field not in data:
        print("Błąd składni pliku.")
        exit()
shelter_dict = {
    "breed": shelter.breed,
    "age": shelter.age
 }
shelter = Shelter(data["breed"], data["age"])
  filename = "shelterfdogs.yml"
with open(filename, "w") as filet:
    yaml.dump(shelter_dict, filet)
class USA_states:
  def __init__(self, name, population)
  self.name = name
  self.population = population
filename = "usa_states.xml"
try:
  tree = xml.parse(filename)
  root - tree.getroot()
except FileNotFoundError:
  print(f"Plik {filename} nie istnieje.")
  exit()
except xml.ParseError:
  print("Błąd składni pliku XML.")
  exit()
#Weryfikowanie poprawności składni pliku
if root.tag != "usa_states":
  print("Błąd składni pliku."
  exit()
required_fields = ["name", "population"]
for field in required_fields:
    if root.find(field) is None:
    print(f"Błąd składni.")
    exit()
#Wczytywanie danych do obiektu
 name = root.find("name").text
 population = int(root.find("population").text)
 usa_states = USA_states(name, population)
 
 print(f"Informacje o stanach w USA: \nNazwa: {usa_states.name}\nPopulation: {usa_states.population}")
