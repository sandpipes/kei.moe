import sys

if len(sys.argv) != 2:
    print("Usage: python addTags.py <file>")
    sys.exit(-1)

filepath = sys.argv[1]
with open(filepath) as fp:
    lines = fp.read().splitlines()

with open(filepath, "w") as fp:
    comment = False
    for line in lines:
        if line.strip().startswith("---"):
            comment = not comment

        if comment or line.strip().startswith("//") or line.strip().startswith("---"):
            print(line.strip(), file=fp)
        elif line.strip() != "":
            print("<p>" + line.strip() + "</p>\n", file=fp)

