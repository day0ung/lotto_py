from bs4 import BeautifulSoup  # pip install beautifulSoup4
import pymysql  # pip install PyMySql

import os
import re


def getData():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    with open(folder_path + "/data/his_data.html", 'r') as data:
        return data.read()

def main():
    his_data = getData()
    soup = BeautifulSoup(his_data, "html.parser")

    conn = pymysql.connect(host='host', port=3306, user='user', password='pwd', db='db')

    elements = soup.select('table > tr ')
    for index, element in enumerate(elements):
        td = element.select('td')
        raffle_round = 0
        raffle_date = ''
        first_win_count = 0
        first_win_amount = 0
        second_win_count = 0
        second_win_amount = 0
        third_win_count = 0
        third_win_amount = 0
        fourth_win_count = 0
        fourth_win_amount = 0
        fifth_win_count = 0
        fifth_win_amount = 0
        raffle_num_one = 0
        raffle_num_two = 0
        raffle_num_three = 0
        raffle_num_four = 0
        raffle_num_five = 0
        raffle_num_six = 0
        raffle_num_bonus = 0
        for i, t in enumerate(td):
            if i == 0: raffle_round = t.text
            if i == 1: raffle_date = t.text.replace('.', '-')
            if i == 2: first_win_count = re.sub('\D+', '', t.text)
            if i == 3: first_win_amount = re.sub('\D+', '', t.text)
            if i == 4: second_win_count = re.sub('\D+', '', t.text)
            if i == 5: second_win_amount = re.sub('\D+', '', t.text)
            if i == 6: third_win_count = re.sub('\D+', '', t.text)
            if i == 7: third_win_amount = re.sub('\D+', '', t.text)
            if i == 8: fourth_win_count = re.sub('\D+', '', t.text)
            if i == 9: fourth_win_amount = re.sub('\D+', '', t.text)
            if i == 10: fifth_win_count = re.sub('\D+', '', t.text)
            if i == 11: fifth_win_amount = re.sub('\D+', '', t.text)
            if i == 12: raffle_num_one = re.sub('\D+', '', t.text)
            if i == 13: raffle_num_two = re.sub('\D+', '', t.text)
            if i == 14: raffle_num_three = re.sub('\D+', '', t.text)
            if i == 15: raffle_num_four = re.sub('\D+', '', t.text)
            if i == 16: raffle_num_five = re.sub('\D+', '', t.text)
            if i == 17: raffle_num_six = re.sub('\D+', '', t.text)
            if i == 18: raffle_num_bonus = re.sub('\D+', '', t.text)
        insertLottoInfo(conn, raffle_round, raffle_date, first_win_count, first_win_amount, second_win_count, second_win_amount,
                   third_win_count, third_win_amount, fourth_win_count, fourth_win_amount, fifth_win_count, fifth_win_amount,
                   raffle_num_one, raffle_num_two, raffle_num_three, raffle_num_four, raffle_num_five, raffle_num_six, raffle_num_bonus)


def insertLottoInfo(conn, raffle_round, raffle_date, first_win_count, first_win_amount, second_win_count, second_win_amount,third_win_count, third_win_amount, fourth_win_count, fourth_win_amount, fifth_win_count, fifth_win_amount,raffle_num_one, raffle_num_two, raffle_num_three, raffle_num_four, raffle_num_five, raffle_num_six, raffle_num_bonus):
    print(first_win_count)
    with conn.cursor(pymysql.cursors.DictCursor) as curs:
        sql = """
        INSERT INTO LOTTO_INFO
        (RAFFLE_ROUND, RAFFLE_DATE, FIRST_WIN_COUNT, FIRST_WIN_AMOUNT, SECOND_WIN_COUNT, SECOND_WIN_AMOUNT, 
        THIRD_WIN_COUNT, THIRD_WIN_AMOUNT, FOURTH_WIN_COUNT, FOURTH_WIN_AMOUNT, FIFTH_WIN_COUNT, FIFTH_WIN_AMOUNT, 
        RAFFLE_NUM_ONE, RAFFLE_NUM_TWO, RAFFLE_NUM_THREE, RAFFLE_NUM_FOUR, RAFFLE_NUM_FIVE, RAFFLE_NUM_SIX, RAFFLE_NUM_BONUS, REG_DT)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW());

              """
        curs.execute(sql, (raffle_round, raffle_date, first_win_count, first_win_amount, second_win_count, second_win_amount,
                    third_win_count, third_win_amount, fourth_win_count, fourth_win_amount, fifth_win_count, fifth_win_amount,
                    raffle_num_one, raffle_num_two, raffle_num_three, raffle_num_four, raffle_num_five, raffle_num_six, raffle_num_bonus))
        conn.commit()







if __name__ == "__main__":
        main()