start = input("Please enter movie names and remaining quota: ")
wanted = input("Please enter the movie you want to watch: ")
index = 0
if wanted in start:
    amount = int(input("Please enter the number of tickets you want to buy: "))
    movielist = start.split(",")
    print(movielist)
else:
    print("There is no such movie in the theater.")

