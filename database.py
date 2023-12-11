from sqlalchemy import create_engine, text

db_connection_string = 'paste_db_connection_string_here'

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem",
                       }})
