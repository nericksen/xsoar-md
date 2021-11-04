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
