import pkgutil

def list_accessible_libraries():
    libraries = []
    for _, name, _ in pkgutil.iter_modules():
        libraries.append(name)
    return libraries

if __name__ == "__main__":
    accessible_libraries = list_accessible_libraries()
    print("Accessible libraries:")
    for library in accessible_libraries:
        print(library)
