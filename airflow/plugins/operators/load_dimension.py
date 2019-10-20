from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults



class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    
    insert_sql = """insert into {table} ({sql})"""
    upsert_sql = """upsert into {table} ({sql})"""

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 redshift_conn_id = '',
                 table = '',
                 sql = '',
                 mode = '',
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql = sql
        self.mode = mode
                

    def execute(self, context):
        #self.log.info('LoadDimensionOperator not implemented yet')
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        #self.log.info(f'INSERTING DATA INTO TABLE {table}...')
        if self.mode == 'insert':
            table_insert_sql = LoadDimensionOperator.insert_sql.format(
            table=self.table,
            sql=self.sql)
            redshift_hook.run(table_insert_sql)
        elif self.mode == 'append':
            table_append_sql = LoadDimensionOperator.insert_sql.format(
            table=self.table,
            sql=self.sql)
            redshift_hook.run(table_append_sql)
        
        #
        
