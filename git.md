##### 本地仓库

###### 创建/修改用户名和密码

```python
git config --global user.name [name]
git config --global user.email [email]
```

###### 查看用户名和密码

```
git config user.name
git config user.email
```

###### 创建版本库

```
git init
```

###### 提交文件

```
1. git add [filename] //将文件添加到版本库
2. git commit -m "operate log"   //将文件添加到版本库
```

###### 使用git status 查看git 状态

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   readme.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

        git.md
        jsq/

no changes added to commit (use "git add" and/or "git commit -a")

```

###### 使用 git diff 查看具体变更内容

```
$ git diff readme.txt
diff --git a/readme.txt b/readme.txt
index d8036c1..013b5bc 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1,2 +1,2 @@
-Git is a version control system.
+Git is a distributed version control system.
 Git is free software.
\ No newline at end of file
```

###### 本地文件删除恢复 git checkout -- fileName

```
$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

        deleted:    git.md
        deleted:    jsq/jsq.txt

no changes added to commit (use "git add" and/or "git commit -a")
------------------------------------------------------------------------------------------------
$ git checkout -- git.md

$ git checkout -- jsq/jsq.txt

$ ls
git.md  jsq/  readme.txt

```

###### 版本回退git reset --hard head^

```
head 表示当前版本 head^ 表示上一个本  head^^ 表示上上个版本  head~100 上100个版本
```

###### 使用git log 查看提交历史/git log --pretty=oneline查看简洁历史

```
$ git log --pretty=oneline
327e76ec697ca773292d7a98ff0d23ac3c3c2a3f (HEAD -> master) add jsq.txt
262ee759e53ca8426798d310a56656af05263bef first add git.md
aae0bae0bd86bfd53a3b1d808744ce9826c38d1b add distributed
92222cc6fb454a3ca2f63b45ab8723d0eaabd0e2 wrote a readme file
```



###### 使用git reflog 查看操作日志

```
$ git reflog
327e76e (HEAD -> master) HEAD@{0}: reset: moving to HEAD
327e76e (HEAD -> master) HEAD@{1}: commit: add jsq.txt
262ee75 HEAD@{2}: commit: first add git.md
aae0bae HEAD@{3}: commit: add distributed
92222cc HEAD@{4}: commit (initial): wrote a readme file
```

###### 使用rm 删除文件

```
rm [fileName]
```

###### 使用git checkout 恢复文件

```
git checkout -- [filename]
```

##### 远程仓库

###### 在github创建一个仓库

https://github.com/new

###### 创建keygen

```
$ ssh-keygen -t rsa -C "gudujianjsk@gmail.com"
$ ssh-keygen -t rsa -C "achaoszc@gmail.com"
Generating public/private rsa key pair.
Enter file in which to save the key (/c/Users/ggczc/.ssh/id_rsa):
Created directory '/c/Users/ggczc/.ssh'.
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /c/Users/ggczc/.ssh/id_rsa.
遇到输入的地方直接回车
会在c/users/yourname/下会多出.ssh文件 秘钥在.ssh/id_rsa.pub中
复制keygen
在github 的setting中，添加ssh keys
```

###### 连接远程仓库

```
echo "# StudyGit" >> README.md
git add README.md
git commit -m "first commit"
git remote add origin git@github.com:[yourgithubaccount]/StudyGit.git
```

###### 文件提交到远程仓库

```
git push -u origin master //提交到 master分支
```

###### 从git上clone文件到本地

```
git clone git@github.com:michaelliao/gitskills.git
```

###### 分支管理

```
//创建dev 分支并且切换到分支
$ git checkout -b dev
//查看分支
$ git branch 
//合并分支
$ git merge dev
删除分支
$ git branch -d dev

```

