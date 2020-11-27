from sys import argv
from csv import DictReader, DictWriter

if len(argv) > 1:
    for filename in argv[1:]:
        try:
            with open(filename, mode="r", encoding="utf-8", newline="") as f:
                entries = [entry for entry in DictReader(f)]

                end = len(entries)
                for i in range(end // 2):
                    entries[i]["Position"], entries[end - 1 - i]["Position"] = (
                        entries[end - 1 - i]["Position"],
                        entries[i]["Position"],
                    )
        except Exception as e:
            print(e)
        else:
            with open(filename, mode="w", encoding="utf-8", newline="") as f:
                writer = DictWriter(f, fieldnames=list(entries[0].keys()))
                writer.writeheader()
                writer.writerows(reversed(entries))
                print("[OK]", filename)
else:
    print("No files given")
