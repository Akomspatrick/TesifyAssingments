# How to use multiple github account on the same system

## Valuable documents from. ==>

- https://www.freecodecamp.org/news/manage-multiple-github-accounts-the-ssh-way-2dadc30ccaca/
- https://gist.github.com/jexchan/2351996

ssh-add -l will list all the SSH keys attached to the ssh-agent. Remove all of them and add the one key you are about to use.

If it’s to a personal Git account that you are about to push:

$ ssh-add -D //removes all ssh entries from the ssh-agent
//$ ssh-add ~/.ssh/gmailgitprojects // Adds the relevant ssh key

//reset your remote => git remote set-url origin git@github.com-gmailgitprojects:Akomspatrick/CodeChallenge.git
 git remote set-url origin git@github.com-gmailgitprojects:Akomspatrick/CodeChallenge.git
$ git config user.name "activehacker"
$ git config user.email "jexlab@gmail.com" 
or you can have global git config $ git config --global user.name "jexchan" $ git config --global user.email "jexchan@gmail.com"