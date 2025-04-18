import os
import time

java_program = """
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World from Java!");
    }
}
"""
with open("Main.java", "w") as file:
    file.write(java_program)
print("Java program written to Main.java")


compile_status = os.system("javac Main.java")
if compile_status == 0:
    print("Compilation successful!")
else:
    print("Compilation failed!")
    raise RuntimeError("Java compilation failed.")


print("Executing Java program...")
execute_status = os.system("java Main")
if execute_status == 0:
    print("Execution successful!")
else:
    print("Execution failed!")

time.sleep(7)
os.system('cls')