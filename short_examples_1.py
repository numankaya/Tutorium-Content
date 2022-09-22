# 1.YOL
if 1 == 2:
  print("a")
else:
  print("b")
  
# 2.YOL
print("a") if 1 == 2 else print("b")

#####################################################

# 1.YOL
ans = input("Do you want to continue? y/n")
if ans == "y":
  print("Running...")
else:
  print("Exit.")
  
# 2.YOL
ans = input("Do you want to continue? y/n")
print("Running") if ans == "y" else print("Exit.")
