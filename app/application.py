# coding: utf-8
import cherrypy
import json
# --------------------------------------


class Application_cl(object):
	# --------------------------------------
	# ----------------------------------
	def __init__(self):
		# --------------------------------------
		# constructor
		pass
		# --------------------------------------
	# Methode "module" definieren

	def module(self):
		# --------------------------------------
		# Datei "module.json" im Lesemodus oeffnen
		json_data = open("data/module.json", "r")
		data = json.loads(json_data.read())
		# Inhalt von Datei zurueckgeben
		return json_data

	module.exposed = True
	# --------------------------------------

	def newFunction(self):
		daten = "lol"
	newFunction.exposed = True

	def	default(self, *arglist, **kwargs):
		# --------------------------------------
		msg_s =	"unbekannte Anforderung: " + \
			str(arglist) + \
			'' + \
			str(kwargs)

		raise cherrypy.HTTPError(404, msg_s)

	default.exposed = True
# EOF
