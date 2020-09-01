# README

These are the python scripts I use to fetch solutions, editorials and user profile on codechef

## Setup

You can clone this repository using `https://github.com/arhankundu99/codechef-crawler.git` \
Scripts are written in python3. So you should have a python3 interpreter

## Requirements

You can easily install all requirements by just using the following command- \
`$ pip install -r requirements.txt`

## Usage
### Get editorials and schedule of future contests
```python
import crawler

crawler.get_schedule(): 
# returns future contests

crawer.get_editorial(contest_code, problem_code)
# downloads editorial for the given problem
```
### Get user specific details
```python
from user import User

# create an object of User class
User user = new User(user_name)

user.get_ratings()
# returns the ratings of long challenges, lunchtimes and cook-off challenges of the user

user.get_profile()
# returns user related profile

user.has_solved(problem_code)
# returns true if the user has solved the problem
