from loader import load_json
from base_splitter import Basesplitter

combined_data, data = load_json()


class UserSplitAlgo(Basesplitter):

    def chunk_size(self, chunks_size):
        self.chunks_size = chunks_size
        return self.chunks_size
    
    def custom_splitter(self, data):
        chunks = []
        for i in range(0, len(data), self.chunks_size):
            chunks.append(data[i:i+self.chunks_size])  
        return chunks    
    
    def set_splitter(self, splitter_callback, data):
        result = splitter_callback(data)
        return result