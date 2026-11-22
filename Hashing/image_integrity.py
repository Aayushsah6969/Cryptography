from verify_integrity import file_integrity

if(file_integrity("../Samples/dog.jpg", "../Samples/dog-2.png")):
    print("Images are Identical")
else:
    print("Images are Different")

