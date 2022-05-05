#!/usr/bin/python3

from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_datetime = datetime.now(bogota_timezone)

if __name__ == "__main__":
    print("Bogotá: ", bogota_datetime.strftime("%m,%d,%Y %H:%M"))
