from data_collection import DataCollection
from data_processing import DataProcessing
from indexing import Indexing

import logging
import pandas as pd
from pathlib import Path

logging.basicConfig(level=logging.INFO)

def main():

    collector = DataCollection('combined_spotify_data.csv')

    df = collector.load_data()

    processor = DataProcessing()
    processed_df = processor.preprocess_data(df)

    output_path = Path(__file__).parent.parent / 'data' / 'processed_data.csv'
    processed_df.to_csv(output_path, index=False)
    logging.info(f"Processed data saved to {output_path}")


    indexer = Indexing(processor.audio_features, processed_df)

    indexer.create_index()
    
    logging.info("Indexing completed")
    

    

if __name__ == "__main__":
    main()

