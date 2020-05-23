from time import gmtime
import logging
import urllib
import requests
from bs4 import BeautifulSoup


class QueryHandler:
    def __init__(self):
        self.url = "https://google.com/search?q="
        # desktop user-agent, no es solo de mac es que google es asi
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        # mobile user-agent
        # MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, " \
        #                    "like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36 "

        self.headers = {"user-agent": USER_AGENT}

    def create_query(self, msg):
        query = msg.replace(' ', '+')
        URL = self.url + query
        resp = requests.get(URL, headers=self.headers)

        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
        else:
            logging.warning(f"something wrong with query: {resp}")
            soup = None
        return soup

    def international_time(self, msg):
        temp_msg = msg.split(" ")
        ciudad = temp_msg[-1]
        soup = self.create_query(msg)
        if soup:
            query1 = soup.find_all('div', class_='gsrt')
            # print(query1)
            # [<div aria-level="3" class="gsrt vk_bk dDoNo" role="heading">17:44</div>]
            query2 = soup.find_all('div', class_='vk_gy vk_sh')
            # print(query2)
            # class="vk_gy vk_sh"> jueves, <span class="KfQeJ">16 de abril de 2020</span> <span class="KfQeJ"> (GMT+1)
            # </span> </div>]
            hora = fecha = ""
            for i in query1:
                hora = i.text
            for j in query2:
                fecha = j.text
            fecha = fecha.replace(" (CEST)", "")
            respuesta = f"En {ciudad}, son las {hora} del {fecha}"
        else:
            respuesta = f"Lo siento, no he podido encontrar resultados sobre: {msg}"
        return respuesta

    def info_searcher(self, busqueda):
        soup = self.create_query(busqueda)
        if soup:
            results = []
            for g in soup.find_all('div', class_='r'):
                anchors = g.find_all('a')
                if anchors:
                    link = anchors[0]['href']
                    title = g.find('h3').text
                    item = {
                        "title": title,
                        "link": link
                    }
                    results.append(item)
            # print(results)
            # [{'title': 'Compra ...- MIL ANUNCIOS.COM', 'link': 'https://www.milanuncios.com/.../'}, {...]
            respuesta = f"Aquí tienes los resultados de: {busqueda}:"
            for search in results:
                respuesta = respuesta + "\n" + search["title"] + ": " + search["link"]
            respuesta = respuesta + "\nEspero haberle sido de ayuda"
        else:
            respuesta = f"Lo siento, no he podido encontrar resultados sobre: {msg}"
        return respuesta
