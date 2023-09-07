from PrecioDolar import preciosCambios
from PrecioDolar import preciosActuales
from PrecioDolar import ListaCompra
from PrecioDolar import ListaVenta
import requests

# Importando las listas y bibliotecas necesarias del archivo "PrecioDolar"

def telegram_bot_sendtext(bot_message):
    # Definición de una función para enviar mensajes a Telegram
    bot_token = '6444326533:AAFzgaBFHEShb_T-XIJipjG55xfDN6vXuLM' # Aquí va el token de mi bot de Telegram
    bot_chatID = '1529590627' # Aquí reemplace con el ID del chat de Telegram a donde quieros enviar el mensaje
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    # Creo la URL para enviar el mensaje

    response = requests.get(send_text)

    return response.json()
    
# Defino la función para enviar mensajes a Telegram


if preciosCambios != preciosActuales:
    test = telegram_bot_sendtext(f"Atención! Hay cambios en el dolar! Está en:{str(ListaCompra)+ str(ListaVenta)} \nEnlace: https://dolarhoy.com/")

else:
    test = telegram_bot_sendtext("No Hay cambios en el dolar blue para la compra.")
# Comparando los precios actuales con los precios obtenidos y enviando un mensaje a Telegram en consecuencia







