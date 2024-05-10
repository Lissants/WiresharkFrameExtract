def extract_frame_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    frame_number = ""
    source_address = ""
    destination_address = ""
    frame_type = ""

    frame_data = []

    for line in lines:
        if line.startswith("Frame"):
            frame_number = line.split()[1].strip(",")
        elif "Source: " in line:
            source_address = line.split("Source: ")[1].split()[-1]
        elif "Destination: " in line:
            destination_address = line.split("Destination: ")[1].split()[-1]
        elif "Type: " in line:
            frame_type = line.split("Type: ")[1].strip()
            frame_data.append(
                f"Frame {frame_number}, Src: {source_address}, Des: {destination_address}, Type: {frame_type}")

    return frame_data


def main():
    filename = "wireShark1.txt"
    frame_data = extract_frame_data(filename)
    for data in frame_data:
        print(data)


if __name__ == "__main__":
    main()
