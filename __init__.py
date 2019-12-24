from mycroft import MycroftSkill, intent_file_handler
import webbrowser
import os


class Showreports(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

 

    @intent_file_handler('showreports.intent')
    def handle_showreports(self, message):
        self.speak_dialog('Opening the report')
        os.system("start cmd")
        #dir_file = "/home/sopra/Downloads/codebeautify.html"
        #webbrowser.open('file://' + dir_file)


def create_skill():
    return Showreports()

