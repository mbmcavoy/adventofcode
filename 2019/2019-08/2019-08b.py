def main():
    input_file = open("2019/2019-08/input.txt")

    sif_string = input_file.readline().strip()

    sif = [int(char) for char in sif_string]

    image_width = 25
    image_height = 6
    layer_size = image_width * image_height
    image_depth = int(len(sif) / layer_size)

    image = []
    for layer_index in range(image_depth):

        layer = []
        for y in range(image_height):
            
            row = []
            for x in range(image_width):
                index = layer_index * layer_size + y * image_width + x
                row.append(sif[index])
                
            layer.append(row)

        image.append(layer)

    for y in range(image_height):
        row = ["-"] * 25
        for x in range(image_width):
            for layer in range(image_depth):
                pixel = image[layer][y][x]
                if pixel == 0:
                    # Black
                    row[x] = " "
                    break
                elif pixel == 1:
                    # White
                    row[x] = "\u2588"
                    break
        print(f"Row {y}: {''.join(row)}")
        

# Execute the program
if __name__ == "__main__":
    main()
