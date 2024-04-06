import os
import gzip

if __name__ == '__main__':
    
    directory = "idats/"

    for filename in os.listdir(directory):
        if filename.endswith('.gz'):
            file_path = os.path.join(directory, filename)
            output_filename = os.path.splitext(file_path)[0]
            with gzip.open(file_path, 'rb') as f_in:
                with open(output_filename, 'wb') as f_out:
                    f_out.write(f_in.read())
            
            print(f"Unzipped {filename} to {output_filename}")
            os.remove(file_path)