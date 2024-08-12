from pywebio.output import *
import pywebio
from pywebio import start_server
h='''
بطاقات جوجل هيه بطاقات تمكنك من شحن الالعاب و الشراء في التطبيقات مثل الغاء الاعلانات او شراء خطط في التطبيقات 
'''
pg='''
2UE80T6HUF57R4RD
K44BZ3ZMPZSP65S3
BGMS37NMY87XMGMG
DMZ0F3539E7UY6MK
38WUNBRE087MNR02
2NZD4XVDD09ECSPF
3BRF35YM9V50VC4Z
HMKATSPEDF9AY7TG
GMCHZBN03H74M4YX
HM0FWMDT8KU7BFHF
2GF2KMFGDRFB7GHV
3NFHM1J88MUHNE96
HMKATSPEDF9AY7TG
BMYSH198YGEE0N6Y
2SCLU8MPSSGN3MH4
2NZD4XVDD09ECSPF
7BV3UAMVCFFYMXHH
HMKATSPEDF9AY7TG
50EX9VSGA0PR2YNH
1GPZ6P2W8C3S6JJD
2SCLU8MPSSGN3MH4
3VT94HP9H039M9P9
50EX9VSGA0PR2YNH
7BV3UAMVCFFYMXHH
'''.split()
import random
hh=lambda :random.choice(pg)
def gg():
	put_text(''.join(hh())).style('color:green;background:black;')

def app():
	put_text('بطاقات الهدايا لجوجل').style('color:red;float: right;background:black;')
	put_text(h).style('color:blue;float:right')
	put_text('احصل على بطاقه مشحونه').style('color:red;float:right;background:black;')
	put_text('\n')
	put_button(' بدء ',onclick=lambda:gg()).style('float:right;')



start_server(app,host='0.0.0.0',port=80)


