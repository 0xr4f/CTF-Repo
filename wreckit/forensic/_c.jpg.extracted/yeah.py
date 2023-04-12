from PIL import Image

# Load the input image
input_image = Image.open('flag.png')

# Get the current size of the image
width, height = input_image.size

# Calculate the new size of the image
new_width = 2000
new_height = int(height * (new_width / width))

# Resize the image to the new size
output_image = input_image.resize((new_width, new_height))

# Save the output image
output_image.save('output.jpg')
