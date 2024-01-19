# Get log from the machine

# powershell start-process powershell -verb runas

#***************** Get all avalable log entries ****************
# use the * wildcard
# Get-EventLog -LogName *

#**************** get current log from Application ***************
# get today event
$End = Get-Date -Format "MM/dd/yyyy HH:mm:ss" 
$Begin = Get-Date -format "MM/dd/yyyy 00:00:00"

# $Begin = Get-Date -Date '1/8/2023 08:00:00'
# $End = Get-Date -Date '1/8/2023 17:00:00'
# $todayEvents = Get-EventLog -LogName  $args[0] -After $start -Before $End

# $eventName = $args[0]
$eventName = 'Security'

# $todayEvents =  Get-EventLog -LogName $eventName -After $Begin -Before $End | ConvertTo-Json

# return $todayEvents

if ($eventName -eq 'Secutiry'){
  powershell start-process powershell -verb runas
  $todayEvents =  Get-EventLog -LogName $eventName -After $Begin -Before $End | ConvertTo-Json

  return $todayEvents
}
#**************** output path *************
# $appLogsCsvPath = "C:\Users\hp\Desktop\Abel\ALx\simple_flask_auth\appLogs.json"

#********* convert results to json *************
# $todayEvents | ConvertTo-Json | Out-File $appLogsCsvPath

# Get the event specified in the sub process

# Get the current work directory
# export the result to csv
# Run save the event to the current directory

# $greeting =  "Hello"
# return $greeting


#get last bootup time 
# Get-CimInstance -ClassName win32_operatingsystem | select csname, lastbootuptime

#open poweshelll with admin doings 
# powershell start-process powershell -verb runas