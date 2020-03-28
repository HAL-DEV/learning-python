# Excepciones

# Levantar situaciones no esperadas
#  try:
#      pass
#  except:
#  else:
import logging

# Ejemplo
try:
    5 + '' # Error de tipos
    pass
except TypeError as e: # Siempre deberíamos cachar la excepción más específica posible
    logging.error(e)
