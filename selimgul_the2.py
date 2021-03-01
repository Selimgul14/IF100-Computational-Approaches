oldcourses = str(input("Please enter the courses you have taken previously with letter grades: "))
oldcourses = oldcourses.upper()
oldcourses = ";" + oldcourses
if oldcourses.count(";") == oldcourses.count(":"):
  newcourses = str(input("Please enter the courses you have taken this semester with letter grades: "))
  newcourses = ";" + newcourses
  newcourses = newcourses.upper()
  if newcourses.count(";") == newcourses.count(":"):
    check = str(input("Please enter the course you want to check: "))
    position = newcourses.find(check) 
    new_p = newcourses.find(":", position)
    remaining = newcourses[new_p+1:]
    grade = remaining.split(";")[0]
    check = ";" + check
    # check = check.strip()
    if check in newcourses:
      oldlist = oldcourses.split(";")
      newlist = newcourses.split(";")
      if (check + ":F") in newcourses:
        if check in oldcourses:
        #   if check + ":U" or check + ":u" in oldcourses:
          if (check + ":U") in oldcourses:
            print("Your grade for", check[1:], "is U.")
          else:
            print("Your grade for", check[1:], "is F.")
        else:
          print("Your grade for", check[1:], "is U.")
      else:
        # print("You can choose between S and {} for {} ")
        print("You can choose between S and {} for {}.".format(grade, check[1:]))
    else:
      print("You didn't take", check[1:], "this semester.")  
  else:
    print("Invalid input")  
else:
  print("Invalid input")  