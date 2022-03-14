from dotenv import load_dotenv
import os

load_dotenv()

S3_BUCKET=os.environ.get('S3_BUCKET')
S3_KEY=os.environ.get('S3_KEY')
S3_SECRET=os.environ.get('S3_SECRET')
POSTGRESQL_URI=os.environ.get('POSTGRESQL_URI')