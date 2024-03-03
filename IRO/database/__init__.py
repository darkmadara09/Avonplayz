#MIT License
#Copyright (c) 2023, ©NovaNetworks

from async_pymongo import AsyncClient

from IRO.config import MONGO_DB_URI

DBNAME = "IRO"

mongo = AsyncClient(MONGO_DB_URI)
dbname = mongo[DBNAME]
