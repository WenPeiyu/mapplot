import requests
from PIL import Image
from io import BytesIO

URL_GEOCODE = "http://api.map.baidu.com/geocoder/v2/"
URL_GETMAP = "http://api.map.baidu.com/staticimage/v2"
URL_IP = "http://api.map.baidu.com/location/ip"
URL_CONVERT = "http://api.map.baidu.com/geoconv/v1/"

class baidumapapi(object):
    def __init__(self, token):
        self.token = token

    def getCoordinate(self, address, output="json", ret_coordtype="bd09ll"):
        res = requests.get(URL_GEOCODE, params={
            "ak":self.token,
            "address":address,
            "output":output,
            "ret_coordtype":ret_coordtype
        })
        return res.json()["result"]

    def getAddress(self, location, coordtype="bd09ll",
                   output="json", ret_coordtype="bd09ll"):
        res = requests.get(URL_GEOCODE, params={
            "ak":self.token,
            "location":location,
            "coordtype":coordtype,
            "output":output,
            "ret_coordtype":ret_coordtype
        })
        return res.json()["result"]

    def getMap(self, center, file="example.png", width="512", height="512",
               zoom="11", coordtype="bd09ll"):
        res = requests.get(URL_GETMAP, params={
            "ak":self.token,
            "center":center,
            "width":width,
            "height":height,
            "zoom":zoom,
            "coordtype":coordtype
        })
        im = Image.open(BytesIO(res.content))
        im.save(file, "png")

    def ip(self, ip, coor="BD09ll"):
        res = requests.get(URL_IP, params={
            "ak":self.token,
            "ip":ip,
            "coor":coor
        })
        return res.json()["result"]

    def convert(self):
        pass