import urllib.request
import csv
from bs4 import BeautifulSoup


BASE_URL = "http://www.nfl.com/teams/roster?team="

teams = ["NE", "BUF", "NYJ", "MIA", "BAL", "CLE", "PIT", "CIN", "IND", "HOU", "JAX", "TEN", "KC", "OAK", "DEN", "LAC", "DAL", "PHI", "NYG", "WAS", "GB", "MIN", "CHI", "DET", "NO", "CAR", "TB", "ATL", "SF", "SEA", "LA", "ARI"]


def remove_td(s):
    n = s[4:-5]
    return n


def bday(s):
    a = s.split(r"/")
    return (a[0], a[1], a[2])


def split_name(s):
    a = s.split(",")
    return (a[0].strip(), a[1].strip())

print(len(teams))
with open("nfl-data.csv", 'w') as csv_file:
    writer = csv.writer(csv_file)
    for name in teams:
        team = name
        url = BASE_URL + team
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        players = soup.find(id="result").find("tbody").find_all("tr")
        
        for player in players:
            player_soup = player.find_all("td")
            number = remove_td(str(player_soup[0]))
            (last_name, first_name) = split_name(player_soup[1].find("a").string)
            active_status = remove_td(str(player_soup[3]))
            (month, day, year) = bday(remove_td(str(player_soup[6])))


            if active_status == "ACT":
                writer.writerow([team, number, first_name, last_name, month, day, year])

# with open('nfl-data.csv', 'a') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow([name, price, birthday])

