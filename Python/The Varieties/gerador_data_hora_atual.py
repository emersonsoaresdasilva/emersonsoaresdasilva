# → Data e Hora atual:

import os
import time
from datetime import datetime

while (True):
    print(datetime.now().strftime('Data: %d/%m/%Y \nHorário: %H:%M:%S'))
    time.sleep(1)
    os.system('cls')

# ← Fim.