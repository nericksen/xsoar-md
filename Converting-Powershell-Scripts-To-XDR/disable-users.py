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
  Get-LocalUser
  """ % exclude_user

  with open("C:\\Users\\Public\\tmp.ps1", "w") as f:
    f.write(ps)

  result = {}
  try:
    with subprocess.Popen(["powershell.exe", "C:\\Users\\Public\\tmp.ps1"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p:
      stdout, stderr = p.communicate()
      if stderr:
        sys.stderr.write(f"stderr: \n{stderr.decode('utf-8')}\n")
      if stdout:
        sys.stdout.write(f"stdout: \n{stdout.decode('utf-8')}\n")
        result["PSScript"] = stdout.decode('utf-8').splitlines() 
      else:
        result["PSScript"] = None 
    
  except Exception as e:
    sys.stderr.write(f"Failed: {e}")
  
  # Remove the tmp PS file
  os.remove("C:\\Users\\Public\\tmp.ps1")
  return result
