import argparse
import subprocess


parser = argparse.ArgumentParser(description="""Take the first line of a file and copy it to the clipboard 
    and pasting it into another program like excel with newlines""")
parser.add_argument('-d','--delimiter', default=',', type=str)
parser.add_argument('file')


def print_and_copy():
    args = vars(parser.parse_args())
    with open(args['file'], 'r') as open_file:
        first_line = open_file.readline()
    line_entries = first_line.split(args['delimiter'])
    out_text =  '\n'.join(line_entries)
    write_to_clipboard(out_text)
    print out_text

def write_to_clipboard(output):
    """
    credit: https://stackoverflow.com/questions/1825692/can-python-send-text-to-the-mac-clipboard
    """
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

if __name__ == "__main__":
    # execute only if run as a script
    print_and_copy()