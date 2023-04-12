from PIL import Image

# Load the input image
input_image = Image.open('flag.png')

# Resize the image to 2000 pixels
output_image = input_image.resize((2000, 2000))

# Save the output image
output_image.save('output.jpg')
