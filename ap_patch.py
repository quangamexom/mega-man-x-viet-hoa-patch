"""Áp đúng bản vá Mega Man X V25 R2 lên ROM Europe có header."""
import argparse
import hashlib
from pathlib import Path

SOURCE_SHA = "2b648ecbebf0659a22910c6ada44d4440cfa19df96f2207a7ed5f56e5dfbb402"
PATCH_SHA = "baf1d51d006737426241530772069f7477b10f1df8b4728b40f40f3c8c532355"
TARGET_SHA = "5dcda6994f9620f413eabe80175d3642b020b2ee17840b50978dbf6c61571f6e"
PATCH_NAME = "MegaManX_VN_v25_muse_r2.ips"


def verify(data, expected, error):
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError(error)


def apply(rom):
    source = rom.read_bytes()
    verify(source, SOURCE_SHA, "Sai ROM gốc. Cần bản Europe có header 512 byte. Xem README.md.")
    patch = Path(__file__).with_name(PATCH_NAME).read_bytes()
    verify(patch, PATCH_SHA, "Sai patch IPS. Hãy giải nén lại gói V25 R2.")
    # Patch đã xác thực có kích thước đầu ra cố định, gồm record thường và RLE.
    output = bytearray(2097664)
    output[:len(source)] = source
    pos = 5
    while patch[pos:pos + 3] != b"EOF":
        offset = int.from_bytes(patch[pos:pos + 3], "big")
        size = int.from_bytes(patch[pos + 3:pos + 5], "big")
        pos += 5
        if size:
            chunk = patch[pos:pos + size]
            pos += size
        else:
            count = int.from_bytes(patch[pos:pos + 2], "big")
            chunk = patch[pos + 2:pos + 3] * count
            pos += 3
        output[offset:offset + len(chunk)] = chunk
    verify(output, TARGET_SHA, "ROM sau khi vá sai hash.")
    destination = rom.with_name("MegaManX_VN_v25_muse_r2.smc")
    if destination.exists() and destination.read_bytes() == output:
        return destination
    with destination.open("xb") as handle:
        handle.write(output)
    return destination


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rom", type=Path, help="Đường dẫn đến ROM gốc .smc")
    try:
        result = apply(parser.parse_args().rom)
        print("OK:", result)
    except FileExistsError:
        parser.exit(1, "Tên file đầu ra đã tồn tại với nội dung khác. Hãy đổi tên file đó rồi chạy lại.\n")
    except (ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")
