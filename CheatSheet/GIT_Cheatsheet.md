## GIT command Cheatsheet

#### Undo `git commit --amend`
```
$ git reset --soft HEAD@{1}
$ do_your_git_stuff_here
$ git commit -C HEAD@{1}
```

#### Revert the full commit
Create a _new_ commit that undoes all changes that were made in the bad commit.

`$ git revert commit_id`


#### Delete the last commit
```
git push origin +dd61ab32^:master
git reset HEAD^ --hard
git push origin -f
```
