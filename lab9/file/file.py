def main():
    fp = open('in.txt', 'r')
    myfile = []
    line_index = 0
    for line in fp:
        line_index += 1
        line = line.strip()
        print("Line {0} ({1} chars): {2}".format(line_index, len(line), line))
    fp.close()

if __name__== '__main__':
    main()
