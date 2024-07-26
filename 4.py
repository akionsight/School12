def box(length, breadth, height):
    return length*breadth*height

convert_to_int = lambda s1, s2, s3: (int(s1), int(s2), int(s3))

length, breadth, height = input("Enter space seperated dimensions (length, breadth, height): ").split(' ')


int_dim = convert_to_int(length, breadth, height)

print(f"Volume of box is {box(int_dim[0], int_dim[1], int_dim[2])} sq. units")