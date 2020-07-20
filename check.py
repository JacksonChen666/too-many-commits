from os.path import exists
from subprocess import run

if not exists("history.txt"):
    print("Running `git log --pretty=format:%s > history.txt`...")
    run("git log --pretty=format:%s > history.txt", shell=True)

with open("history.txt") as f:
    text = [int(i[10:]) for i in f.read().splitlines()]
commits, incorrect, incorrect2, tempC = len(text), [], [], 0

for i in text:
    if i != commits:
        incorrect.append(i)
    commits -= 1

incLen = len(incorrect)

for i in range(incLen):
    try:
        t1 = incorrect[i]
        if not t1 == incorrect[i + 1] + 1:
            incorrect2.append(str(t1))
    except IndexError:
        incorrect2.append(str(incorrect[i]))

if len(incorrect2) > 0:
    print(f'Incorrects: {", ".join(list(reversed(incorrect2)))}')
else:
    print("Noice. Nothing is wrong here.")