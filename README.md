# GSEUK22_ansible101

Repository for Ansible 101 course with hands on activities

## Infra as Code approach

Usually our changes to infrastructure has to happen out of business hours, is common to have complex tasks to be executed on weekend evenings. Looking for an automated process where we can avoid human errors we map our activities, the configuration, our infrastructure.

The coding of our infrastructure will be the input of the automation tool we use, in this case we will have Ansible as our tool.

There are 2 types of IaC, declaratve and imperative.

The declarative approach

## Quick introduction to Ansible engines

Ansible is an automation engine that can be used across multiple platforms for cloud provision, network management, application deployment and orchestration. Recently IBM has addeed to the vast se of Options it has, specific modules for Mainframe environment.

It help us adopt to bring infrastructure as code. Let's take a scenario wher we have to execute multiple tasks during a maintenance period, usually this is out of business hours. If we can create a receipt, a step by step instructions of the tasks we need to create, we can add this tasks into a file called `playbook`. It then can be executed across multiple environments saving us time and helping to avoid human errors.

To be able to replicate this actions Ansible will find all servers, hosts from the `Inventory`. It could be a static file, or it could be sourced from an online CMDB.

On it's engine, Ansible have some structure that encapsulate functions to help us, some modules and plugins that have the scripts needed for specific action, and all we need to do is provide the data for this to run, to go to our hosts through an `SSH - Secure Shell` connection. This is in fact other advantage of Ansible, it doesnt need to have an agent installed on the hosts it will manage.

https://docs.ansible.com/ansible-core/2.19/index.html

## Getting started with our environment

To avoid any local installation, we will use the codeanywhere: https://app.codeanywhere.com/

Let's create the workspace using this github repository as base: https://github.com/phil34130/GSEUK22_ansible101.

For mainframe practices we will use an id on ZXplore: https://ibmzxplore.influitive.com/

With credentials in hand, add execution flag to script `get_started.sh` and then execute it passing your userid `zxxxxx`. After it starts it will ask for your password.

```
codeany ➜ /workspaces/GSEUK22_ansible101 (main) $ chmod +x get_started.sh
codeany ➜ /workspaces/GSEUK22_ansible101 (main) $ ./get_started.sh
MF USERID:
Password:
```

After the scripts ends, you can see the ansible config of your environment with `ansible --version`:

```
pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  sshpass
0 upgraded, 1 newly installed, 0 to remove and 147 not upgraded.
Need to get 11.7 kB of archives.
After this operation, 35.8 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 sshpass amd64 1.09-1 [11.7 kB]
Fetched 11.7 kB in 0s (408 kB/s)   
debconf: unable to initialize frontend: Dialog
debconf: (Dialog frontend requires a screen at least 13 lines tall and 31 columns wide.)
debconf: falling back to frontend: Readline
Selecting previously unselected package sshpass.
(Reading database ... 41869 files and directories currently installed.)
Preparing to unpack .../sshpass_1.09-1_amd64.deb ...
Unpacking sshpass (1.09-1) ...
Setting up sshpass (1.09-1) ...
Processing triggers for man-db (2.10.2-1) ...
Defaulting to user installation because normal site-packages is not writeable
Collecting ansible
  Downloading ansible-10.7.0-py3-none-any.whl (51.6 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 51.6/51.6 MB 50.0 MB/s eta 0:00:00
Collecting ansible-core~=2.17.7
  Downloading ansible_core-2.17.14-py3-none-any.whl (2.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.2/2.2 MB 112.5 MB/s eta 0:00:00

     ```
Enter: ansible --version
ansible --version
ansible [core 2.17.14]
  config file = None
  configured module search path = ['/home/codeany/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/codeany/.local/lib/python3.10/site-packages/ansible
  ansible collection location = /home/codeany/.ansible/collections:/usr/share/ansible/collections
  executable location = /home/codeany/.local/bin/ansible
  python version = 3.10.12 (main, Sep 11 2024, 15:47:36) [GCC 11.4.0] (/usr/bin/python3)
  jinja version = 3.1.6
  libyaml = True

And the inventory with data for the ZXplore lpar will be ready.
you can verify your inventory.yaml file that has been populated withy your zexplore credentials and IP address
all:
  hosts:
    zxplore:
      ansible_user: Zxxxxx
      ansible_password: pppppppp
      ansible_host: 204.90.115.200
      PYZ: "/usr/lpp/IBM/cyp/v3r9/pyz"
      ZOAU: "/usr/lpp/IBM/zoautil"
      ansible_ssh_common_args: "-o StrictHostKeyChecking=no"
      ansible_python_interpreter: /usr/lpp/IBM/cyp/v3r9/pyz/bin/python3
      environment_vars:
        _BPXK_AUTOCVT: "ON"
        ZOAU_HOME: "{{ ZOAU }}"
        PYTHONPATH: "{{ ZOAU }}/lib"
        LIBPATH: "{{ ZOAU }}/lib:{{ PYZ }}/lib:/lib:/usr/lib:"
        PATH: "{{ ZOAU }}/bin:{{ PYZ }}/bin:/bin:/var/bin"
        _CEE_RUNOPTS: "FILETAG(AUTOCVT,AUTOTAG) POSIX(ON)"
        _TAG_REDIR_ERR: "txt"
        _TAG_REDIR_IN: "txt"
        _TAG_REDIR_OUT: "txt"
        _CC_LIB_PREFIX: "SYS1"
        LANG: "C"


```
## Ansible AD HOC Commands: test create a  new local folder
codeany ➜ /workspaces/GSEUK22_ansible101 (main) $ ansible localhost -m file -a "path=./test_folder state=directory"

[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | CHANGED => {
    "changed": true,
    "gid": 1000,
    "group": "codeany",
    "mode": "0755",
    "owner": "codeany",
    "path": "./test_folder",
    "size": 10,
    "state": "directory",
    "uid": 1000
}


## Ansible AD HOC Commands: test a local shell command
ansible localhost -m shell -a "ls -al"
[WARNING]: No inventory was parsed, only implicit localhost is available
localhost | CHANGED | rc=0 >>
total 208
drwxr-xr-x 6 codeany codeany  4096 Nov 17 16:40 .
drwxr-xr-x 3 root    root       40 Nov 17 16:14 ..
-rw-r--r-- 1 codeany codeany  4242 Nov 17 16:13 active_tasks
-rw-r--r-- 1 codeany codeany   805 Nov 17 16:13 active_tasks.yaml
-rw-r--r-- 1 codeany codeany   765 Nov 17 16:13 convert_text.yaml
-rw-r--r-- 1 codeany codeany  4576 Nov 17 16:13 copy_edit_submit.yaml
-rw-r--r-- 1 codeany codeany   405 Nov 17 16:13 copy_local_dir_to_pds.yaml
-rw-r--r-- 1 codeany codeany   655 Nov 17 16:13 copy_member.yaml
-rw-r--r-- 1 codeany codeany   645 Nov 17 16:13 copy_parmlib_member.yaml
-rw-r--r-- 1 codeany codeany   316 Nov 17 16:13 copy_to_dataset.yaml
-rw-r--r-- 1 codeany codeany   336 Nov 17 16:13 copy_to_uss.yaml
-rw-r--r-- 1 codeany codeany  1356 Nov 17 16:13 create_dataset_and_listcat.yaml
-rw-r--r-- 1 codeany codeany   326 Nov 17 16:13 dataset_allocate.yaml
drwxr-xr-x 2 codeany codeany   139 Nov 17 16:13 files
-rw-r--r-- 1 codeany codeany  3752 Nov 17 16:13 gather_facts.yaml
-rwxr-xr-x 1 codeany codeany  1802 Nov 17 16:13 get_started.sh
drwxr-xr-x 7 codeany codeany   190 Nov 17 16:28 .git
-rw-r--r-- 1 codeany codeany   485 Nov 17 16:13 hello.yaml
-rw-r--r-- 1 codeany codeany   769 Nov 17 16:29 inventory.yaml
-rw-r--r-- 1 codeany codeany   768 Nov 17 16:13 inventory.yaml.ref
-rw-r--r-- 1 codeany codeany  1058 Nov 17 16:13 iplinfo
-rw-r--r-- 1 codeany codeany   569 Nov 17 16:13 iplinfo_device.yaml
-rw-r--r-- 1 codeany codeany    96 Nov 17 16:13 job1.jcl
-rw-r--r-- 1 codeany codeany    96 Nov 17 16:13 job2.jcl
-rw-r--r-- 1 codeany codeany   845 Nov 17 16:13 mvs_command.yaml
-rw-r--r-- 1 codeany codeany   121 Nov 17 16:13 ping.yaml
-rw-r--r-- 1 codeany codeany 19668 Nov 17 16:13 README.md
-rw-r--r-- 1 codeany codeany   859 Nov 17 16:13 restart.yaml
-rw-r--r-- 1 codeany codeany  2862 Nov 17 16:13 run_rexx_and_clist.yaml
-rw-r--r-- 1 codeany codeany  1990 Nov 17 16:13 sample_job_role_complete.yaml
-rw-r--r-- 1 codeany codeany  1818 Nov 17 16:13 smpe_list_sysmod.yaml
-rw-r--r-- 1 codeany codeany  1087 Nov 17 16:13 submit_job2.yaml
-rw-r--r-- 1 codeany codeany   625 Nov 17 16:13 submit_job.yaml
-rw-r--r-- 1 codeany codeany  1509 Nov 17 16:13 submit_query_output_by_id.yaml
-rw-r--r-- 1 codeany codeany 10082 Nov 17 16:13 submit_query_retrieve.yaml
-rw-r--r-- 1 codeany codeany   898 Nov 17 16:13 system_discover.yaml
drwxr-xr-x 2 codeany codeany    54 Nov 17 16:13 templates
-rw-r--r-- 1 codeany codeany   791 Nov 17 16:13 templating-2.yaml
-rw-r--r-- 1 codeany codeany   708 Nov 17 16:13 templating_submit_job_and_get_output.yaml
-rw-r--r-- 1 codeany codeany   862 Nov 17 16:13 templating.yaml
drwxr-xr-x 2 codeany codeany    10 Nov 17 16:40 test_folder
-rw-r--r-- 1 codeany codeany  5907 Nov 17 16:13 uri_sample.yaml
-rw-r--r-- 1 codeany codeany   678 Nov 17 16:13 vars_n_cond.yaml
-rw-r--r-- 1 codeany codeany  5601 Nov 17 16:13 workflow_basic.yaml
-rw-r--r-- 1 codeany codeany  2021 Nov 17 16:13 zosmf_dslist.yaml
-rw-r--r-- 1 codeany codeany  3280 Nov 17 16:13 zosmf_submit_job.yaml
-rw-r--r-- 1 codeany codeany   871 Nov 17 16:13 zowe.config.json

## Ansible test ping : using inventory.yaml
codeany ➜ /workspaces/GSEUK22_ansible101 (main) $  ansible -i inventory.yaml zxplore -m ping
zxplore | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

## Ansible Playbooks

### YAML - YAML ain't markup language

So now you are probably asking how do we provide these instructions for Ansible, how we provide these data?

The language we use is the YAML, that stands for YAML Ain't Markup Language, it's a data serialization language often used for writing configuration files.

Let's take a look on how we can get started with YAML files. One of the things that is very common is to have pairs `key: value`.

```
key: value
name: Tony
age: 35
date: 13-07-2022
member_of_gse: true
```

One important thing about YAML files, it's oriented by identation, so let's look other example:

```
gse_member:
  name: Tony
  start_date: 13-07-2022
  talk: Zowe
```

Now when we use the identation, we transformed all those keys(name, start_date, speciality) into properties of gis_team_member, this is similar to when we add a object as property of a key in JSON.

If we need to represent a list of team members on this YAML, all we need is make use of `-` and the identation

```
gis_team_member:
  - name: Tony
    start_date: 13-07-2022
    talk: Zowe

  - name: Sylvia
    start_date: 1-06-2021
    talk: DB2
```

This gives a basic understanding for us to continue, but more detailed documentation can be found on:

https://yaml.org/spec/1.2.2/

## Setup

During the `get_started.sh` we have added all requirements for our hands on in this environment, `python` and `ansible`.

Together to facilitate we have added the following extensions:

```
Zowe - to verify the files we will be handling in ZXplore
Ansible - For highligh in our playbooks
indent-rainbow - To highlight identation
```

In the z/OS, all we need to have available is `python`, `Z Open Automation Utilities` and `OpenSSH`. The path for Python and ZOAU is already included on the inventory created by the get_started script.

## Our first play

Here we have already our first playbook to get started, the `ping.yaml` that will use the same module we have used together with adhoc command.

```
---
  - hosts: zxplore
    gather_facts: no
    tasks:
      - name: Testing connection with zxplore
        ansible.builtin.ping:
```

This playbook is pointing with what target host we are running these tasks against, and under the tasks we have only the `ping` module that allow us check our connection. To run that use `ansible-playbook -i inventory.yaml ping.yaml`

```
codeany ➜ /workspaces/GSEUK22_ansible101 (main) $ ansible-playbook -i inventory.yaml ping.yaml --key-file "./zxplore_id"

PLAY [zxplore] *************************************************************************************************************************************************

TASK [Testing connection with zxplore] *************************************************************************************************************************
ok: [zxplore]

PLAY RECAP *****************************************************************************************************************************************************
zxplore                    : ok=1    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
```

## Adding our first collection

So let's explore the first z/OS module, adding our ibm_core_zos collections and playing with zos_copy:
https://ibm.github.io/z_ansible_collections_doc/ibm_zos_core/docs/source/modules/zos_copy.html

0- Install the zOS  Collection with `ansible-galaxy collection install ibm.ibm_zos_core:*`

```
➜ ansible-galaxy collection install ibm.ibm_zos_core
ansible-galaxy collection install ibm.ibm_zos_core
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Downloading https://galaxy.ansible.com/api/v3/plugin/ansible/content/published/collections/artifacts/ibm-ibm_zos_core-1.15.0.tar.gz to /home/codeany/.ansible/tmp/ansible-local-4973a99yo6f_/tmp9cxodqg6/ibm-ibm_zos_core-1.15.0-ggqy46po
Installing 'ibm.ibm_zos_core:1.15.0' to '/home/codeany/.ansible/collections/ansible_collections/ibm/ibm_zos_core'
ibm.ibm_zos_core:1.15.0 was installed successfully
```
➜ Install the z/OSMF Collection with `ansible-galaxy collection install ibm.ibm_zosmf`
```
ansible-galaxy collection install ibm.ibm_zosmf
ansible-galaxy collection install ibm.ibm_zosmf
Starting galaxy collection install process
Process install dependency map
Starting collection install process
Downloading https://galaxy.ansible.com/api/v3/plugin/ansible/content/published/collections/artifacts/ibm-ibm_zosmf-1.5.0.tar.gz to /home/codeany/.ansible/tmp/ansible-local-50450luki0wo/tmpymo1xm84/ibm-ibm_zosmf-1.5.0-9e63ra6t
Installing 'ibm.ibm_zosmf:1.5.0' to '/home/codeany/.ansible/collections/ansible_collections/ibm/ibm_zosmf'
ibm.ibm_zosmf:1.5.0 was installed successfully
```

➜ Open file hello.yaml
1- You will have to add the collections to the playbook and the zos environment vars.

```
  environment: "{{ environment_vars }}"
  collections:
    - ibm.ibm_zos_core
    - ibm.ibm_zosmf
```

2- and add a task to copy content to a file in USS

```
    - name: "Copy from content to file"
      ibm.ibm_zos_core.zos_copy:
        content: "Hello World"
        dest: /z/zxxxx/hello_from_GSE
```

3- Add a task to copy content to a dataset

```
    - name: "Copy from content to dataset"
      ibm.ibm_zos_core.zos_copy:
        content: "Hello World"
        dest: Zxxxx.ANSB.HELLO.GSE
```
➜ Now invoke this playbook with:
ansible-playbook -i inventory.yaml hello.yaml 

 ansible-playbook -i inventory.yaml hello.yaml 

PLAY [zxplore] *************************************************************************************************************************************************

TASK [Testing connection with zxplore] *************************************************************************************************************************
ok: [zxplore]

TASK [Copy from content to file] *******************************************************************************************************************************
ok: [zxplore]

TASK [Copy from content to dataset] ****************************************************************************************************************************
changed: [zxplore]

PLAY RECAP *****************************************************************************************************************************************************
zxplore                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

You can verify on your TSO session Z04683.ANSIBLE.TEST1
 BROWSE    Z04683.ANSIBLE.TEST1  
*********************************
Hello World                      
******************************** 


➜ Open copy_parmlib_member.yaml
1- Lets now change it, Lets create a copy of our active IEASYS00 to USERID.ANSB.PARMLIB, first allocate the PDS with `zos_data_set` module.

```
    - name: "Allocate Zxxxx.ANSB.PARMLIB"
      ibm.ibm_zos_core.zos_data_set:
        name: Zxxxx.ANSB.PARMLIB
        type: PDS
        state: present
```

2- Copy SYS1.PARMLIB(IEASYS00) to USERID.ANSB.PARMLIB.

```
    - name: "COPY IEASYS00"
      ibm.ibm_zos_core.zos_copy:
        src: "LVL0.PARMLIB(IEASYS00)"
        dest: Zxxxx.ANSB.PARMLIB(IEASYS00)
        remote_src: true
```

## Variables

To make that re-usable we may want to have the member name as variable for example, or the dataset name. This is something we can do with variables/facts in the playbook in several ways.

The variables could be defined in the playbook under `vars`, we can have this also under specific task. It could be defined used `set_fact`, in the iventory, there are several ways, and based on how it is defined we have a precedence for them (the last listed variables override all other variables):

```
command line values (for example, -u my_user, these are not variables)
role defaults (defined in role/defaults/main.yml)
inventory file or script group vars
inventory group_vars/all
playbook group_vars/all
inventory group_vars/*
playbook group_vars/*
inventory file or script host vars
inventory host_vars/*
playbook host_vars/*
host facts / cached set_facts
play vars
play vars_prompt
play vars_files
role vars (defined in role/vars/main.yml)
block vars (only for tasks in block)
task vars (only for the task)
include_vars
set_facts / registered vars
role (and include_role) params
include params
extra vars (for example, -e "user=my_user")(always win precedence)
```

The variable can NOT be named starting with number, have `space`, `.` or `-`. Neither use python or playbook keywords.

3 - So now, instead of keeping your parmlib, the copy and the member hardcoded on the playbook, use as a variable defining them as `play vars`.

```
  vars:
    src_library: "LVL0.PARMLIB"
    target_library: "Z12309.ANSB.PARMLIB"
    member: "IEASYS00"
```

To reference that we will use Jinja2 format, including the var inside of double curly braces `{{ var_name }}`

https://jinja.palletsprojects.com/en/3.1.x/

4 - Now update your tasks:

```
---
- name: Creating a copy of parmlib member
  hosts: zxplore
  gather_facts: false
  environment: "{{ environment_vars }}"
  collections:
    - ibm.ibm_zos_core
  vars:
    src_library: "LVL0.PARMLIB"
    target_library: "Zxxxx.ANSB.PARMLIB"
    member: "IEASYS00"
  tasks:
    - name: "Allocate our parmlib copy dataset"
      ibm.ibm_zos_core.zos_data_set:
        name: "{{ target_library }}"
        type: PDS
        state: present

    - name: "COPY IEASYS00"
      ibm.ibm_zos_core.zos_copy:
        src: "{{ src_library }}({{ member }})"
        dest: "{{ target_library }}({{ member }})"
        remote_src: true

```
➜Now invoke this playbook with:
 
ansible-playbook -i inventory.yaml copy_parmlib_member.yaml 

PLAY [Creating a copy of parmlib member] ***********************************************************************************************************************

TASK [Allocate our parmlib copy dataset] ***********************************************************************************************************************
ok: [zxplore]

TASK [COPY IEASYS00] *******************************************************************************************************************************************
changed: [zxplore]

PLAY RECAP *****************************************************************************************************************************************************
zxplore                    : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

you can verify on TSO the content of Z04683.ANSB.PARMLIB(IEASYS00)
 BROWSE    Z04683.ANSB.PARMLIB(IEASYS00)            Line 0000000000 Col 00
********************************* Top of Data ****************************
CLPA,                                                                     
REAL=280,                    ALLOWS 2 64K JOBS OR 1 128K JOB TO RUN V=R   
RSU=0,                       NO RECONFIG STORAGE UNITS          DEFAULT   
VRREGN=140                   DEFAULT REAL-STORAGE REGION SIZE             
******************************** Bottom of Data **************************

➜ Open iplinfo_device.yaml
1- Let's now play with the `set_fact` option and `lookup` to read our `iplinfo` file, and take decisions based on this output. We are doing it instead of using the zos command cause we don't have authority to issue commands on this lpar.

```
    - name: Getting content of iplinfo file
      ansible.builtin.set_fact:
        iplinfo: "{{ lookup('file', 'iplinfo') }}"

```

Manipulate strings is very useful tool, for example we could take from thee facts information about current columes to prepare a whole process for alternates volumes. To practice let's use `regex_findall`.

2 - Use `set_fact` and `regex_findall` to get the IPL Address from our IPLINFO output. To display your results use `debug` module

```
    - name: Find IPL Address
      ansible.builtin.set_fact:
        ipladdress: "{{ iplinfo | regex_findall('(IPL DEVICE: ORIGINAL\\()(.*?)\\)') }}"
```

3 - To complete it let's use this variable in a message to display the IPL DEVICE:

```
    - name: Find IPL Address
      ansible.builtin.set_fact:
        ipladdress: "{{ iplinfo | regex_findall('(IPL DEVICE: ORIGINAL\\()(.*?)\\)') }}"

    - name: Displaying var
      ansible.builtin.debug:
        msg: "The last IPL was on address {{ ipladdress[0][1] }}"

➜Now invoke this playbook with:
 
ansible-playbook -i inventory.yaml iplinfo_device.yaml 

TASK [Getting content of iplinfo file] *********************************************************************************
ok: [zxplore]

TASK [Find IPL Address] ************************************************************************************************
ok: [zxplore]

TASK [Displaying var] **************************************************************************************************
ok: [zxplore] => {
    "msg": "The last IPL was on address 01000"
}

PLAY RECAP *************************************************************************************************************
zxplore                    : ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
``
➜Now Open file copy_local_dir_to_pds.yaml, which will copy the local files under /files as members of your userid.ANSB.JCL PDS dataset. 
Invoke the playbook with:  ansible-playbook -i inventory.yaml copy_local_dir_to_pds.yaml 
ansible-playbook -i inventory.yaml copy_local_dir_to_pds.yaml 

PLAY [zxplore] *************************************************************************************************************************************************

TASK [Copy local directory /workspaces/GSEUK22_ansible101/files to Z04683.ANSB.JCL] ****************************************************************************
changed: [zxplore]

PLAY RECAP *****************************************************************************************************************************************************
zxplore                    : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

➜Now check on TSO the content of Z04683.ANSB.JCL   
 BROWSE            Z04683.ANSB.JCL    
            Name     Prompt       Size
 _________ CLIST                      
 _________ DSINFO                     
 _________ HELLO                      
 _________ RXSAY                      
 _________ UPTIME                     
           **End**                    

## Looping and Conditions
➜Now Open file active_tasks.yaml

We also have the hability as in other programming languages, to work with loops and conditions.

To get started let's create a PDS `USERID.ANSB.JCL` and add this 2 JCLs:

```
JOB1
//JCL1    JOB 1
//***************************************************/
//HELLO  EXEC PGM=IEFBR14


JOB2
//JCL1    JOB 1
//***************************************************/
//HELLO  EXEC PGM=IEFBR14

```

Now let's imagine we just want to run these 2 jobs in case a specific task, `ZWE1AC` is NOT up.

We could `zos_operator` to display all active tasks and register in `active_tasks` variable, but as we don't have access to issue commands, let's have it like task before reading from active_tasks file.

```
    - name: "Checking active tasks"
      ibm.ibm_zos_core.zos_operator:
        cmd: D A,L
      register: active_tasks
```

1 - Set the variables `task_to_search` that we want, and `active_tasks` to hold the results of the command

```
    - name: Setting variables
      ansible.builtin.set_fact:
        active_tasks: "{{ lookup('file', 'active_tasks') }}"
        task_to_search: ZWE1AC
```

Now to evaluate a condition we are going to use `when`, it let us work with traditional operators, example `==`, `>`... and also with other special operators, example `in`, `not in` like in python.

So it allow us to use the following condition to submit or not our jobs:

```
when: task_to_search in command_result
```

3 - Now we can use the `zos_job_submit` to submit our JCLs. There are different manners for that, we will play with `with_items`. This execute our task for each item on the list.

```
    - name: Submitting maintenance jobs
      ibm.ibm_zos_core.zos_job_submit:
        src: "{{ item.dsn }}({{ item.member }})"
        location: DATA_SET
        wait: true
        return_output: true
        max_rc: 0
      loop:
        - dsn: Zxxxx.ANSB.JCL
          member: JOB1
        - dsn: Zxxxx.ANSB.JCL
          member: JOB2
      when: task_to_search not in active_tasks
```

> Challenge - What if you create a block for executing your jobs and print a message that it's happening or print a message if it's not and task is active?

➜Invoke the playbook with:  ansible-playbook -i inventory.yaml active_tasks.yaml 
You should get:
PLAY [Creating a copy of parmlib member] ***********************************************************************************************************************

TASK [Setting variables] ***************************************************************************************************************************************
ok: [zxplore]

TASK [Submitting maintenance jobs] *****************************************************************************************************************************
changed: [zxplore] => (item={'dsn': 'Z04683.ANSB.JCL', 'member': 'JOB1'})
changed: [zxplore] => (item={'dsn': 'Z04683.ANSB.JCL', 'member': 'JOB2'})

TASK [ansible.builtin.debug] ***********************************************************************************************************************************
ok: [zxplore] => {
    "submitted_jobs": {
        "changed": true,
        "msg": "All items completed",
        "results": [
            {
                "ansible_loop_var": "item",
                "asid": null,
                "changed": true,
                "creation_date": null,
                "ddnames": {
                    "byte_count": null,
                    "content": [],
                    "ddname": null,
                    "id": null,
                    "procstep": null,
                    "record_count": null,
                    "stepname": null
                },
                "duration": 1,
                "execution_time": "00:00:00",
                "failed": false,
                "invocation": {
                    "module_args": {
                        "encoding": null,
                        "from_encoding": "UTF-8",
                        "location": "data_set",
                        "max_rc": 0,
                        "return_output": true,
                        "src": "Z04683.ANSB.JCL(JOB1)",
                        "template_parameters": null,
                        "to_encoding": "IBM-1047",
                        "use_template": false,
                        "volume": null,
                        "wait_time_s": 30
                    }
                },
                "item": {
                    "dsn": "Z04683.ANSB.JCL",
                    "member": "JOB1"
                },
                "job_class": null,
                "job_id": "JOB07563",
                "job_name": null,
                "jobs": [
                    {
                        "asid": 0,
                        "class": "A",
                        "content_type": "JOB",
                        "cpu_time": 0,
                        "creation_date": "2025-11-17",
                        "creation_time": "2:09:53",
                        "ddnames": [
                            {
                                "byte_count": 1099,
                                "content": [
                                    "1                   J E S 2  J O B  L O G  --  S Y S T E M  S 0 W 1  --  N O D E  S V S C J E S 2        ",
                                    "0 ",
                                    " 12.09.53 JOB07563 ---- MONDAY,    17 NOV 2025 ----",
                                    " 12.09.53 JOB07563  IRR010I  USERID Z04683   IS ASSIGNED TO THIS JOB.",
                                    " 12.09.54 JOB07563  ICH70001I Z04683   LAST ACCESS AT 12:08:57 ON MONDAY, NOVEMBER 17, 2025",
                                    " 12.09.54 JOB07563  $HASP373 JCL1     STARTED - INIT 1    - CLASS A        - SYS S0W1",
                                    " 12.09.54 JOB07563  -                                      -----TIMINGS (MINS.)------                          -----PAGING COUNTS----",
                                    " 12.09.54 JOB07563  -STEPNAME PROCSTEP    RC   EXCP   CONN       TCB       SRB  CLOCK          SERV  WORKLOAD  PAGE  SWAP   VIO SWAPS",
                                    " 12.09.54 JOB07563  -HELLO                00      1      0       .00       .00     .0                BATCH        0     0     0     0",
                                    " 12.09.54 JOB07563  -JCL1     ENDED.  NAME-                     TOTAL TCB CPU TIME=      .00 TOTAL ELAPSED TIME=    .0",
                                    " 12.09.54 JOB07563  $HASP395 JCL1     ENDED - RC=0000",
                                    "0------ JES2 JOB STATISTICS ------",
                                    "-  17 NOV 2025 JOB EXECUTION DATE",
                                    "-            3 CARDS READ",
                                    "-           35 SYSOUT PRINT RECORDS",
                                    "-            0 SYSOUT PUNCH RECORDS",
                                    "-            2 SYSOUT SPOOL KBYTES",
                                    "-         0.00 MINUTES EXECUTION TIME"
                                ],
                                "ddname": "JESMSGLG",
                                "id": 2,
                                "procstep": "-",
                                "record_count": 18,
                                "stepname": "JES2"
                            },
                            {
                                "byte_count": 215,
                                "content": [
                                    "        1 //JCL1    JOB 1                                                         JOB07563",
                                    "          //***************************************************/                          ",
                                    "        2 //HELLO  EXEC PGM=IEFBR14                                                       "
                                ],
                                "ddname": "JESJCL",
                                "id": 3,
                                "procstep": "-",
                                "record_count": 3,
                                "stepname": "JES2"
                            },
                            {
                                "byte_count": 813,
                                "content": [
                                    " ICH70001I Z04683   LAST ACCESS AT 12:08:57 ON MONDAY, NOVEMBER 17, 2025",
                                    " IEFA111I JCL1 IS USING THE FOLLOWING JOB RELATED SETTINGS:",
                                    "          SWA=ABOVE,TIOT SIZE=32K,DSENQSHR=DISALLOW,GDGBIAS=JOB",
                                    " IEF142I JCL1 HELLO - STEP WAS EXECUTED - COND CODE 0000",
                                    " IEF373I STEP/HELLO   /START 2025321.1209",
                                    " IEF032I STEP/HELLO   /STOP  2025321.1209 ",
                                    "         CPU:     0 HR  00 MIN  00.00 SEC    SRB:     0 HR  00 MIN  00.00 SEC    ",
                                    "         VIRT:     8K  SYS:   228K  EXT:        0K  SYS:    11208K",
                                    "         ATB- REAL:                  1252K  SLOTS:                     0K",
                                    "              VIRT- ALLOC:      14M SHRD:       0M",
                                    " IEF375I  JOB/JCL1    /START 2025321.1209",
                                    " IEF033I  JOB/JCL1    /STOP  2025321.1209 ",
                                    "         CPU:     0 HR  00 MIN  00.00 SEC    SRB:     0 HR  00 MIN  00.00 SEC    "
                                ],
                                "ddname": "JESYSMSG",
                                "id": 4,
                                "procstep": "-",
                                "record_count": 13,
                                "stepname": "JES2"
                            }
                        ],
                        "duration": 1,
                        "execution_node": "SVSCJES2",
                        "execution_time": "00:00:00",
                        "job_class": "A",
                        "job_id": "JOB07563",
                        "job_name": "JCL1",
                        "origin_node": "SVSCJES2",
                        "owner": "Z04683",
                        "priority": 1,
                        "program_name": null,
                        "queue_position": 406,
                        "ret_code": {
                            "code": 0,
                            "msg": "CC",
                            "msg_code": "0000",
                            "msg_txt": "CC",
                            "steps": [
                                {
                                    "step_cc": 0,
                                    "step_name": "HELLO"
                                }
                            ]
                        },
                        "subsystem": "JES2",
                        "svc_class": null,
                        "system": "S0W1"
                    }
                ],
                "priority": null,
                "program_name": null,
                "queue_position": null,
                "ret_code": {
                    "code": null,
                    "msg": null,
                    "msg_code": null,
                    "msg_txt": null,
                    "steps": []
                },
                "svc_class": null
            },
            {
                "ansible_loop_var": "item",
                "asid": null,
                "changed": true,
                "creation_date": null,
                "ddnames": {
                    "byte_count": null,
                    "content": [],
                    "ddname": null,
                    "id": null,
                    "procstep": null,
                    "record_count": null,
                    "stepname": null
                },
                "duration": 1,
                "execution_time": "00:00:00",
                "failed": false,
                "invocation": {
                    "module_args": {
                        "encoding": null,
                        "from_encoding": "UTF-8",
                        "location": "data_set",
                        "max_rc": 0,
                        "return_output": true,
                        "src": "Z04683.ANSB.JCL(JOB2)",
                        "template_parameters": null,
                        "to_encoding": "IBM-1047",
                        "use_template": false,
                        "volume": null,
                        "wait_time_s": 30
                    }
                },
                "item": {
                    "dsn": "Z04683.ANSB.JCL",
                    "member": "JOB2"
                },
                "job_class": null,
                "job_id": "JOB07564",
                "job_name": null,
                "jobs": [
                    {
                        "asid": 0,
                        "class": "A",
                        "content_type": "JOB",
                        "cpu_time": 0,
                        "creation_date": "2025-11-17",
                        "creation_time": "2:09:59",
                        "ddnames": [
                            {
                                "byte_count": 1099,
                                "content": [
                                    "1                   J E S 2  J O B  L O G  --  S Y S T E M  S 0 W 1  --  N O D E  S V S C J E S 2        ",
                                    "0 ",
                                    " 12.09.59 JOB07564 ---- MONDAY,    17 NOV 2025 ----",
                                    " 12.09.59 JOB07564  IRR010I  USERID Z04683   IS ASSIGNED TO THIS JOB.",
                                    " 12.10.00 JOB07564  ICH70001I Z04683   LAST ACCESS AT 12:09:54 ON MONDAY, NOVEMBER 17, 2025",
                                    " 12.10.00 JOB07564  $HASP373 JCL2     STARTED - INIT 1    - CLASS A        - SYS S0W1",
                                    " 12.10.00 JOB07564  -                                      -----TIMINGS (MINS.)------                          -----PAGING COUNTS----",
                                    " 12.10.00 JOB07564  -STEPNAME PROCSTEP    RC   EXCP   CONN       TCB       SRB  CLOCK          SERV  WORKLOAD  PAGE  SWAP   VIO SWAPS",
                                    " 12.10.00 JOB07564  -WORLD                00      1      0       .00       .00     .0                BATCH        0     0     0     0",
                                    " 12.10.00 JOB07564  -JCL2     ENDED.  NAME-                     TOTAL TCB CPU TIME=      .00 TOTAL ELAPSED TIME=    .0",
                                    " 12.10.00 JOB07564  $HASP395 JCL2     ENDED - RC=0000",
                                    "0------ JES2 JOB STATISTICS ------",
                                    "-  17 NOV 2025 JOB EXECUTION DATE",
                                    "-            3 CARDS READ",
                                    "-           35 SYSOUT PRINT RECORDS",
                                    "-            0 SYSOUT PUNCH RECORDS",
                                    "-            2 SYSOUT SPOOL KBYTES",
                                    "-         0.00 MINUTES EXECUTION TIME"
                                ],
                                "ddname": "JESMSGLG",
                                "id": 2,
                                "procstep": "-",
                                "record_count": 18,
                                "stepname": "JES2"
                            },
                            {
                                "byte_count": 215,
                                "content": [
                                    "        1 //JCL2    JOB 1                                                         JOB07564",
                                    "          //***************************************************/                          ",
                                    "        2 //WORLD  EXEC PGM=IEFBR14                                                       "
                                ],
                                "ddname": "JESJCL",
                                "id": 3,
                                "procstep": "-",
                                "record_count": 3,
                                "stepname": "JES2"
                            },
                            {
                                "byte_count": 813,
                                "content": [
                                    " ICH70001I Z04683   LAST ACCESS AT 12:09:54 ON MONDAY, NOVEMBER 17, 2025",
                                    " IEFA111I JCL2 IS USING THE FOLLOWING JOB RELATED SETTINGS:",
                                    "          SWA=ABOVE,TIOT SIZE=32K,DSENQSHR=DISALLOW,GDGBIAS=JOB",
                                    " IEF142I JCL2 WORLD - STEP WAS EXECUTED - COND CODE 0000",
                                    " IEF373I STEP/WORLD   /START 2025321.1210",
                                    " IEF032I STEP/WORLD   /STOP  2025321.1210 ",
                                    "         CPU:     0 HR  00 MIN  00.00 SEC    SRB:     0 HR  00 MIN  00.00 SEC    ",
                                    "         VIRT:     8K  SYS:   228K  EXT:        0K  SYS:    11208K",
                                    "         ATB- REAL:                  1252K  SLOTS:                     0K",
                                    "              VIRT- ALLOC:      14M SHRD:       0M",
                                    " IEF375I  JOB/JCL2    /START 2025321.1210",
                                    " IEF033I  JOB/JCL2    /STOP  2025321.1210 ",
                                    "         CPU:     0 HR  00 MIN  00.00 SEC    SRB:     0 HR  00 MIN  00.00 SEC    "
                                ],
                                "ddname": "JESYSMSG",
                                "id": 4,
                                "procstep": "-",
                                "record_count": 13,
                                "stepname": "JES2"
                            }
                        ],
                        "duration": 1,
                        "execution_node": "SVSCJES2",
                        "execution_time": "00:00:00",
                        "job_class": "A",
                        "job_id": "JOB07564",
                        "job_name": "JCL2",
                        "origin_node": "SVSCJES2",
                        "owner": "Z04683",
                        "priority": 1,
                        "program_name": null,
                        "queue_position": 412,
                        "ret_code": {
                            "code": 0,
                            "msg": "CC",
                            "msg_code": "0000",
                            "msg_txt": "CC",
                            "steps": [
                                {
                                    "step_cc": 0,
                                    "step_name": "WORLD"
                                }
                            ]
                        },
                        "subsystem": "JES2",
                        "svc_class": null,
                        "system": "S0W1"
                    }
                ],
                "priority": null,
                "program_name": null,
                "queue_position": null,
                "ret_code": {
                    "code": null,
                    "msg": null,
                    "msg_code": null,
                    "msg_txt": null,
                    "steps": []
                },
                "svc_class": null
            }
        ],
        "skipped": false
    }
}

PLAY RECAP *****************************************************************************************************************************************************
zxplore                    : ok=3    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   

## Templating
➜now open playbook file:  templating_submi_job_and_get_output.yaml 

Templating is another useful function we can make use. On previous task we have submitted some jobs, but if these jobs need to be customized before we submit them?

Let's put our IEFBR14 jobs to allocate some datasets.

Ansible has the builtin `template` module that let us work with Jinja2 Templating.

So let's create our template job `job14-1.j2` to allocate a dataset using a variable for the DSNAME to allocate Zxxxx.ANSB.DSN1.

```
It is located under /templates local directory: job14-1.j2
//JCL14   JOB 1
//***************************************************/
//HELLO   EXEC PGM=IEFBR14
//DSN1    DD DSN={{dsname}}1,
//        DISP=(NEW,CATLG),
//        UNIT=SYSALLDA,
//        SPACE=(TRK,1)
```

Inside of the `.j2` file we use the same notation as in the playbook, using the `{{}}` to point a variable. And we can perform multiple operations, conditions, loop, following the same format we have seen, the `Jinja2`.

So let's how the template module works:

```
    - name: Prepare our job
      ansible.builtin.template:
        src: job14.j2
        dest: ./job14.jcl
      delegate_to: localhost
```


In the `src` we have the location where the template is on tontrol node, and on the `dest` where the results will be saved on target host.
➜now execute this playbook with:    ansible-playbook -i inventory.yaml templating_submit_job_and_get_output.yaml 

Just a last exercise with the templating, let's add multiple DD fields so we can pass a list of datasets from the playbook to be allocated.

So on our playbook, we will create a variable `datasets_to_be_allocated` that will be a list containing `ddname` and `dsname` for our template.

```
    - name: "Preparing for our tests"
      set_fact:
        datasets_to_be_allocated:
          - ddname: JCL
            dsname: Zxxxx.ANSB.JCL
          - ddname: REXX
            dsname: Zxxxx.ANSB.REXX
```

On the template we will have the `DD` statement in a for block:

```
{% for variable in list %}

{% endfor %}
```

So our template will be:

```
//JOB14 JOB (ACCT),'BR14 JOB',CLASS=A,
//  REGION=64M,MSGCLASS=X,MSGLEVEL=(1,1),
//  NOTIFY=&SYSUID
//****
//*
//****
//*
//HELLO EXEC PGM=IEFBR14
{% for dataset in datasets_to_be_allocated %}
//{{dataset.ddname}}  DD DSN={{dataset.dsname}},
//      DISP=(NEW,CATLG),
//      UNIT=SYSALLDA,
//      SPACE=(TRK,1)
{% endfor %}
```

## Restarting activities on ZXplorer

If you want to restart the hands on activities on the lpar use `restart.yaml` It will delete the jcls generated from template, datasets and files allocated on the lpar.


## Some of the sample playbooks you may want to try: 

	system_discover.yaml
  active_tasks.yaml
  list_apf.yaml 
	convert_text.yaml 
	copy_edit_submit.yaml 
	copy_local_dir_to_pds.yaml 
	copy_member.yaml 
	copy_parmlib_member.yaml 
	copy_to_dataset.yaml 
	copy_to_uss.yaml 
	create_dataset_and_listcat.yaml 
	dataset_allocate.yaml 
	hello.yaml
 	gather_facts.yaml
 	iplinfo_device.yaml 
	mvs_command.yaml 
	run_rexx_and_clist.yaml 
	smpe_list_sysmod.yaml 
	submit_job.yaml
 	submit_job2.yaml 
	submit_query_output_by_id.yaml 
	submit_query_retrieve.yaml 
	system_discover.yaml
 
	uri_sample.yaml
 
	vars_n_cond.yaml
 
	workflow_basic.yaml
 
	zosmf_dslist.yaml
 
	zosmf_submit_job.yaml
