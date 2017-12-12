from mainClass import mainClass
from functions import *

#initialize
mainClass=mainClass()

#run the tracker
MktValue_track,log_t = track(mainClass)

#output the result()
write_xls(log_t,mainClass.settings)

#output the result(Total Market Value Only)
#write_xls(MktValue_track,mainClass.settings)

#scheduling
#sche(5,track)