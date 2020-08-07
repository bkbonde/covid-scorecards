from datetime import datetime
import json
from ..Snapshot import Snapshot

class SpaceSnapshot(Snapshot):

    def __init__(self, district):
        self.district = district
        with open('data/base_data.json') as f:
            self.base_data = json.load(f)[self.district.id]['space']

    def status(self):
        data = {
            'district_id': self.district.id,
            'update_date': datetime.today(),
            'status': True,
            'facilities': []
        }

        for f in self.base_data['facilities']:
            r={
                'facility': f['facility'],
                'update_date': datetime.today(),
                'status': True,
                'rooms': []
            }

            for room in f['rooms']:
                t = {
                    'room_type': room['room_type'],
                    'room_count': room['room_count'],
                    'room_avg_capacity': room['capacity']/room['room_count'],
                    'capacity': room['capacity'],
                    'demand': room['demand'],
                    'fill_pct': room['demand']/room['capacity'],
                    'avg_class': room['demand']/room['room_count'],
                    'status': (room['demand']<room['capacity'])
                }
                r['rooms'].append(t)
                if not t['status']:
                    r['status'] = False

            data['facilities'].append(r)
            if not r['status']:
                data['status'] = False

        return data