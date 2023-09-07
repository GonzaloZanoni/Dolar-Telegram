from bs4 import BeautifulSoup
import requests
from colorama import Fore

url = requests.get("https://dolarhoy.com/")

# Realiza una solicitud HTTP GET a la URL  para obtener el contenido de la página web

soup = BeautifulSoup(url.content, "html.parser")# Creo un objeto BeautifulSoup para analizar el contenido HTML

Val_divs = soup.find_all("div", class_="val")# Encuentra todos los elementos <div> con la clase "val" en el contenido de la página

indices = [0, 1, 4, 5]

# Índices que se usarán para acceder a los elementos específicos de la lista de divisas

categorias = ["BLUE", "BLUE", "Oficial promedio", "Oficial promedio"]

# Etiquetas para categorías específicas de divisas

preciosCambios = []
ListaCompra = []
ListaVenta = []

# Inicializando listas vacías para almacenar los precios y la información de compra/venta

for idx, categoria in zip(indices, categorias):
    val_div = Val_divs[idx]
    label_text = val_div.find_previous_sibling("div", class_="label").text.strip()
    valor = val_div.text.strip()
    valorNumero = float(valor.replace('$', ''))
    preciosCambios.append(valorNumero)
    if "compra" in label_text.lower():
        compra = (f"{categoria} Compra: {valorNumero}")
        ListaCompra.append(compra)
    elif "venta" in label_text.lower():
        venta = (f"{categoria} Venta: {valorNumero}")
        ListaVenta.append(venta)

# Procesando la información obtenida de los elementos HTML y almacenándola en las listas correspondientes

preciosActuales = [715.0, 735.0, 349.03, 366.79]

# Lista de precios actuales para comparación
color_verde = Fore.GREEN
color_amarillo = Fore.YELLOW
if preciosCambios != preciosActuales:
    print("\n"+color_amarillo+"Hay Cambios en el Dolar")
else:
    print("\n"+color_verde+"No hay Cambios en el Dolar")

# Comparando los precios actuales con los precios obtenidos y mostrando un mensaje según el resultado


















# D_Blue_Compra = soup.find("div",{"class":"val"})
# BlueC_Inicio_text = D_Blue_Compra.text
# BlueC_Inicial= float(BlueC_Inicio_text.replace('$', ''))
# print(BlueC_Inicial)

# precioActual = 720
# if BlueC_Inicial != precioActual:
#     print("Hay Cambios en el Dolar Blue")
# else:
#     print("No hay Cambios en el Dolar blue")
        
      
            
        

        