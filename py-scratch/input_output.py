import time

symbolic_mark = "|"

print("Sequence will be like this..")
print("package_manager / package_name / support / installed")

package_manager = input("Enter name of package manager here: ")
package_name = input("Enter name of package name here: ")
support = input("Enter if X11/Wayland / X11/Wayland boh here: ")
status = input("Indicate if the package is installed by typing Y & N if no: ")

print(package_manager, symbolic_mark , package_name, symbolic_mark, support, symbolic_mark, status);