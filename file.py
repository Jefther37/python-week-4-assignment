def read_and_modify_file():
    try:
        # Ask the user for the input file name
        input_file = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_file, 'r') as file:
            lines = file.readlines()

        # Modify the content (example: add line numbers)
        modified_lines = [f"{idx + 1}: {line}" for idx, line in enumerate(lines)]

        # Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, 'w') as new_file:
            new_file.writelines(modified_lines)

        print(f"\n✅ File has been read and modified successfully!")
        print(f"Modified file saved as: {output_file}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("❌ Error: There was an issue reading or writing the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
