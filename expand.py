bases = [
    "python error",
    "python exception",
    "python traceback",
    "python runtime error",
    "python syntax error",
    "python typeerror",
    "python valueerror",
    "python keyerror",
    "python indexerror",
    "python attributeerror",
    "javascript error",
    "javascript exception",
    "javascript runtime error",
    "javascript typeerror",
    "javascript referenceerror",
    "javascript syntaxerror",
    "windows error code",
    "windows update error",
    "windows installation error",
    "linux error",
    "linux permission error",
    "linux boot error",
    "git error",
    "git clone error",
    "git push error",
    "git pull error",
    "docker error",
    "docker build error",
    "docker run error",
    "docker container error",
    "npm error",
    "npm install error",
    "npm build error",
    "pip error",
    "pip install error",
    "pip dependency error"
]

modifiers = [
    "explained",
    "meaning",
    "fix",
    "solution",
    "causes",
    "how to fix",
    "how to resolve",
    "troubleshooting",
    "step by step",
    "examples",
    "common reasons",
    "best solution",
    "quick fix",
    "error message",
    "resolution",
    "debugging",
    "stack trace",
    "root cause",
    "why it happens",
    "permanent fix",
    "detailed guide",
    "beginner explanation",
    "advanced fix",
    "official solution",
    "common mistake",
    "frequent issue",
    "real example",
    "practical fix",
    "developer guide",
    "complete explanation"
]

with open("data/keywords.txt", "w", encoding="utf-8") as f:
    for b in bases:
        for m in modifiers:
            f.write(f"{b} {m}\n")

print(f"Generated {len(bases) * len(modifiers)} keywords.")

