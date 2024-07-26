from base_splitter import BaseSplitter

class ChunkSplitter(BaseSplitter):
    def __init__(self):
        self.chunks_size = 0

    def chunk_size(self, chunks_size) -> int:
        self.chunks_size = chunks_size
        return self.chunks_size

    def splitter(self, data):
        ids = 0
        for i in range(0, len(data), self.chunks_size):
            chunk = data[i:i + self.chunks_size]
            chunk_ids = [str(ids + j) for j in range(len(chunk))]
            yield chunk, chunk_ids
            #ids += len(chunk)

    def set_splitter(self, splitter_callback, data):
        return splitter_callback(data)