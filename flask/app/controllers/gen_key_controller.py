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
    )

    return query

def get_data(email):
    print('------------email', email)

    return True