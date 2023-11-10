"""
  UC101: Create project
"""

import mlrun
from qgate.uc.ucbase import UCBase
import os
import glob
import json


class UC101(UCBase):

    def __init__(self, environment):
        super().__init__(environment, self.__class__.__name__)

    def exec(self):

        # create projects
        dir=os.path.join(os.getcwd(), self._model_definition, "01-model", "01-project", "*.json")
        for file in glob.glob(dir):
            with open(file, "r") as json_file:
                json_content = json.load(json_file)
                name, desc, lbls, kind=self._get_json_header(json_content)

                #TODO: asset kind

                # create project
                #self._log(f"Creating project '{name}'...")
                #self._projects.append(name)
                prj=mlrun.get_or_create_project(name, context="./", user_project=False)
                prj.description=desc
                for lbl in lbls:
                    prj.metadata.labels[lbl]=lbls[lbl]
                prj.save()

