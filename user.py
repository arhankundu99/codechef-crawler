from bs4 import BeautifulSoup
from time import sleep
import requests
from headers import headers
import os


def download(problem_code, link):
    file = problem_code + ".txt"
    parent_path = "SOLUTIONS"
    final_path = os.path.join(parent_path, file)

    if os.path.exists(final_path):
        print("This file is already downloaded")
        return

    r = requests.get(link)
    link = BeautifulSoup(r.text, 'html.parser').find('a', string="View")['href']
    view_solution_link = "https://www.codechef.com" + link
    view_plane_text_link = view_solution_link.replace("viewsolution", "viewplaintext")

    r = requests.get(view_plane_text_link, headers=headers)
    code = BeautifulSoup(r.content, "html.parser").find("pre").text

    with open(file, "w") as f:
        for line in code:
            f.write(line)

    if not os.path.exists(parent_path):
        os.mkdir(parent_path)
    os.rename(file, final_path)


class User:
    def __init__(self, user_name):
        self.user_name = user_name
        url = 'https://www.codechef.com/users/' + self.user_name
        r = requests.get(url)
        self.soup = BeautifulSoup(markup=r.text, features='html.parser')

    def get_ratings(self):
        print("Fetching ratings...")
        sleep(2)
        try:
            overall_rating = self.soup.find("div", attrs={'class': 'rating-number'}).text
            ratings = self.soup.find('table', attrs={'class': 'rating-table'}).findAll('td')
            long_rating = ratings[1].text
            cookoff_rating = ratings[5].text
            lunch_rating = ratings[9].text

            print("Overall Rating: {}\nLong Challenge Rating: {}\nCookoff Rating: {}\nLunch Time Rating: {}"
                  .format(overall_rating, long_rating, cookoff_rating, lunch_rating))
        except Exception :
            print("Something went wrong!")

    def get_profile(self):
        try:
            user_details = self.soup.find("ul", attrs={'class', 'side-nav'}).findAll('li')
            print("Username: {}".format(self.user_name))
            for i in range(1, 5):
                print(user_details[i].text)
        except Exception:
            print("Something went wrong!")

    def get_code(self, problem_code):
        info = self.soup.find('a', text=problem_code)
        if info:
            link = 'https://www.codechef.com'+info['href']
            download(problem_code, link)
        else:
            print("User has not solved this problem yet")

    def has_solved(self, problem_code):
        content = self.soup.find("section", attrs={'class': 'rating-data-section problems-solved'})
        return content.text.__contains__(problem_code)
