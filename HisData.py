from bs4 import BeautifulSoup  # pip install beautifulSoup4
import os
import re

class HisData:
    def __int__(self):
        self.folder_path = ''
        self.his_data = []

    def getData(self):
        self.folder_path = os.path.dirname(os.path.realpath(__file__))
        with open(self.folder_path + "/data/his_data.html", 'r') as data:
            return data.read()

    def preprocessingData(self, elements):
        list_all = []
        for index, element in enumerate(elements):
            list = []
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
            list.append(raffle_round)
            list.append(raffle_date)
            list.append(first_win_count)
            list.append(first_win_amount)
            list.append(second_win_count)
            list.append(second_win_amount)
            list.append(third_win_count)
            list.append(third_win_amount)
            list.append(fourth_win_count)
            list.append(fourth_win_amount)
            list.append(fifth_win_count)
            list.append(fifth_win_amount)
            list.append(raffle_num_one)
            list.append(raffle_num_two)
            list.append(raffle_num_three)
            list.append(raffle_num_four)
            list.append(raffle_num_five)
            list.append(raffle_num_six)
            list.append(raffle_num_bonus)

            list_all.append(list)
        return list_all


    def getLottoinfo(self):
        data = self.getData()
        soup = BeautifulSoup(data, "html.parser")
        elements = soup.select('table > tr ')
        self.his_data = self.preprocessingData(elements)
        return self.his_data


# if __name__ == "__main__":
#         main = HisData()


