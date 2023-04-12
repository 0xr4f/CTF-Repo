from PIL import Image

# Load the input image
input_image = Image.open('output.jpg')

# Get the size of the image
width, height = input_image.size

# Define the white color
white_color = (255, 255, 255) # (R, G, B) values of the white color

# Process the pixels to remove white pixels
for x in range(width):
    for y in range(height):
        # Get the color of the current pixel
        current_color = input_image.getpixel((x, y))

        # Check if the pixel color is white
        if current_color == white_color:
            # Set the pixel to be transparent
            input_image.putpixel((x, y), (0, 0, 0, 0))

# Save the output image with transparent background
input_image.save('jiah.png', format='PNG')
