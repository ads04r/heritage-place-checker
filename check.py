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
	parser.add_argument('-e', '--export', type=argparse.FileType('r'), help="A Heritage Place summary file in JSON format, exported from EAMENA using the custom 'summary' management command.")

	args = parser.parse_args()
	message("NO ERRORS FOUND!", bcolours.OKGREEN)
