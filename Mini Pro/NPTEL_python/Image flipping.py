from PIL import Image
#flipping the image
img = Image.open("D:\Studies\PycharmProjects\PythonProject\Images\yyyy.jpg") #opening the image

#transposing
transposed_img = img.transpose(Image.Transpose.FLIP_LEFT_RIGHT)

#save it to a file
transposed_img.save("D:\Studies\PycharmProjects\PythonProject\Images\corrected.jpg")
print("Done flipping")

