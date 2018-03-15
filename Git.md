# Git教程
## Git
 - 分布式版本控制系统
 - 去仓库中心
 - 设立交换中心跟踪并管理的修改
## 安装配置Git
```
[root@localhost ~]#yum install git.x86_64
[git@localhost ~]\$ git config --global user.name "name"
[git@localhost ~]\$ git config --global user.email "email"
```
## repository
### 创建本地repository

1、创建一个空目录
```
[git@localhost ~]\$ mkdir learngit
[git@localhost learngit]\$ pwd
/home/git/learngit
```
2、通过git init命令把这个目录变成Git可以管理的仓库目录
```
[git@localhost learngit]\$ git init
Initialized empty Git repository in /home/git/learngit/.git/
```
### 工作区、暂存区

电脑里能看到的目录叫**工作区**
.git的目录，这个目录是Git来跟踪管理版本库的，其中最重要的就是称为stage（或者叫index）的**暂存区**，还有Git为我们自动创建的第一个分支master，以及指向master的一个指针叫**HEAD**
每当你觉得文件修改到一定程度的时候，就可以“保存一个快照”，这个快照在Git中被称为**commit**
## 基本使用

**git add**把要提交的所有修改放到暂存区（Stage）
**git commit**一次性把暂存区的所有修改提交到分支
**git status**要随时掌握工作区的状态
**git diff**如果git status告诉你有文件被修改过，用git diff可以对比工作区和分支的区别
**git log**git log命令查看文件每次都改了什么内容
### 把文件添加到版本库

1、在仓库（子）目录下编辑文件
2、命令git add把文件添加到仓库
3、git commit把文件提交到仓库
### 提交文件修改

提交修改和提交新文件是一样的
1、在仓库（子）目录下修改文件
2、命令git add把文件添加到仓库
3、git commit把文件提交到仓库
### 撤销及回退

撤销工作区修改git checkout -- *file*
撤销缓冲区修改（回退至上个版本）git reset HEAD *file*
回退版本的时候，Git仅仅是把HEAD从指向回退位置**HEAD**表示当前版本，上一个版本就是HEAD^，上上一个版本就是HEAD^^，往上100个版本HEAD~100
找到版本号git reflog
撤销至某个个版本git reset --hard 版本号

## 远程仓库
### 管理远程仓库

已有目录，初始化目录：
```
git remote add origin https://github.com/496092102/learngit.git
```
暂无目录，执行克隆：
```
git clone git@github.com:496092102/gitskills.git
```
使用https速度慢且每次推送都必须输入口令，但是在某些只开放http端口的公司内部就无法使用ssh协议而只能用http
### 推送内容至远程仓库

把本地库的所有内容推送到远程库上：
```
git push -u origin master
```
-u参数：Git不但会把本地的master分支内容推送的远程新的master分支，还会把本地的master分支和远程的master分支关联起来，在以后的推送或者拉取时就可以简化命令
本地作了commit，就可以通过以下命令把本地master分支的最新修改推送至GitHub：
```
git push origin master
```
## 分支管理

创建了一个属于你自己的分支，别人看不到，还继续在原来的分支上正常工作，而你在自己的分支上干活，想提交就提交，直到开发完毕后，再一次性合并到原来的分支上，这样，既安全，又不影响别人工作
