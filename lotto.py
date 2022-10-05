from bs4 import BeautifulSoup  #need pip install beautifulSoup4
import os



def getData():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    with open(folder_path + "/data/his_data.html", 'r') as data:
        return data.read()

def main():
    his_data = getData()
    soup = BeautifulSoup(his_data, "html.parser")
    print(soup.table)

if __name__ == "__main__":
        main()