from vector_test import User_vector
user_vector= User_vector()

# Using the vector_name method as a callback
result_name = user_vector.set_vector(user_vector.vector_name, "XYZ")
print(result_name)