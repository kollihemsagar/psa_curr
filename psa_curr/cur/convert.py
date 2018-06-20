import requests
import json


def conv(to, frm):
    url_str = to +'_'+ frm
    res = requests.get('http://free.currencyconverterapi.com/api/v5/convert?q='+url_str+'&compact=y')
    return json.loads(res.content)[url_str]['val']
