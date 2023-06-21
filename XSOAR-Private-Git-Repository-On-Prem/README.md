# Private Git Repository for Content Auditing of Hosted XSOAR



## Overview

If you have an hosted XSOAR instance you may be interested in storing your custom 
content in a private GIT repository on premise. This may be accomplished using an XSOAR engine which is NOT running in docker mode to request the zip bundle of custom content from the hosted instance, commits it to a local git repository, and push the repository to full on premises GIT instance such as Gitlab, Bitbucket, etc. 


```


     ┌────────────────────┐
     │                    │
     │                    │
     │    XSOAR           │
     │                    │
     │           ┌────────┤
     │           │  ZIP   │
     └───────────┴─▲─┬────┘
                   │ │                              HOSTED
     ─ ─ ─ ─ ─ ─ ─ ┼ ┼ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
               WSS │ │ ZIP Download                 ON PREM
                   │ │    (API)
                   │ │
     ┌─────────────┴─▼────┐          ┌─────────────────────────┐
     │                    │          │                         │
     │                    │  git     │     GIT Repository      │
     │    XSOAR Engine    ├─────────►│  (Bitbucket, Gitlab,..) │
     │                    │  push    │                         │
     │     ┌──────────────┤          └─────────────────────────┘
     │     │   Local GIT  │
     │     │ Repository   │
     └─────┴──────────────┘



```

## Configuration

NOTE: in the following example BitBucket will be used, but any on premises git based system can be used.


1. Create a linux based XSOAR engine instance on premises which has network access to the BitBucket instance. When you run the installer be sure to specify `-tools=false`.


```
./d1.sh -- -tools=false
```

This prevents Docker from being installed so that the integration commands run on the local engine server OS instead of in the context of a Docker container. This means that the demisto user will execute commands directly against the Python version installed on the linux operating system. You should install Python3 and set it to the default python as this is what XSOAR will use to execute the code.

2. Make Python3 the default for `/usr/bin/python` and ensure Pip is installed locally.

You can check using `which python` and by running `/usr/bin/python --version` to ensure version 3.x is installed and operational. You should also similarly install pip to manage the Python dependencies locally.

Then install the required Python dependencies using pip for XSOAR to function

```
sudo python -m pip install demisto-py
sudo python -m pip install demistoapi
```

3. Add shell for demisto user in `/etc/passwd`

```
demisto:x:111:111::/home/demisto:/bin/bash
```

Add git email and user name (should match setup in on prem BitBucket git instance)

```
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

Then run 

```
git config --global credential.helper store
```


4. Create a new git repository in the on premises BitBucket named `xsoar-content-audit`. Git clone the new repository into the `/tmp/` directory on the XSOAR engine.

```
sudo su demisto
cd /tmp/
git clone <xsoar-content-audit>
```

Add a file or change the README, commit and push to remote repo. Then enter password and username. Now it is stored in the git keychain for use on the engine by the demisto user.

NOTE: Better solution, add SSH keys for the user and SSH key based authentication.

5. Configure the LocalContentExporter integration in XSOAR
Add the hosted server URL and API key from the XSOAR instance into the integration parameters. Add the engine configured above. Test it works.
Run the command `!download-local-content-zip` in the warroom to test loading all the custom content into the on premises repository.



6. Run the playbook as a job in XSOAR to automatically pull the custom content bundle, add it as a commit and push to the internal GIT repository.

The bundle is pulled via the demisto API and then unzipped. The git commands are run via python subprocess module.

FIN!


### References

```

https://stackoverflow.com/questions/35942754/how-can-i-save-username-and-password-in-git

https://gist.github.com/sweenzor/1685717

https://www.liquidweb.com/kb/how-to-install-python-3-on-centos-7/

```



