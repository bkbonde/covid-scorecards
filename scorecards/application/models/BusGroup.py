from .. import db

class BusGroup(db.Model):
    __tablename__ = 'bus_groups'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)
    district = db.Column(db.Integer)
    available = db.Column(db.Integer)
    required = db.Column(db.Integer)
    update_date = db.Column(db.DateTime)
    recorder_id = db.Column(db.Integer,db.ForeignKey('users.id'))


    def __init__(self, id, description, district, available, required, update_date, recorder_id):
        self.id = id
        self.description = description
        self.district = district
        self.available = available
        self.required = required
        self.update_date = update_date
        self.recorder_id = recorder_id

    def __repr__(self):
        return '<BusGroup %r>' % (self.description)
