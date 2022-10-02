"""
File: webcrawler.py
Name: Helen Lai
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="lxml")

        # ----- Write your code below this line ----- #

        tags = soup.tbody.find_all('tr')

        male_number = 0
        female_number = 0
        rank = 0
        for tag in tags:
            rank += 1
            if rank <= 200:  # to deal with the last tag that we don't wanna include in [all_td]
                # extract all text in <td></td>
                all_td = tag.find_all('td')
                all_td = [ele.text for ele in all_td]
                # calculate male and female number
                male_number += int(all_td[2].replace(',', ''))
                female_number += int(all_td[4].replace(',', ''))
        print('Male Number: ', male_number)
        print('Female Number: ', female_number)


if __name__ == '__main__':
    main()
