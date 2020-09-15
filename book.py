import requests
from bs4 import BeautifulSoup

libIndex = int(input("输入要预约的图书馆编号:")) + 10

url = 'http://10.203.97.155/home/book/more/lib/'+ str(libIndex) +'/type/4'
response = requests.get(url)
soup = BeautifulSoup(response.content,'lxml')
rest = soup.find('div', class_="col-xs-12 col-md-4").find('span',style='color:#000;').text
restNum = int(rest[0:-1])
print('剩余预约' + rest)
if(restNum > 0):
    refurltab = soup.find('a', class_="btn btn-info")
    if(refurltab):
        refurl = 'http://10.203.97.155' + refurltab['href']
        actid = refurl[40:44]
        http_session = requests.session()
        cookies = {
            'PHPSESSID':'pvnkjoge9n31quiecdkic8ij03',
            'uservisit':'1',
            'userid':'3190104509',
            'user_name':'%E9%AB%98%E4%BC%9F%E6%B8%8A'
        }

        requests.utils.add_dict_to_cookiejar(http_session.cookies,cookies)
        form_header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
            "Referer":refurl
        }
        questring = {'mobile': '15267688090', 'id': actid}

        response =  http_session.post('http://10.203.97.155/api.php/activities/' + actid + '/application2', params=questring, headers=form_header)
        if(response.status_code == 200):
            r = response.content.decode()
            status = r[10:11]
            if status == '1':
                print("预约成功")
            else:
                print("预约失败")
        else:
            print("预约失败")
    else:
        print("已停止预约")