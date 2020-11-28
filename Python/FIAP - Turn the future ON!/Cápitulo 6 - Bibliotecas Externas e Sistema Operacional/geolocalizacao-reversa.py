from pygeocoder import Geocoder

latitude = float(input("Digite a latitude...: "))
longitude = float(input("Digite a longitude.: "))

resultado = Geocoder.reverse_geocode(latitude, longitude)

if resultado.valid_address == True:
    print("Endereço completo.:", resultado)
    print("Número............:", resultado.street_number)
    print("CEP...............:", resultado.postal_code)