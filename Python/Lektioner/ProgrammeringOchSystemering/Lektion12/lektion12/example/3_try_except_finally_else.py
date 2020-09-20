def success():
    print("Success")
    return True


print("----- All went fine scenario -----")
try:
    success()
except Exception as e:
    print(f"In except Exception with e {e}")
else:
    print("No failure occurred")
finally:
    print("Always do this")

print("----- Done -----\n")

print("----- Something went wrong scenario -----")
try:
    raise RuntimeError("Something went so wrong")
except RuntimeError as re:
    print(f"In except RuntimeError with re {re}:")
except Exception as e:
    print(f"In except Exception with e {e}:")
else:
    print("No failure occurred")
finally:
    print("Always do this")

print("----- Done -----\n")
