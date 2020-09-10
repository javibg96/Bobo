import logging
import src.cerebro_bobo as b

try:
    print(b.Cerebro().funciona())

except:
    logging.exception("Bobo error traceback")
