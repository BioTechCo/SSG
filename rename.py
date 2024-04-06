import os

if __name__ == '__main__':
    
    directory = 'idats/'
    for filename in os.listdir(directory):
        if filename.endswith('.idat'):
            file_path = os.path.join(directory, filename)
            out_path = os.path.join(directory, "_".join(filename.split("_")[1:]) + ".idat")
            os.rename(file_path, out_path)