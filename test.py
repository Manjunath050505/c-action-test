import os, subprocess

# Settings

TEST_DIR = "/tests"
CODE_FILE = "main.c"
COMPILER_TIMEOUT = 10.0  # seconds  
RUN_TIMEOUT = 10.0  # seconds

# Create absolute paths for the test directory and code file    
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")


# compile the program

print("building...")

try: 

    ret = subprocess.run(["gcc", code_path, "-o", app_path], 
    
                          stdout=subprocess.PIPE, 
                          stderr=subprocess.PIPE, 
                          timeout=COMPILER_TIMEOUT)

except Exception as e:
    print("Error during compilation:", str(e))
    exit(1)

# parse output

output = ret.stdout.decode("utf-8")
print("Compilation output:", output)
output = ret.stderr.decode("utf-8")
print("Compilation errors:", output)

# check to see if the compilation was successful
if ret.returncode != 0:
    print("Compilation failed with return code:", ret.returncode)
    exit(1)

# run the compiled program

print("running...")

try:
    ret = subprocess.run([app_path], 
                         stdout=subprocess.PIPE, 
                         stderr=subprocess.PIPE, 
                         timeout=RUN_TIMEOUT)

except Exception as e:
    print("Error during execution:", str(e))
    exit(1)

# parse output
output = ret.stdout.decode("utf-8")
print("Program output:", output)

#all testa passed! exit gracefully
print("All tests passed! Exiting gracefully.")
exit(0)
