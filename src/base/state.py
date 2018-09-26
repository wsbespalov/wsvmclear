
from messages import Messages

class State:
    idle = 0
    start = 1
    pending = 2
    downloading = 3
    parsing = 4
    caching = 5
    saving = 6
    undefined = 7

    def __init__(self):
        pass

    def decode_to_string(self, state):
        if state == self.idle:
            return Messages.idle
        if state == self.start:
            return Messages.start
        if state == self.pending:
            return Messages.pending
        if state == self.downloading:
            return Messages.downloading
        if state == self.parsing:
            return Messages.parsing
        if state == self.caching:
            return Messages.caching
        if state == self.saving:
            return Messages.saving
        return Messages.undefined

    def encode_to_state(self, state):
        if state == Messages.idle:
            return self.idle
        if state == Messages.start:
            return self.start
        if state == Messages.pending:
            return self.pending
        if state == Messages.downloading:
            return self.downloading
        if state == Messages.parsing:
            return self.parsing
        if state == Messages.caching:
            return self.caching
        if state == Messages.saving:
            return self.saving
        if state == Messages.undefined:
            return self.undefined