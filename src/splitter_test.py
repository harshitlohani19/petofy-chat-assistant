from user_splitter import UserSplitAlgo
from loader import load_json

combined_data, data = load_json()
user_in = UserSplitAlgo()


chunked_result = user_in.chunk_size(10)
#
split_result = user_in.set_splitter(user_in.custom_splitter,data)
for i in split_result:
    print(i)
