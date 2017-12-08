创建/修改用户名和密码

```python
git config --global user.name [name]
git config --global user.email [email]
```

查看用户名和密码

```
git config user.name
git config user.email
```

创建版本库

```
git init
```

提交文件

```
1. git add [filename] //将文件添加到版本库
2. git commit -m "operate log"   //将文件添加到版本库
```

使用git status 查看git 状态

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

使用 git diff 查看具体变更内容

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

