import requests
from input_handler import parse_args
import argparse


def iterar_archivo_status(path, funcion):
    try:
        with open(path,"r") as archivo:
            for linea in archivo:
                limpio = linea.strip()
                funcion(limpio,mayus,write_file)
    except FileNotFoundError:
        print("te has equivocado, prueba otra vez")
    except Exception as e:
        print("Error" + e)



def check_status(url,funcion,funcion2):
    url = add_http(url)
    try:
        respuesta = requests.get(url, timeout = 5)
        url = funcion(url)
        funcion2(respuesta.status_code,url)
        print(respuesta.status_code, url)
    except requests.exceptions.RequestException as error:
        print(f"[Error] {error}")


def add_http(url):
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
        return url
    else:
        return url


def mayus(url3):
   url4 = url3.upper()
   return url4


def write_file(code,url,file="resultados.txt"):
    with open(file,"a") as f:
        f.write(f"[{code}] - {url}\n")


args = parse_args()
print(args.input1)
iterar_archivo_status(args.input1, check_status)