from mycroft import MycroftSkill, intent_file_handler
import webbrowser


class Showreports(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

 

    @intent_file_handler('showreports.intent')
    def handle_showreports(self, message):
        self.speak_dialog('Opening the report')
        dir_file = "/home/sopra/Downloads/OpenPowerBi.html"
        webbrowser.open('file://' + dir_file)


def create_skill():
    return Showreports()

