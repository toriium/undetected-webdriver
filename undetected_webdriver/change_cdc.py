import io, re, string, os


path = os.path.abspath("/tmp/chromedriver")
replacement = "akl_roepstdlwoeproslPOweos".encode()

with io.open(path, "r+b") as fh:
    for line in iter(lambda: fh.readline(), b""):
        if b"cdc_" in line:
            fh.seek(-len(line), 1)
            newline = re.sub(b"cdc_.{22}", replacement, line)
            fh.write(newline)
            print("\033[93m[*]\033[0m Linha encontrada e alterada com sucesso: ", line, "to", newline)