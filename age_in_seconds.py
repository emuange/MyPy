def age_in_seconds():
    user_age = input("Enter your age: ")
    age_seconds = int(user_age) * 365 * 24 * 60 * 60
    print("You have been alive for like... {} seconds! That is a LOT!".format(age_seconds))
    
age_in_seconds()