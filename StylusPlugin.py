#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import sublime
import sublime_plugin

# fix for import order

sys.path.append(os.path.join(sublime.packages_path(), 'LiveReload'))
LiveReload = __import__('LiveReload')
sys.path.remove(os.path.join(sublime.packages_path(), 'LiveReload'))


class StylusRefresh(LiveReload.Plugin, sublime_plugin.EventListener):

    title = 'Stylus Reload'
    description = 'Refresh css when stylus file is saved'
    file_types = '.styl'
    this_session_only = False
    file_name = ''

    def on_post_save(self, view):
        self.original_filename = os.path.basename(view.file_name())

        if self.should_run(self.original_filename):
            self.file_name_to_refresh = \
                self.original_filename.replace('.styl', '.css')
            dirname = os.path.dirname(view.file_name())
            self.on_compile()

    def on_compile(self):
        print(self.original_filename, self.file_name_to_refresh)
        settings = {
            'path': self.file_name_to_refresh,
            'apply_js_live': False,
            'apply_css_live': True,
            'apply_images_live': True,
            }
        self.sendCommand('refresh', settings, self.original_filename)
