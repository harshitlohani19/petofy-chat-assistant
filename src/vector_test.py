from src.user_vector_config import User_vector
user_vector= User_vector()

# Using the vector_name method as a callback
result_name = user_vector.set_vector(user_vector.vector_name, "xyz")
print(result_name)