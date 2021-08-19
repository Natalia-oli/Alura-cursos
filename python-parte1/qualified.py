import string
def calculate_string(st): 
  a = list(string.ascii_lowercase)
  for elemento in st:
    for elemento_2 in a:
      if elemento in elemento_2:
        print("presente")

calculate_string( "gdfgdf234dg54gf*23oP42")