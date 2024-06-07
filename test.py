import os
import sys

run = {
    "c": "gcc {0} -o a.exe && a.exe < {1} > {2}",
    "cpp": "g++ {0} -o a.exe && a.exe < {1} > {2}",
    "java": "javac {0} && java {3} < {1} > {2}",
    "py": "python {0} < {1} > {2}"
}

m = {}
for i in range(1, len(sys.argv), 2):
    m[sys.argv[i]] = sys.argv[i+1]

def runCode(fileType, input, output):
    file = m[fileType]
    filename, language = file.split(".")
    os.system(run[language].format(file, input, output, filename))

def getData(filename):
    file, data = open(filename, "r"), []
    try:
        for line in file:
            if len(line.rstrip()) > 0:
                data.append(line.rstrip())
    finally:
        file.close()
    return data

# Execution starts from here
os.system("echo. > dummy")
testcase, t = int(m["-t"]) if "-t" in m else 1, 0
while t < testcase:
    runCode("-g", "dummy", "input") # Run generator code
    runCode("-c", "input", "correct") # Run correct code
    runCode("-w", "input", "wrong") #Run wrong code
    if getData("correct") != getData("wrong"):
        os.system("copy input input" + str(t))
        os.system("del input")
        os.system("copy correct correct" + str(t))
        os.system("del correct")
        os.system("copy wrong wrong" + str(t))
        os.system("del wrong")
        t += 1
        print(str(t) + " testcase found!")
os.system("del dummy")
