from app.models.secrets_model import Secrets, db

import pandas as pd
import sqlalchemy

def get_data_db(query):
    df = pd.read_sql(query.statement, db.engine)
    results = df.to_dict(orient='records')

    return results

def filter_query():
    query = Secrets.query.with_entities(
        Secrets.created_at,
        Secrets.raw,
        Secrets.key_id
    ).order_by(Secrets.created_at.desc())

    return query

def get_data():
    query = filter_query()
    data = get_data_db(query)

    return data


def get_secret_by_key_id(key_id):
    query = filter_query().where(Secrets.key_id == key_id)
    data = get_data_db(query)

    return data
