from shape_factory import ShapeFactory

def shapes_client():
    shape_factory = ShapeFactory()
    shape_name = input("Enter the name of the shape: ")

    shape = shape_factory.create_shape(shape_name)

    print(f"The type of object created: {type(shape)}")
    print(f"The area of the {shape_name} is: {shape.calculate_area()}")
    print(f"The perimeter of the {shape_name} is: {shape.calculate_perimeter()}")


shapes_client()