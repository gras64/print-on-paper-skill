from mycroft import MycroftSkill, intent_file_handler


class PrintOnPaper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('paper.on.print.intent')
    def handle_paper_on_print(self, message):
        self.speak_dialog('paper.on.print')


def create_skill():
    return PrintOnPaper()

