import os

for i in range(30):
    d = '1 day ago'
    ## Open a text file and modify it
    with open('bot.txt', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add bot.txt')
    ## Commit it
    os.system('git commit -m "first commit"')

## push the commit to github
os.system('git push -u origin main')