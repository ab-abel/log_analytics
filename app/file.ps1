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

$eventName = $args[0]
# $eventName = 'Security'

$todayEvents =  Get-EventLog -LogName $eventName -After $Begin -Before $End | ConvertTo-Json

return $todayEvents

# if ($eventName -eq 'Security'){
# powershell start-process powershell -verb runas
# $todayEvents =  Get-EventLog -LogName $eventName -After $Begin -Before $End | ConvertTo-Json

# return $todayEvents
# }
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


# Filter for logon events in the Security log
# $logonEvents = Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4624 or EventID=4625]]" -MaxEvents 50

# Display the relevant information for each logon event
# foreach ($event in $logonEvents) {
#     $time = $event.TimeCreated
#     $userName = $event.Properties[5].Value
#     $logonType = $event.Properties[8].Value
#     $logonStatus = $event.Properties[10].Value

#     Write-Host "Time: $time - User: $userName - Logon Type: $logonType - Logon Status: $logonStatus"
# }
# return $time


# run script on admin mode using start process

# $out = Start-Process powershell  -Verb RunAs
# $out>>'hello'