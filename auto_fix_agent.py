def apply_fix_to_file(filename: str, instruction: str) -> bool:
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()

        # Look for line to remove based on the instruction
        for i, line in enumerate(lines):
            if "throw new Error" in line:
                print(f"🛠️ Removing line: {line.strip()}")
                del lines[i]
                break

        with open(filename, 'w') as f:
            f.writelines(lines)

        return True
    except Exception as e:
        print(f"❌ Failed to apply fix: {str(e)}")
        return False
