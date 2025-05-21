def read_and_modify_file():
    try:
        # Ask user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("\nOriginal Content:")
            print(content)

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Ask for a name to save the modified file
        output_filename = input("Enter the name for the modified file to save: ")

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"\nModified content saved to '{output_filename}' successfully!")

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except IOError:
        print("❌ Error: There was a problem reading or writing the file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()

