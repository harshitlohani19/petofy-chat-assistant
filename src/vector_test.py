from vector import Vector

vectors=Vector()

def main():
    name=input(str("Input name: "))
    vectors.set_vector(vectors.vector_name,name)
    
    loc=input(str("Enter location:"))
    vectors.set_vector(vectors.vector_loc,loc)


main()