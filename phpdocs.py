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
		self.edit = edit

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
		write(view, " " + self.contentLine() + "$0 */")

	def commentMultiline(self, view):
		snippet = "\n"
		snippet += " * $0\n"
		snippet += " */"
		write(view, snippet)

	def commentExtend(self, view):
		write(view, "\n* $0")

	# Obtener contenido de la linea
	def contentLine (self):
		v = self.view # Vista actual
		point = v.sel()[0].end() # Donde se encuentra el cursor
		region = sublime.Region(point, v.line(point).end()) # Desde el cursor hasta el final de la linea
		text = v.substr(region).strip() # Texto de la linea
		v.erase(self.edit, region) # Elimina el texto
		return text