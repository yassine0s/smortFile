class fileHandling:
    def __init__(self, file_path, mode) -> None:
        self.file_path = file_path
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.close()

    def open(self):
        "open file"
        if not self.file or self.file.closed:
            try:
                self.file = open(self.file_path, self.mode)
            except FileNotFoundError:
                print(f"Error: file '{self.file_path} not found.")
                self.file = None
            except PermissionError:
                print(f"Error: Permission denied for file {self.file_path}")
                self.file = None
        else:
            print("warning: File already open")

    def close(self):
        "Manually close the file"
        if self.file and not self.file.closed:
            self.file.close()

    def read(self):
        if self.file and not self.file.closed:
            return self.file.read()
        else:
            raise ValueError("File is not open")

    def write(self,content):
        if self.file and not self.file.closed:
            self.file.write(content)
        else:
            raise ValueError("File is not open")
