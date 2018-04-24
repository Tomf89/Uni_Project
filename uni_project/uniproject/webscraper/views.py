from webscraper.models import Rise_against
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
from pymongo.collection import ReturnDocument
from pymongo import MongoClient
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

client = MongoClient()
db = client.test
mycollection = db["auth_user"]


def index(request):
	data = {}
	return render(request,"webscraper/index.html",data)


def create(request):
	now = datetime.datetime.now()
	artist = "Rise Against"
	url = "http://www.riseagainst.com/tour"
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	##############################################################
	##############################################################
	###### THIS GETS THE DATES AND INPUTS THE CURRENT YEAR #######
	##############################################################
	##############################################################

	g_data_left_inner = soup.find_all("div", {"class": "group-left"})
	g_data_middle_inner = soup.find_all("div", {"class": "group-middle"})
	g_data_right = soup.find_all("div", {"class": "group-right"})
	for itemKey in range(0,len(g_data_left_inner)):
		test = g_data_left_inner[itemKey].find_all("div", {"class": "field__item"})
		for item in test:
			month = item.find_all("span", {"class": "month"})
			day = item.find_all("span", {"class": "day"})
			year = (now.year)
			test1 = g_data_middle_inner[itemKey].find_all("div", {"class": "field__item"})
			test2 = g_data_right[itemKey].find_all("a")
			event_url = str(test2)[10:-14]
			city_country = test1[0].text
			venue = test1[1].text
			event = Rise_against(event_day=day[0].text, event_month=month[0].text, event_year=year, event_url=event_url, event_venue=venue, event_city_country=city_country)
			event.save()
	return HttpResponseRedirect(reverse("webscraper:show"))

def post(self, request):
	form = HomeForm(request.POST)
	if form.is_valid():
		text = form.cleaned_data['post']

def show(request):
	email = None
	try:
		email = request.user.email
	except:
		print('There is no user')
	data = {}
	p = Rise_against.objects.all()
	data["rise_againsts"] = p
	return render(request, 'webscraper/show.html', context={'data':data, 'email':email})

def delete(request):
	Rise_againsts.objects.delete()
	return HttpResponseRedirect(reverse("webscraper:show"))

    
class S(BaseHTTPRequestHandler):
    client = MongoClient()
    db = client.test
    mycollection = db["auth_user"]
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
        
        if self.path[:11] == "/subscribe/":
            self._set_response()
            test = self.path[17:]
            print(test)
            test2 = test.split("&")
            print(test2)
            print(test2[0])
            email = test2[0]
            band = test2[1][5:]
            print(band)
            collections = (db.collection_names())
            if band in collections and "auth_user" in collections:
                mycollection.find_and_modify(query={'email': email}, update={"$set": {'following_artists': band}}, upsert=False, full_response=True)
                self.wfile.write("You have followed Rise Against".format(self.path).encode('utf-8'))
                self.wfile.write('<br><a href="http://127.0.0.1:8000/webscraper/show/">Return</a>'.format(self.path).encode('utf-8'))
            else:
                print("None is not an email")
        else:
            self._set_response()
            self.wfile.write("You are not signed in, please sign in to follow an artist{}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()