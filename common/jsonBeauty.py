#!/usr/bin/python

import json,sys,os
cur_path = os.getcwd()


def main(jsonFile):
	try:
		json_path = os.path.abspath(jsonFile)
		with open(json_path) as f:
			data = json.loads(f.read())
	except:
		usage()
		sys.exit(1)
	json_path = os.path.abspath(jsonFile)
	with open(json_path, 'w') as f:
		f.write(json.dumps(data, sort_keys=False, ensure_ascii=True, indent=4, separators=(', ', ': ')))


def usage():
	usageInfo = '''[ERROR] Wrong params , please check follows:
Usage:
	python %s {jsonFile}
e.g.
	python %s C:/Users/administrator/passwd.json
	''' % (sys.argv[0], sys.argv[0])
	print(usageInfo)
	sys.exit(1)


if __name__ == '__main__':
	jsonFile = sys.argv[1] if len(sys.argv) > 1 else usage()
	main(jsonFile)