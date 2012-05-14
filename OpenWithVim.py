import sublime
import sublime_plugin
import subprocess
import platform

class OpenWithVimCommand(sublime_plugin.WindowCommand):
    def get_path(self):
        if self.window.active_view():
            return self.window.active_view().file_name()
        else:
            sublime.error_message(__name__ + ": No file to open.")
            return None

    def run(self):
        path = self.get_path()
        if path is not None:
            self.open_vim(path)

    def open_vim(self, path):
        local_os = platform.system()
        if local_os == 'Linux':
            terminal = "gnome-terminal"
            option = "--command"
            vim = "/usr/bin/vim"
            args = [terminal, option, vim + ' "' + path + '"']
        else:
            sublime.error_message("Sorry, I don't know how to open terminal vim on this platform: %s. Try open_with_gvim" % local_os)
            return
        subprocess.Popen(args)


class OpenWithGvimCommand(OpenWithVimCommand):
    def open_vim(self, path):
        local_os = platform.system()
        if local_os == 'Darwin':
            args = ["mvim", path]
        else:
            args = ["gvim", path]
        subprocess.Popen(args)

