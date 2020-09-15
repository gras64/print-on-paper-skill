from mycroft import MycroftSkill, intent_file_handler
import cups


class PrintOnPaper(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        host = str(self.settings.get('host'))
        self.log.info(host)
        conn = cups.Connection()
        printers = conn.getPrinters ()
        for printer in printers:
            print(printer, printers[printer]["device-uri"])
        if not host == "None":
            printer = getNetworkPrinter()(host=host, port=9100)
            self.register_intent_file('paper.on.print.intent', self.handle_paper_on_print)

    def handle_paper_on_print(self, message):
        self.speak_dialog('paper.on.print')
        printer.text("Hello World")
        printer.lf()


def create_skill():
    return PrintOnPaper()

