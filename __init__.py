from mycroft import MycroftSkill, intent_file_handler


class Showreport(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('showreport.intent')
    def handle_showreport(self, message):
        self.speak_dialog('showreport')


def create_skill():
    return Showreport()

