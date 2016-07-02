#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import re

def main():
  filename = os.getenv('TM_FILEPATH')
  project_dir = os.getenv('TM_PROJECT_DIRECTORY')
  if not filename:
    filename = sys.argv[1]
  m = re.search('/features/(.+)\.feature$', filename)
  if not m:
    print "Cannot find feature ! : " + filename
    return
  feature = m.group(1)
  print "Found feature:  {0}\n".format(feature)
  cucumber_args = "cucumber.js '{0}/cucumber/features/{1}.feature' --require '{0}/cucumber/features/step_definitions/{1}.coffee'".format(project_dir,feature)
  os.system(cucumber_args)

if __name__ == '__main__':
  main()
