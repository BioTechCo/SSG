import os
import gzip

if __name__ == '__main__':
    
    directory = input("Enter the directory: ")

    for filename in os.listdir(directory):
        if filename.endswith('.gz'):
            file_path = os.path.join(directory, filename)
            out_path = os.path.join(directory[:-3], '_'.join(filename.split('_')[1:]))
            output_filename = os.path.splitext(out_path)[0]
            with gzip.open(file_path, 'rb') as f_in:
                with open(output_filename, 'wb') as f_out:
                    f_out.write(f_in.read())
            
            print(f"Unzipped {filename} to {output_filename}")
            os.remove(file_path)