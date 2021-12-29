# -*- coding: utf-8 -*-

from random import randint
from bs4 import BeautifulSoup
import requests as req 
from time import sleep
import lxml
def linkgenerator(lenght: int) -> str:
  '''
  This function generates links with lenght 'lenght' symbols for postimg.cc parsing.
  '''
  # Feel free to change links, postimg.cc is just an example
  link = 'https://postimg.cc/'
  
  alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
              'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4',
              '5', '6', '7', '8', '9', '0']
  for lenghtlink in range(lenght):
    link += alphabet[randint(0,len(alphabet) - 1)]
    
  yield link
  link = 'https://postimg.cc/'


def startparsing() -> str:
  '''
  This function requests link from linkgenerator, then check it's title.
  If title 404 -> next link, else func print SUCCESS and breaks
  '''
  # This loop requests new links and send 'em to req.get() until working one won't be found.
  while True:
    generatedlink = linkgenerator(8)
    for link in generatedlink:
      print(link)
    # Parsing html from our lin
    resp = req.get(link) 
    soup = BeautifulSoup(resp.text, 'lxml')
    # Default title for clear page on postimg.cc is Error 404 (Not found)
    if str(soup.title) == '<title>Error 404 (Not found)</title>':
      print('404')
    else:
      # Double triumph if u find a working link out of 136 trillion possible links.
      print('SUCCESS')
      return 'SUCCESS'
    #sleep(2) # Feel free to play with sleep parameter,
    # better use vpn to except blocking ur IP(RiseUp VPN the most comfy for me).


startparsing()

