import pywhatkit as kit

# Número de teléfono del destinatario (con código de país, pero sin el +)
phone_number = '+51978530640'

# Mensaje que quieres enviar
message = 'Hello from Python using pywhatkit!'

# Hora y minuto en que deseas enviar el mensaje (24 horas)
# Nota: pywhatkit envía mensajes con al menos 1 minuto de anticipación
import datetime
now = datetime.datetime.now()
hour = now.hour
minute = now.minute + 2  # Enviar el mensaje dentro de 2 minutos

# Envía el mensaje
kit.sendwhatmsg(phone_number, message, hour, minute)
