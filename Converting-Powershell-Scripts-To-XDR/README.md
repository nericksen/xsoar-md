# Powershell Scripts from XDR

XDR has a powerful ability to run Python scripts on an endpoint.
Many users from the Windows perspective use Powershell today.

By creating a Python wrapper around these Powershell scripts it is 
possible to leverage existing Powershell scripts.

Attached to this repo is `disable-users.py` script. It can be uploaded into 
XDR and run on a specified endpoint.

A user to exlcude can be passed as an arguement.

The entry point should be specified as the `run` function.

The Powershell script is wrapped in a string.
Arguments can be passed to the PS script using %s string formatting syntax in Python.

A temporary PS file is then written to the endpoints disk and run before being deleted.
It would also be possible to run this as base64 encoded commands presumably in order to 
remove the need to write to disk.

```
import subprocess, sys
import os

def run(exclude_user):

  ps = """
  $excludeUser = "%s"

  $allUsers = Get-LocalUser

  foreach ($user in $allUsers.Name) {
    if($user -ne $excludeUser) {
      Get-LocalUser $user | Disable-LocalUser
    }
  }
  """ % exclude_user

  with open("C:\\Users\\Public\\tmp.ps1", "w") as f:
    f.write(ps)

  p = subprocess.Popen(["powershell.exe", 
                "C:\\Users\\Public\\tmp.ps1"], 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  stdout, stderr = p.communicate()

  os.remove("C:\\Users\\Public\\tmp.ps1")
  return stdout if stdout else stderr
```
