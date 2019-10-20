import logging
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 redshift_conn_id = '',
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        self.redshift_conn_id = redshift_conn_id

    def execute(self, context):
        #self.log.info('DataQualityOperator not implemented yet')
        redshift_hook = PostgresHook(self.redshift_conn_id)
        
        checking_sql = """select count(*) from {}"""
        
        tables = ['songs', 'users', 'artists', 'time']
        
        for table in tables:
            formated_sql = checking_sql.format(table)
            records = redshift_hook.get_records(formated_sql)
            if records is None or records == 0:
               raise ValueError(f'Data quality check failed. {table} returned no rows')
            if len(records) < 1 or len(records[0]) < 1:
                raise ValueError(f'Data quality check failed. {table} returned 0 rows')
            else:
                logging.info(f'Data quality on table {table} check passed with {records[0][0]} records')
        