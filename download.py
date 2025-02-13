import os
import argparse
import subprocess

parser = argparse.ArgumentParser("Monolingual text stream download.")
parser.add_argument("--lang",
                     nargs='*',
                     default=["bn", "sw"], 
                     help="List of language that you want to extract. Add \"all\" to download full corpush. Value-type: list(lang code)")
parser.add_argument("--force-download",
                    action="store_true",
                    help="Force download if the data exists in the folder. Value-type: (str)")
parser.add_argument("--extract",
                    action="store_true",
                    help="Force download if the data exists in the folder. Value-type: (str)")
parser.add_argument("--delete-compressed",
                    action="store_true",
                    help="Delete the compressed source files. Value-type: (str)")
parser.add_argument("--folder",
                    default="data", 
                    type=str, 
                    help="Folder where will be data downloaded. Value-type: (str)")
parser.add_argument("--source-url",
                    default="http://data.statmt.org/cc-100/{}.txt.xz", 
                    type=str, 
                    help="Source url address. Value-type: (str)")
parser.add_argument("--corpus-dict",
                    default="corpus-data.txt", 
                    type=str, 
                    help="Source url address. Value-type: (str)")
args = parser.parse_args()


content = []
flag = "all" in args.lang
with open(args.corpus_dict) as filePtr:
    for line in filePtr:
        line=line.strip().split(" ", 1)
        lang, desc = line[0], line[1]
        content.append((lang,desc))

os.makedirs(args.folder, exist_ok = True)

for lang, desc in content:
    if lang in args.lang or lang.split("_") in args.lang or flag:
        if args.force_download or not os.path.exists(os.path.join(args.folder, "{}.txt.xz".format(lang))):
            print("Downloading ... : {} {}".format(lang, desc))
            cmd = "wget " + args.source_url.format(lang) + "  -P {}".format(args.folder)
            print("Running cmd: {}".format(cmd))
            subprocess.check_output(cmd, shell=True)
        if args.extract and os.path.exists(os.path.join(args.folder, "{}.txt.xz".format(lang))):
            cmd = "xz -d {}".format(os.path.join(args.folder, "{}.txt.xz".format(lang)))
            print("Running cmd: {}".format(cmd))
            subprocess.check_output(cmd, shell=True)
        if args.delete_compressed and os.path.exists(os.path.join(args.folder, "{}.txt.xz".format(lang))):
            cmd = "rm {}".format(os.path.join(args.folder, "{}.txt.xz".format(lang)))
            print("Running cmd: {}".format(cmd))
            subprocess.check_output(cmd, shell=True)