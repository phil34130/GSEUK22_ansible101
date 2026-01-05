#!/bin/env python
from zoautil_py.jobs import submit, read_output, list_dds
from zoautil_py.datasets import read
from time import sleep

def printjob(jobid):
 stepds = list_dds(jobid)
 for item in stepds:
  print(read_output(jobid, item["step_name"], item["dd_name"]))

def subsd(fname):

  print(120 * '*')
  print(read(fname))
  print(120 * '*')

  joppie = submit(fname, wait=True, timeout=20)

  print("Job name:" , joppie.name, " Job ID:" , joppie.job_id, " Job owner:", joppie.owner)
  print(120 * '*')

  i=1
  while joppie.status == 'AC':
    sleep(1.0)
    print('\r Running job', i * '.',"end =", flush=True)
    i+=1
    joppie.refresh()

  printjob(joppie.job_id)
  print(120 * '*')

subsd('Z04683.ANSB.JCL(HELLO)')
