# app/models.py

from app import db

class Bucketlist(db.Model):
    """
    Class represents the bucketlist table
    """
    __tablename__ = 'bucketlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(
        db.DateTime, default=db.func.current_timestamp(), 
        onupdate=db.func.current_timestamp()
    )

    def __init__(self, name):
        """
        Initialize with name
        """
        self.name = name

    def save(self):
        """
        Save a bucketlist to the database
        """
        db.session.add(self)
        db.session.commit()

    # static method
    @staticmethod
    def get_all():
        """
        Returns all bucketlists.
        """
        return Bucketlist.query.all()

    def delete(self):
        """
        Delete a bucketlist
        """
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        """
        Return a full formated bucketlist
        """
        return "<Bucketlist: {}>".format(self.name)



