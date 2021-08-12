#!/usr/bin/python
#
# Copyright (c) 2018 drafear
#
# Ignore '_*' problems

import re
import itertools

import rime.basic.targets.problem   # target dependency
import rime.basic.targets.project   # target dependency
import rime.basic.targets.solution  # target dependency
import rime.basic.targets.testset   # target dependency
from rime.core import taskgraph
from rime.core import targets

class Project(targets.registry.Project):
  def PreLoad(self, ui):
    super(Project, self).PreLoad(ui)
    def ignore_config(reg_str):
      self.reg = re.compile(reg_str)
    self.exports['ignore_config'] = ignore_config
    ignore_config('^_')

  def _ChainLoad(self, ui):
    super(Project, self)._ChainLoad(ui)
    self.problems = [problem for problem in self.problems if self.reg.search(problem.name) is None]

targets.registry.Override('Project', Project)
