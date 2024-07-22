from user_splitter import user_split_algo
from loader import load_json

combined_data, data = load_json()
user_in = user_split_algo()

chunked_result = user_in.chunk_size(10)
split_result = user_in.set_splitter(data, user_in.custom_splitter)
print(split_result)
