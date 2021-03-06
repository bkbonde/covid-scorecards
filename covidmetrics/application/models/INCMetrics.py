from .. import db

class INCMetrics(db.Model):
    __tablename__ = 'inc_metrics'
    update_date = db.Column(db.DateTime, primary_key=True)
    county_name = db.Column(db.String,db.ForeignKey('counties.name'),primary_key=True)
    value = db.Column(db.Integer)

    def __init__(self, update_date, county_name, value):
        self.update_date=update_date
        self.county_name = county_name
        self.value = value

    def __repr__(self):
        return '<INCMetrics %r>' % (str(self.update_date))
