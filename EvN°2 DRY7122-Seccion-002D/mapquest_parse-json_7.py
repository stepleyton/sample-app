import urllib.parse
import requests
import time

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "bWtNOVMx9vj2Dxh1Zvczd7FLto8DgWcN"

while True:
    hora_actual = time.strftime("%H:%M:%S")
    print("¡Bienvenido! La hora actual es:", hora_actual)
    orig = input("Ciudad de Origen: ")
    if orig == "leyton" or orig == "l":
        break
    dest = input("Ciudad de Destino: ")
    if dest == "leyton" or dest == "l":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = Una llamada de ruta exitosa.\n")
        print("=============================================")
        print("Direcciones desde:  " + (orig) + " to " + (dest))
        print("Duración del viaje: " + (json_data["route"]["formattedTime"]))
        print("Kilometros:         " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
