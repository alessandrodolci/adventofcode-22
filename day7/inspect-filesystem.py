import os

PROMPT_CHAR = '$'
CD_COMMAND = "cd"
LS_COMMAND = "ls"

TOTAL_SPACE = 70000000
MINIMUM_NEEDED_SPACE = 30000000


class FilesystemObject:
    name: str

    def __init__(self, name: str) -> None:
        self.name = name


class Directory(FilesystemObject):
    parent: "Directory"
    objects: list[FilesystemObject]

    def __init__(self, name: str, parent: "Directory") -> None:
        super().__init__(name)
        self.parent = parent
        self.objects = []

    def getTotalDirectorySize(self) -> int:
        result = 0
        for object in self.objects:
            if isinstance(object, File):
                result += object.size
            elif isinstance(object, Directory):
                result += object.getTotalDirectorySize()

        return result


class File(FilesystemObject):
    size: int
    parent: Directory

    def __init__(self, name: str, parent: Directory, size: int) -> None:
        super().__init__(name)
        self.parent = parent
        self.size = size


def parse_filesystem(terminal_lines: list[str]) -> Directory:

    def parse_ls_line(directory: Directory, ls_line: str) -> None:
        ls_tokens = ls_line.split()
        if ls_tokens[0] == "dir":
            directory.objects.append(Directory(ls_tokens[1], directory))
        elif ls_tokens[0].isnumeric():
            directory.objects.append(
                File(ls_tokens[1], directory, int(ls_tokens[0])))

    current_line = terminal_lines.pop(0)
    root_directory = Directory(current_line.split()[2], None)
    current_directory = root_directory

    current_line = terminal_lines.pop(0)
    while current_line:
        tokens = current_line.split()
        if tokens[0] == PROMPT_CHAR and tokens[1] == CD_COMMAND:
            if tokens[2] == "..":
                current_directory = current_directory.parent
            else:
                current_directory = next(o for o in current_directory.objects if isinstance(
                    o, Directory) and o.name == tokens[2])
            try:
                current_line = terminal_lines.pop(0)
            except IndexError:
                current_line = None
        elif tokens[0] == PROMPT_CHAR and tokens[1] == LS_COMMAND:
            try:
                current_line = terminal_lines.pop(0)
            except IndexError:
                current_line = None
            while current_line and current_line[0] != PROMPT_CHAR:
                parse_ls_line(current_directory, current_line)
                try:
                    current_line = terminal_lines.pop(0)
                except IndexError:
                    current_line = None

    return root_directory


def get_dirs_under_100k(dirs: list[Directory], current_directory: Directory) -> list[Directory]:
    if current_directory.getTotalDirectorySize() <= 100000:
        dirs.append(current_directory)

    for directory in [o for o in current_directory.objects if isinstance(o, Directory)]:
        get_dirs_under_100k(dirs, directory)


def get_candidate_dirs(threshold: int, candidate_dirs: list[Directory], current_directory: Directory) -> Directory:
    if current_directory.getTotalDirectorySize() >= threshold:
        candidate_dirs.append(current_directory)
    for directory in [o for o in current_directory.objects if isinstance(o, Directory)]:
        get_candidate_dirs(threshold, candidate_dirs, directory)


with open(os.path.join("input", "input.txt"), "r") as input_file:
    terminal_lines = [line.strip() for line in input_file.readlines()]

root_directory = parse_filesystem(terminal_lines)

dirs_under_10k: list[Directory] = []
root_directory_size = root_directory.getTotalDirectorySize()
if root_directory_size <= 100000:
    dirs_under_10k.append(root_directory)
get_dirs_under_100k(dirs_under_10k, root_directory)
total_size_of_dirs_under_100k = sum(
    [d.getTotalDirectorySize() for d in dirs_under_10k]
)

space_available = TOTAL_SPACE - root_directory.getTotalDirectorySize()
space_to_delete = MINIMUM_NEEDED_SPACE - space_available
candidate_dirs: list[Directory] = []
get_candidate_dirs(space_to_delete, candidate_dirs, root_directory)

print("The total size of directories under 100000 is: " +
      str(total_size_of_dirs_under_100k))
print("The size of the smallest directory to delete to free up enough space for the update is: " +
      str(min([d.getTotalDirectorySize() for d in candidate_dirs])))
