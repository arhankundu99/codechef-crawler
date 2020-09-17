from user import User
import crawler

user = User('arhankundu99')


def solutions_download_test():
    contest_name = 'APRIL20B'
    user.download_all_codes(contest_name)


def editorial_download_test():
    contest_name = 'MAY20B'
    crawler.get_editorial(contest_name)


def get_code():
    problem_code = 'TRPLSRT'
    user.get_code(problem_code)


def profile_test():
    user.get_profile()


def ratings_test():
    user.get_ratings()


def crawler_test():
    crawler.get_schedule()

