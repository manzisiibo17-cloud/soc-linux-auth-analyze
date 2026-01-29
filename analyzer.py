failed_ip_counts = {}
THRESHOLD = 5
with open("logs/auth.log", "r") as file:
    for line in file:
        if "Failed password" in line:
            parts = line.split()
            ip_address = parts[parts.index("from") + 1]

            if ip_address in failed_ip_counts:
                failed_ip_counts[ip_address] += 1
            else:
                failed_ip_counts[ip_address] = 1


for ip, count in failed_ip_counts.items():
    if count >= THRESHOLD:
        print(f"ALERT: Possible brute-force attack from {ip} ({count} failed attempts)")