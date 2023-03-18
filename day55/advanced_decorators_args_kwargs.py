
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False


def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        print("Checking if user is authenticated")
        if args[0].is_logged_in:
            function(args[0])
    return wrapper


@is_authenticated_decorator
def create_blog_post(user):
    print(f"{user.name} is creating a blog post")


new_user = User("Angela")
new_user.is_logged_in = True
create_blog_post(user=new_user)

