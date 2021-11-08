import subprocess
import sys
import os

def run():

  ps = """
  """

  # Write the PS script to a local tmp file
  with open("C:\\Users\\Public\\tmp.ps1", "w") as f:
    f.write(ps)

  # Execute the tmp PS script
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
    sys.stderr.write(f"Failed: {e} ")
  
  # Remove the tmp PS file
  os.remove("C:\\Users\\Public\\tmp.ps1")
  return result
