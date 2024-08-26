import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime


def process_data(data):
    #Para criar dataframe e salvar como parquet
    df = pd.DataFrame([data])
    filename = f"raw_data_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)
    return filename

def prepare_dataframe_for_insert(df):
    df['data_ingestao'] = datetime.now()
    df['dado_linha'] = df.apply(lambda row: row.to_json(), axis=1)
    df['tag'] = 'example_tag'
    return df(['data_ingestao', 'dado_linha', 'tag'])