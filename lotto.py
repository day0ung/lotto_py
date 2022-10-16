import pymysql  # pip install PyMySql

import os

from Data import Data

def main():

    conn = pymysql.connect(host='localhost', port=3306, user='user', password='pwd', db='db')

    instance = Data()
    # his_data = instance.getLottoInfoHis()
    # for data in his_data:
    #     insertLottoInfo(conn, data)

    now_data = instance.getLottoInfoNow()
    insertLottoInfo(conn, now_data)


    conn.close()



def insertLottoInfo(conn, data):
    with conn.cursor(pymysql.cursors.DictCursor) as curs:
        sql = """
        INSERT INTO LOTTO_INFO
        (RAFFLE_ROUND, RAFFLE_DATE, FIRST_WIN_COUNT, FIRST_WIN_AMOUNT, SECOND_WIN_COUNT, SECOND_WIN_AMOUNT,
        THIRD_WIN_COUNT, THIRD_WIN_AMOUNT, FOURTH_WIN_COUNT, FOURTH_WIN_AMOUNT, FIFTH_WIN_COUNT, FIFTH_WIN_AMOUNT,
        BALL_ONE, BALL_TWO, BALL_THREE, BALL_FOUR, BALL_FIVE, BALL_SIX,BALL_BONUS, REG_DT)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW());
        """

        curs.execute(sql, (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18]))
        conn.commit()





if __name__ == "__main__":
        main()