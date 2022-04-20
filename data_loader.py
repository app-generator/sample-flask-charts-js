# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from csv import reader
import click
import sqlalchemy
def data_importer(db, DataModel, file_path, fields : list, dtypes : list):
    try:
        with open(file_path) as fp:
            rd = reader(fp)
            
            for cnt, row in enumerate(rd):
                data = {field: dtype(cell) for field, cell, dtype in zip(fields, row, dtypes) }
                record = DataModel(**data)
                db.session.add(record)
            db.session.commit()
            click.echo(click.style(f"Added {cnt} records in {DataModel.__name__}", fg="green"))
    except sqlalchemy.exc.IntegrityError:
        click.echo(click.style(f"Could not load data in {DataModel.__name__}, UNIQUE constraint failed", fg="red"))
        db.session.rollback()
    finally:
        db.session.close()
