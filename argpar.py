import argparse, requests as rr

parser = argparse.ArgumentParser(description='THIS IS DEMO TOOL')
parser.add_argument('-url',type=str, help="Provide URL", required=True)
parser.add_argument('-o',type=str, help="Provide output file name", required=False)

args = parser.parse_args()
with open(f"{args.o}","w") as f:
    data = rr.get(args.url, timeout=10, allow_redirects=True)
    f.write(str(data.status_code))