from contacts_app import app


def db_init():
    # Use this function to initalizate a default database with exemples.
    from contacts_app import db
    from contacts_app.models import User, Contact
    db.create_all()
    db.session.commit()
    u1 = User(username='demo', password='123456')
    db.session.add(u1)
    db.session.commit()
    c1 = Contact(name='Terry Carter', email='terry.carter@example.com',
                 phone='(260)-609-5692', user_id=u1.id)
    db.session.add(c1)
    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    app.run(debug=True)
