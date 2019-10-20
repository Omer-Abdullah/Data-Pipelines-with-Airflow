from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'
    
    insert_sql = """insert into {table} (start_time, userid, level, songid, artistid, sessionid, location, user_agent) {sql}"""

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 redshift_conn_id = '',
                 table = '',
                 sql = '',
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        # Map params here
        # Example:
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.sql = sql

    def execute(self, context):
        #self.log.info('LoadFactOperator not implemented yet')
        redshift_hook = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        fact_insert_sql = LoadFactOperator.insert_sql.format(
            table=self.table,
            sql=self.sql)
        
        redshift_hook.run(fact_insert_sql)
        
