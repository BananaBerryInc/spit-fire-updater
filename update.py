import git
from subprocess import call
from configparser import SafeConfigParser
import shutil

y = "Yes"
n = "No"
save = "n"
firsttime = input("Are you downloading Spit-fire for the first time?(y/n)")
if firsttime == "n":
    save = input("Contnue with the saved game? (y/n)")
    if save == "y":
        parser = SafeConfigParser()
        parser.read("spit-fire/res/options.ini")
        fulscr = parser.get("options", "fulscr")
        level = parser.get("options", "level")
        points = parser.get("options", "points")
    shutil.rmtree("spit-fire")
git.Git().clone("https://github.com/BananaBerryInc/spit-fire")
if save == "y":
    parser.set("options", "fulscr", str(fulscr))
    parser.set("options", "level", str(level))
    parser.set("options", "points", str(points))
    with open('spit-fire/res/options.ini', 'w') as configfile:
        parser.write(configfile)
print("Your copy of Spit-Fire is now up-to-date!" )
exit = input("Press enter to exit ")
