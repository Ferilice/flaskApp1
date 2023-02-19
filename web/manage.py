from flask.cli import FlaskGroup


from app import app, db
from app.models.contact import Contact
from app.models.BlogEntry import BlogEntry


cli = FlaskGroup(app)




@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()




@cli.command("seed_db")
def seed_db():
    db.session.add(
        Contact(firstname='สมชาย', lastname='ทรงแบด', phone='081-111-1111'))
    db.session.add(
        BlogEntry(name='สมชาย', message='ทรงแบด', email='somchine@gmail.com', date_created='2/19/2023 1:41 PM', date_updated='2/19/2023 1:41 PM'))
    db.session.commit()




if __name__ == "__main__":
    cli()
