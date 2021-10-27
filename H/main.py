import os
for i in range(1, 500):
    os.system("sudo rm bot.txt")
    os.system('git add -A')
    os.system('git commit -m "Added File"')
    os.system("touch bot.txt")
    os.system('git add -A')
    os.system('git commit -m "Added File"')
os.system('git push -u origin main')