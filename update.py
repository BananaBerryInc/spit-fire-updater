import git
from subprocess import call
call(["rm","-rf", "-r", "spit-fire"])
call(["del","spit-fire/*.*"])
call(["del","spit-fire\*.*"])
git.Git().clone("https://github.com/BananaBerryInc/spit-fire")
