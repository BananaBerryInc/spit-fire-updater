import git
from subprocess import call
call(["rm","-rf", "-r", "spit-fire"])
git.Git().clone("https://github.com/BananaBerryInc/spit-fire")
