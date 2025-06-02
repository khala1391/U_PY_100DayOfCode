class User:

    # attribute
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 10  # default but not input required
        self.following = 20
    
    # method
    def follow(self, user):
        user.followers += 1
        self.following += 1



user_1 = User("001","angela")

# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)

user_2 = User("002","jack")

user_1.follow(user_2)
print(user_1.followers)  #10
print(user_1.following)  #21 >>increase
print(user_2.followers)  #11 >>increase
print(user_2.following)  #20
