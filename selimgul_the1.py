# Selim Gul
Quota = float(input("Please enter your internet quota (GB): "))
TimeWatched = float(input("Please enter your total video viewing time in minutes: "))
MessagesSent = float(input("Please enter the number of messages you send: "))
x = TimeWatched*7.7    #Amount of quota consumed by video in MB
y = MessagesSent*1.7/1024   #Amount of quota consumed by messages in MB
z = Quota*1024   #Total in MB
k = (z-x-y)/1024  #Remaining quota in GB

if k<0:
  print("You don't have any quota remaining, you can't watch anymore videos")
else:
  print("Your remaining internet quota is", format(k,".2f"), "GB(s).")
m = k*1024/7.7 #Total minutes left
h = m/60
e = int(h)  #Hours left
n = int(m-(e*60)) #Minutes left
d = m*60-(e*3600+n*60)
print("You can watch video for", e, "hour(s),", n, "minute(s)", "and", format(d,".2f"), "second(s).")
