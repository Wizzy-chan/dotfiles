This repo contains my dotfiles so I can keep them the same for all my machines.

There is a helper script to help make symlinks into .config or wherever they need to go.  
Use it with the following commands:

```bash
./helper.py link [modules]
```
Creates symlinks for the provided modules.

```bash
./helper.py unlink [modules]
```
Removes symlinks for the provided modules.

Each module is just a folder containing some dotfiles for an application. There is a `__init__.py` file which contains the symlink targets for that application, e.g.
```python
TARGETS = [ ('link path', 'dotfile path') ]
```
where the link path is relative to `$HOME` and the dotfile path is relative to the module directory. For example `('.bashrc', 'bashrc')` in a module `~/dotfiles/bash` creates a symlink from `~/.bashrc` to `~/dotfiles/bash/bashrc`.

Maybe in the future I'll add a way to use python to generate the dotfiles because I liked that when using Nix.
