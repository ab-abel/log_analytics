# Get log from the machine

#***************** Get all avalable log entries ****************
# use the * wildcard
# Get-EventLog -LogName *


#**************** get current log from Application ***************

# $end = Get-Date -Format "dd/MM/yyyy HH:mm:ss" 
# $start = Get-Date -format "dd/MM/yyyy 00:00:00"

# $todayEvents = Get-EventLog -LogName Application -After $Begin -Before $End

# convert results to json
#  