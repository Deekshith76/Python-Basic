try:
    d = [1,2,3,4]
    print(d[10])
except Exception:
    print("You've tried to access beyond the last element")
    
try: 
    f = open("/etc/passwdx")
    line = f.readline()
    print(line)

except (FileNotFoundError, PermissionError) as e:
    print(f"Couldn't open file. Error is {e}")