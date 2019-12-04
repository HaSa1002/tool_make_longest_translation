import argparse
parser = argparse.ArgumentParser(description="Searchs and writes the longest Entry in a CSV Translation File. Useful for UI Testing")
parser.add_argument('file', help="The Source CSV Translation File")
parser.add_argument('-out', help="The Output CSV Translation File. Content will be overwritten. If omitted, the output will be written into the source file", default="")
parser.add_argument('-delim', help="The delimeteting character. Default: ;", default=';')
parser.add_argument('-code', help="The language code in which the longest entries are saved. Default: aa", default="aa")
args = parser.parse_args()

res = ""
first = True

with open(args.file, "r") as f:
    for line in f:
        if first:
            res = line.strip("\n") + args.delim + args.langcode +"\n"
            first = False
            continue
        entries = line.strip("\n").split(args.delim)
        length = 0
        skip_key = True
        longest_string = ""
        for e in entries:
            if skip_key:
                skip_key = False
                continue
            if len(e) > length:
                length = len(e)
                longest_string = e
        res += line.strip("\n") + args.delim +longest_string+"\n"

if args.out == "":
    of = args.file
else:
    of = args.out

with open(of, "w") as f:
    f.write(res)

