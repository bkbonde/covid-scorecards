from datetime import datetime


class Snapshot:

    def __init__(self, dc):
        self.dc = dc

    def status(self):
        data = {
            'update_date': datetime.today(),
            'status': False,
        }
        return data
