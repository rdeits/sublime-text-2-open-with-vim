Sublime Text 2 Open With Vim
============================
Open the current file in Vim. This works in terminal and GVim on Linux
and MacVim on OSX.

Installation
------------

    $ cd ~/.config/sublime-text-2/Packages/
    $ git clone https://github.com/rdeits/sublime-text-2-open-with-vim OpenWithVim


Usage
-----

add the following to `User/Default (Linux).sublime-keymap`:

    { "keys": ["ctrl+shift+alt+i"], "command": "open_with_vim" },
	{ "keys": ["ctrl+alt+e"], "command": "open_with_gvim"}

AND/OR add the following to `User/Default (OSX).sublime-keymap`:

	{ "keys": ["super+ctrl+e"], "command": "open_with_gvim" }

