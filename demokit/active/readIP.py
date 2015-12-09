import sys

def printCurl(filename):
  filehandle = open(filename, "rt")
  i = 0;
  for line in filehandle:
    curlString = 'curl --data "comment=' + str(i) + '" ' + "'" + line + "'"

    print curlString.replace("\n", "")
    i += 1



# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 2:
    print 'usage: ./readIP.py file'
    sys.exit(1)

  filename = sys.argv[1]
  printCurl(filename)

if __name__ == '__main__':
  main()