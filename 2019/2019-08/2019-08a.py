def main():
    input_file = open("2019/2019-08/input.txt")

    sif_string = input_file.readline().strip()

    sif = [int(char) for char in sif_string]

    image_width = 25
    image_height = 6
    layer_size = image_width * image_height
    image_depth = int(len(sif) / layer_size)

    print(F"Image Depth is {image_depth} layers.")

    image = []
    layer_zeroCount = []
    for layer_index in range(image_depth):

        layer = []
        for pixel in range(layer_size):
            
            index = layer_index * layer_size + pixel
            layer.append(sif[index])

        layer_zeroCount.append(layer.count(0))
        image.append(layer)

    # Figure out which layer has the fewest zeroes
    minZeros = min(layer_zeroCount)
    minZeroLayer = layer_zeroCount.index(minZeros)

    result = image[minZeroLayer].count(1) * image[minZeroLayer].count(2)

    print(f"Layer {minZeroLayer} has the fewest zeroes, with {minZeros}.")

    print(f"The result is {result}.")


# Execute the program
if __name__ == "__main__":
    main()
