import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if os.path.exists(storage_path):
  with open(storage_path, 'r') as f:
    dic = json.load(f)
else:
  dic={}

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

if args.key!=None and args.val!=None:
  if args.key not in dic:
    dic[args.key] = [args.val]
  else:
    dic[args.key].append(args.val)

elif args.key!=None and args.val==None:
  if args.key not in dic:
    print(None)
  else:
    print(*dic[args.key], sep=', ')
#    print(', '.join(dic[args.key]))

with open(storage_path, 'w') as f:
  json.dump(dic, f)

#storage.py --val беляков --key миша
#storage.py --key миша
