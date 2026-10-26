from database import engine,Base
from model import PlannerTable

Base.metadata.create_all(bind=engine)

print("table created successfully")
