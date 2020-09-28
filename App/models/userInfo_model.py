from App.ext import db


class UserInfo(db.Model):
    __tablename__ = 'UserInfo'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(64))
    name = db.Column(db.String(64))
    stuCode = db.Column(db.String(64))
    email = db.Column(db.String(64))
    idtype = db.Column(db.String(64))
    sex = db.Column(db.String(64))
    bm = db.Column(db.String(64))
    zy = db.Column(db.String(64))
    bj = db.Column(db.String(64))
    clcc = db.Column(db.String(64))

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def update(self):
        db.session.commit()
        return True

    def rollback(self):
        db.session.rollback()
        return True
