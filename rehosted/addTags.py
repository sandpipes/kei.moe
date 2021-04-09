
filepath = "./fanfics/hades_kerbex_the_day_of_the_class_poll_exam.md"
with open(filepath) as fp:
    lines = fp.read().splitlines()

with open(filepath, "w") as fp:
    for line in lines:
        if line.strip() != "":
            print("<p>" + line.strip() + "</p>\n", file=fp)

