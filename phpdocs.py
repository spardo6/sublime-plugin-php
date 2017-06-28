import sublime
import sublime_plugin
import os
import re

# Escribit snippet
def write(view, str):
	view.run_command('insert_snippet', {
		'contents': str
	})


# Clase principal
class phpdocsCommand(sublime_plugin.TextCommand):

	def run(self, edit, insert=None):
		v = self.view
		if insert == "comment-after-sentence":
			self.CommentAfterSentence(v)
		elif insert == "comment-inline":
			self.commentInline(v)
		elif insert == "comment-multiline":
			self.commentMultiline(v)
		elif insert == "comment-extend":
			self.commentExtend(v);

	def CommentAfterSentence(self, view):
		write(view, " // $0")

	def commentInline(self, view):
		write(view, " $0 */")

	def commentMultiline(self, view):
		snippet = "\n"
		snippet += " * $0\n"
		snippet += " */"
		write(view, snippet)

	def commentExtend(self, view):
		write(view, "\n* $0")