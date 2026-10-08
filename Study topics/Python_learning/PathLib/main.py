from pathlib import Path

data_dir = Path("data") / "output"
# data_dir = data_dir / "new"
data_dir.mkdir(parents=True, exist_ok=True)

output_file = data_dir / "results.txt"
output_file = data_dir / "results1.txt"

# output_file.write_text("Hello Worldfff")

print(output_file.read_text())