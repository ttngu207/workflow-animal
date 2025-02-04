import datajoint as dj
from elements_lab import lab
from elements_animal import subject, genotyping
from elements_lab.lab import Source, Lab, Protocol, User, Location


if 'custom' not in dj.config:
    dj.config['custom'] = {}

db_prefix = dj.config['custom'].get('database.prefix', '')


# ---------------------------------- Activate "lab" schema -------------------------------

lab.activate(db_prefix + 'lab')


# ------------------------- Activate "subject" and "genotyping" schema -------------------

subject.activate(db_prefix + 'subject', linking_module=__name__)

# Omit this schema if genotying is not needed
genotyping.activate(db_prefix + 'genotyping',  db_prefix + 'subject',  linking_module=__name__)
