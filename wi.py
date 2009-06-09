#
# wi.py
# 
import getopt, sys, glob, string, os

#print a short help message
def usage():
    sys.stderr.write("""
  -------------------------------------------------------
  Shef - Find Work Instructions on Sheffield.
  -------------------------------------------------------
  Tim Browning 11/12/2008


  USAGE: %s <part of filename>

  Searches: \\\\Sheffield\\SPD_Data\\Production\\Production_ Documents\\Work_Instructions\\WI Issued\\*
  
  Wildcards accepted: * and ?


""" % (sys.argv[0], ))

if __name__ == '__main__':
    #parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:],"",)
    except getopt.GetoptError:
        # print help information and exit:
        usage()
        sys.exit(2)

    if  len(args) == 1:
        searchstring = args[0]
        filepaths=glob.glob('\\\\Sheffield\\SPD_Data\\Production\\Production_ Documents\\Work_Instructions\\WI Issued\\*'+searchstring+'*')
        print
        num = 0
        for filepath in filepaths:
            filename = filepath.split('\\')[-1:]
            print num, ">>>", filename[0]
            num+=1

        print
        print "Type a number to open the corresponding file,"
        print "or press return to exit."

        z=raw_input()
        try:
            number=int(z)
        except:
            print "bye"
        else:
            #system(filepaths[int(z)])
            print
            path = filepaths[number]
            sam='Z:\\tb126975\\scripts\\automation\\open.exe '+'"%s"' % (path)
            #bob=sam.replace("\\", "\\\\")
            print
            print "opening ..."
            print
            print sam
            os.system(sam)

    else:
        usage()
        sys.exit(2)
        
