import json, argparse, sys

class bcolours:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def message(text, colour=None):

	if colour is None:
		sys.stderr.write(f'{text}\n')
	else:
		sys.stderr.write(f'{colour}{text}{bcolours.ENDC}\n')

if __name__ == "__main__":

	parser = argparse.ArgumentParser(prog="heritage-place-checker", description="A quick and dirty script to check for duplicate IDs in the Heritage Places of the EAMENA database.")
	parser.add_argument('-s', '--summary', type=argparse.FileType('r'), required=True, help="A Heritage Place summary file in JSON format, exported from EAMENA using the custom 'summary' management command.")

	args = parser.parse_args()

	data = json.load(args.summary)
	byid = {}
	noid = []
	multipleid = []
	for uuid, item in data.items():
		if 'ID' in item:
			if not item['ID'] in byid:
				byid[item['ID']] = []
			byid[item['ID']].append(uuid)
		else:
			noid.append(uuid)
	for id, uuids in byid.items():
		if len(uuids) < 2:
			continue
		multipleid.append([id, uuids])

	if len(noid) + len(multipleid) == 0:
		message("NO ERRORS FOUND!", bcolours.OKGREEN)
		sys.exit(0)

	if len(noid) > 0:
		message("The following " + str(len(noid)) + " items have no EAMENA ID:")
		for uuid in noid:
			message(" * " + uuid, colour=bcolours.WARNING)

	if len(multipleid) > 0:
		message("The following " + str(len(multipleid)) + " items have multiple EAMENA IDs:")
		for item in multipleid:
			id = item[0]
			uuids = item[1]
			message(" * " + id, colour=bcolours.WARNING)
			for uuid in uuids:
				message("   " + uuid, colour=bcolours.WARNING)

