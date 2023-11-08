import subprocess
import git, os
def play():
    print("Starting Pyncraft")
    try:
        git.Repo.clone_from("https://github.com/Xanderplayz16/Pyncraft.git", "./versions/git")
    except:
        pass

    os.system("cd versions/git && git pull && cd ../..")

    os.system("pip install -r versions/git/requirements.txt")

    os.system("python versions/git/src/PynCraft.py")
