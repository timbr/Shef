import win32clipboard as w
import win32con
import os, glob, string

try:
    w.OpenClipboard()
    clip=w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    #os.startfile(tq)

    searchstring=clip.rstrip(' ')
    #print 'tim'+'browning'+searchstring[:-2]+'end'
    thing='\\\\Sheffield\\SPD_Data\\_SPD Drawings\\1.1.Issued (DIN)\\*\\*'+searchstring[:-2]+'*' # slice -2 to remove space and endline
    #print thing
    filepaths=glob.glob(thing)
    print
    #print type(searchstring)
    #print filepaths
    num=0
    for filepath in filepaths:
        filename = filepath.split('\\')[-1:]
        #print filename[0]
        print num,
        print " >>", filename[0]
        num+=1

    print
    print "Type a number to open the corresponding file,"
    print "or press return to exit"

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
	
except:
    pass