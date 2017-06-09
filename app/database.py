from app import models
from app.forms import CreateAgentForm

_db = models.db


def insert(form):
    entry = None

    if isinstance(form, CreateAgentForm):
        entry = models.Agent(name="Name", description="Description")

    try:
        _db.session.add(entry)
        _db.session.commit()
    except Exception as e:
        print("Database insertion failure")


def retrieve(form):
    entries = None

    try:
        if isinstance(form, CreateAgentForm):
            entries = models.Agent.query.all()
    except Exception as e:
        print("Database list failure")

    return entries





