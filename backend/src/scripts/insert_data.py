import pandas as pd
import numpy as np
from sqlalchemy.exc import SQLAlchemyError
from db.database import sessionLocal
from db.models import Track
import faiss
from pathlib import Path

