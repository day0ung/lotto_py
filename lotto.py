from bs4 import BeautifulSoup  # pip install beautifulSoup4
import pymysql  # pip install PyMySql

import os



def getData():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    with open(folder_path + "/data/his_data.html", 'r') as data:
        return data.read()

def main():
    his_data = getData()
    soup = BeautifulSoup(his_data, "html.parser")

    #conn = pymysql.connect(host='', port=3306, user='', password='', db='')

    elements = soup.select('table > tr ')
    for index, element in enumerate(elements):
        td = element.select('td')
        for i, t in enumerate(td):
            if i == 0: print(t.text, '회차')
            if i == 1: print(t.text, '추첨일')
            if i == 2: print(t.text, '1등 당첨자수')
            if i == 3: print(t.text, '1등 당첨금액')
            if i == 4: print(t.text, '2등 당첨자수')
            if i == 5: print(t.text, '2등 당첨금액')
            if i == 6: print(t.text, '3등 당첨자수')
            if i == 7: print(t.text, '3등 당첨금액')
            if i == 8: print(t.text, '4등 당첨자수')
            if i == 9: print(t.text, '4등 당첨금액')
            if i == 10: print(t.text, '5등 당첨자수')
            if i == 11: print(t.text, '5등 당첨금액')
            if i == 12: print(t.text, '당첨번호 1')
            if i == 13: print(t.text, '당첨번호 2')
            if i == 14: print(t.text, '당첨번호 3')
            if i == 15: print(t.text, '당첨번호 4')
            if i == 16: print(t.text, '당첨번호 5')
            if i == 17: print(t.text, '당첨번호 6')
            if i == 18: print(t.text, '당첨번호 보너스')
            




if __name__ == "__main__":
        main()