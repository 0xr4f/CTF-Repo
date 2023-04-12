from PIL import Image

# Load the input image
input_image = Image.open('output.jpg')

# Get the size of the image
width, height = input_image.size

# Process the pixels to change red pixels to white
for x in range(width):
    for y in range(height):
        # Get the color of the current pixel
        current_color = input_image.getpixel((x, y))

        # Check if the pixel is red
        if current_color[0] > 200 and current_color[1] < 50 and current_color[2] < 50:
            # Set the pixel to white
            input_image.putpixel((x, y), (255, 255, 255))

# Save the output image
input_image.save('flag.jpg')
