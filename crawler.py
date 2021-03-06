import requests
from user import User
from bs4 import BeautifulSoup
from headers import headers
import os


def get_schedule():
    r = requests.get("https://www.codechef.com/contests")
    future_contests = BeautifulSoup(r.text, 'html.parser').findAll('table',
                                                                   attrs={'class': 'dataTable'})[1].findAll('td')
    for i in range(0, len(future_contests), 4):
        print("Contest code:{}\nContest name:{}Start Date:{}\nEnd Date:{}\n".format(future_contests[i].text,
                                                                                    future_contests[i + 1].text,
                                                                                    future_contests[i + 2].text,
                                                                                    future_contests[i + 3].text))


def get_editorial(contest_code, problem_code):
    file = problem_code + " Editorial.txt"
    parent_path = "EDITORIALS"
    path = os.path.join(parent_path, contest_code)
    final_path = os.path.join(path, file)

    if os.path.exists(final_path):
        print("This code has already been downloaded")
        return
    url = "https://discuss.codechef.com/tags/" + contest_code.lower()
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    editorial_link_tags = soup.findAll('a', attrs={"class": 'title raw-link raw-topic-link'})
    editorial_link = ''
    for link in editorial_link_tags:
        if link.text.strip() == problem_code.upper() + ' - Editorial':
            editorial_link = link['href']
            break
    print(editorial_link)

    r = requests.get(editorial_link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    code = soup.find('code').text

    with open(file, 'w') as f:
        for line in code:
            f.write(line)

    if not os.path.exists(parent_path):
        os.mkdir(parent_path)

    if not os.path.exists(path):
        os.mkdir(path)
    os.rename(file, final_path)


# user = User('username') # creates an object of class User
# get_schedule() prints the schedule of upcoming contests
# get_editorial('APRIL20', 'UNITGCD') downloads the editorial
# user = User(username)  creates User object
# user.get_profile()     prints profile details of the user
# user.get_code(problem_code)    downloads the code of the user
# user.get_ratings()     prints ratings of different contests
# user.has_solved(problem_code)     returns True if the user has solved the problem
