#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import zipfile
from GlobalConfig import * 

git_diffCommond = 'git diff --name-only --diff-filter=ACMRTUXB %s %s assets'
git_archiveGitCommond = "git archive -o %s %s $(git diff --name-only --diff-filter=ACMRTUXB %s %s assets)"

def pickOneDiffAsset(oldTag,targetTag):
    os.chdir(projectPath)
    gitDiffCommond = git_diffCommond%(oldTag,targetTag)
    diffStr=os.popen(gitDiffCommond).read()
    print diffStr
    diffAssets = diffAssetsPath+"/update-%s-%s-noso.zip"%(oldTag,targetTag);
    if len(diffStr)> 0:
        #如果素材有变化，则打包变化的素材
        gitCommond = git_archiveGitCommond%(diffAssets,targetTag,oldTag,targetTag)
        print "gitCommond:"+gitCommond
        os.system(gitCommond)
    else:
        #如果素材没有差异，则创建一个目录结构，用于添加so文件
        pick_z =zipfile.ZipFile(diffAssets, 'w')
        pick_z.write("assets")
        pick_z.close()
  
def pickEveryDiffAssets():
    for tag in oldTags:
        pickOneDiffAsset(tag,targetTag)
     
pickEveryDiffAssets()