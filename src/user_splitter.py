from loader import load_json
from splitting import Basesplitter

combined_data, data = load_json()


class user_split_algo(Basesplitter):

    def chunk_size(self, chunks_size):
        self.chunks_size = chunks_size
        return self.chunks_size
    
    def custom_splitter(self, data):
        chunks = []
        for i in range(0, len(data), self.chunks_size):

            chunks.append(data[i:i+self.chunks_size])  
        return chunks    
    
    def set_splitter(self, combined_text, splitter_callback):
        result = splitter_callback(combined_text)
        return result