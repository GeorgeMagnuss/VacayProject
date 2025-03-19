import psycopg as pg
from src.config import conninfo

def get_connection():
    return pg.connect(conninfo)
